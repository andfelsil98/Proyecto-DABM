# coding= UTF-8
from flask import Flask, render_template, request
import os

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
        if resultado == True:
            return render_template("main.html", title = "Inicio")   
        else: 
            return render_template("login.html", title = "Login", resultado = resultado)    

@app.route('/registro', methods = ["GET","POST"])  
def registro():
    nombreArchivo = "bd/userAdmin.csv"
    if request.method == "POST":
        usuarioAdmin = request.form["usuarioAdmin"]
        passwordAdmin = request.form["passwordAdmin"]
        verificacion = verificar(usuarioAdmin, passwordAdmin, nombreArchivo)
        if verificacion == True:
            return render_template("registro.html", title = "Registro")     
        else:
            return render_template("login.html", title = "Login", verificacion = verificacion)
            # return 'falso'

@app.route('/menu', methods = ['POST'] )
def menu():
    return render_template('main.html', title = 'Menu principal')

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
            return True
    if len(usuario) == 0 or len(password) == 0:
        return 'vacio'
    return False                  

if __name__ == "__main__":
    app.run(debug = True)
