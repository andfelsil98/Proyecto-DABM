# coding= UTF-8
from flask import Flask, render_template, request
import os

#usuarios = []

class user:
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
        self._file = os.path.join(os.path.dirname(__file__), "bd/users.csv")
    
        
    def saveToFile(self):   
        """Esta función crea un archivo csv y añade los usuarios que se creen 
        al archivo pacientes.csv"""
        file = open(self._file, "a")
        datos = str(self.usuario) + ";" + str(self.password) + "\n"
        file.write(datos)
        file.close()   

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/', methods = ["POST"])
def validar():
    nombreArchivo = "bd/users.csv"
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        
        resultado = verificar(usuario, password, nombreArchivo)
        if resultado == 'existe':
            return render_template("main.html", title = "Inicio")   
        else: 
            return render_template("login.html", title = "Login", resultado = resultado)    

@app.route('/registro', methods = ["GET","POST"])  
def registro1():
    nombreArchivo = "bd/userAdmin.csv"
    if request.method == "POST":
        usuarioAdmin = request.form["usuarioAdmin"]
        passwordAdmin = request.form["passwordAdmin"]
        verificacion = verificar(usuarioAdmin, passwordAdmin, nombreArchivo)
        if verificacion == "existe":
            verificacion = "primer ingreso"
            return render_template("registro.html", title = "Registro", verificacion = verificacion)     
        elif verificacion == "no existe":
            return render_template("login.html", title = "Login", verificacion = verificacion)

        ######################################################
        elif verificacion == 'vacio':
            return render_template('login.html', title = 'Login', verificacion = verificacion)

@app.route('/registro/validar', methods = ["GET","POST"])
def registro2():
    if request.method == "POST":
        usuario = request.form["usuarioRegistro"]
        password1 = request.form["passwordRegistro1"]
        password2 = request.form["passwordRegistro2"]
        verificacion = verificarRegistro(usuario, password1,password2)
        if verificacion == "existe" and password1 != "" and password2 != "":
            return render_template("registro.html", title = "Registro", verificacion = verificacion) 

        elif verificacion == 'repetidos' and password1 != "" and password2 != "":
            return render_template("registro.html", title = "Registro", verificacion = verificacion)

        elif verificacion == "no existe" and password2 != "" and password1==password2:
            u = user(usuario, password1)
            u.saveToFile()
            usuarios.append(u)  
            return render_template("registro.html", title = "Registro", verificacion = verificacion) 
        else:
            return render_template("registro.html", title = "Registro") 





     
@app.route('/menu', methods = ['POST'] )
def menu():
    return render_template('main.html', title = 'Menu principal')

def verificarRegistro(usuario, password1,password2):
    nombreArchivo = "bd/users.csv"
    directorio = os.path.dirname(__file__)
    archivo = nombreArchivo 
    ruta = os.path.join(directorio, archivo)

    f = open(ruta, "r")
    lineas = f.readlines()
    f.close()
    datos = []
    for l in lineas:
        l = l.replace("\n","")
        l = l.split(";")
        datos.append(l)  
        if (usuario in l):
            return "existe"
            ########################################
        elif password1 != password2:
            return "repetidos"
            ##########################################
    return "no existe"

def verificar(usuario, password, nombreArchivo):
    
    directorio = os.path.dirname(__file__)
    archivo = nombreArchivo 
    ruta = os.path.join(directorio, archivo)

    f = open(ruta, "r")
    lineas = f.readlines()
    f.close()
    datos = []
    for l in lineas:
        l = l.replace("\n","")
        l = l.split(";")
        datos.append(l)  
        if (usuario in l) and (password in l):
            return "existe"
    if len(usuario) == 0 or len(password) == 0:
        return 'vacio'
    return "no existe"           

def loadFromFile():
    try:
        usuarios = []
        fileUsuarios  = os.path.join(os.path.dirname(__file__), "bd/users.csv")
        f = open(fileUsuarios, "r")
        datos = f.readlines()
        f.close()
        for d in datos:
            d = d.replace("\n", "")
            datos = d.split(";")
            usuario = datos[0]
            password = datos[1]
        
            u = user(usuario, password) 
            usuarios.append(u)
            
    except:
        fileUsuarios  = os.path.join(os.path.dirname(__file__), "bd/users.csv")
        f = open(fileUsuarios, "a")
        f.close()
        
    return usuarios        

if __name__ == "__main__":
    usuarios = loadFromFile()
    app.run(debug = True)
    
