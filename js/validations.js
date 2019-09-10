$('#btnEnviar').click(function () {


    nombre = $('#nombretxt').val();
    email = $('#emailtxt').val();
    region = $('#regiontxt').val();
    comuna = $('#comunatxt').val();
    telefono = $('#fonotxt').val();

    $('<div>').text(nombre).appendTo("#nombretxt");

    $('<div>').text(email).appendTo("#emailtxt");

    $('<div>').text(region).appendTo("#regiontxt");

    $('<div>').text(comuna).appendTo("#comunatxt");

    $('<div>').text(telefono).appendTo("#fonotxt");


    console.log(nombre, email, region, comuna, telefono)
});


//según los codigos ascii solo acepta números

function validaNumericos(event) {
    if (event.charCode >= 48 && event.charCode <= 57) {
        return true;
    }
    return false;
}

function soloLetras(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toLowerCase();
    letras = " áéíóúabcdefghijklmnñopqrstuvwxyz";
    especiales = "8-37-39-46";

    tecla_especial = false
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        return false;
    }

}

function validarEmail(elemento){

    var texto = document.getElementById(elemento.id).value;
    var regex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;

    if (!regex.test(texto)) {
        document.getElementById("resultado").innerHTML = "Correo invalido";
        document.getElementById("emailtxt").style.borderColor="red";
    } else {
        document.getElementById("resultado").innerHTML = "";
        document.getElementById("emailtxt").style.borderColor="";
    }

}