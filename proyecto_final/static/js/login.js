
function validar_iniciar_sesion_cliente(){
var password = document.getElementById('password').value;
var email = document.getElementById('email').value;
  $("bt_login").on('click', function(){

      if(email.value === ''){

          evt.preventDefault();
          return false;

      }else if(password.value === ''){

          evt.preventDefault();
          return false;

        }else if(email.length>50){
            alert("El email debe tener menos de 51 carácteres.");
            document.getElementById("email").value = "";
            document.getElementById("email").focus();
            return false;
    } else if(password.length<8){
        alert("La contraseña debe tener al menos 8 carácteres.");
        document.getElementById("password").focus();
        return false;

    }else if(email === emailU && password === passwordU){
        window.location.href("../pages/home.html")
        return true;
        
  }else{
    
    document.getElementById("email").value = "";
    document.getElementById("password").value = "";
    document.getElementById("email").focus();
    return false;
  }
  
  
});}