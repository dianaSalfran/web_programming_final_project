 $(document).ready(() => {
    $('.alert').hide();
    $('#formLog').submit((event) => {
        let correo = $('#email').val().trim;
        let contraseña = $('#password').val();

        if (correo.length) {
            $('.alert').show();
            return;
        }else if (contraseña.length) {
            $('.alert').show();
            return;            
        }
    })
 });