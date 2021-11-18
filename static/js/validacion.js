function botonIngresar(){
    usuario = document.getElementById("exampleInputEmail1").value;
    password = document.getElementById("exampleInputPassword1").value;
    if ((usuario == "") || (password == "")){
       alert("Complete todos los campos");
    }
    else{
      document.getElementById("formLogin").submit();
    }
  }

function registro(){
  usuario = document.getElementById("exampleInputEmail2").value;
  password = document.getElementById("exampleInputPassword2").value;
  if ((usuario == "") || (password == "")){
     alert("Complete todos los campos");
  }
  else{
    document.getElementById("formRegistro").submit();
  }
}