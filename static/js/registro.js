function botonRegistro1(){
    usuario = document.getElementById("usuarioRegistro").value;
    password1 = document.getElementById("passwordRegistro1").value;
    password2 = document.getElementById("passwordRegistro2").value;
    if(((usuario == "") || (password1 == "")) || (password2 == "")){
        alert("Complete todos los campos");
    }

    else if ((password1 == password2)){
        document.getElementById("formRegistro1").submit();
    }
}    
  