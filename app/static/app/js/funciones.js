function actRPM(){
    var tipoMaquina=document.getElementById('tipo_maquina');
    var selectedOption = tipoMaquina.options[tipoMaquina.selectedIndex];
    var rpm = selectedOption.getAttribute('data-rpm');
    var ppp=selectedOption.getAttribute('data-ppp');
    document.getElementById('rpm').value = rpm;
    HSF(); // Llamar a la función HSF aquí para actualizar el campo fhsf
    MTS()
    console.log(rpm)
    
    
}
function actcodOp(){
    var codigo=document.getElementById("operacion")
    var seleccion=codigo.options[codigo.selectedIndex]
    var cod=seleccion.getAttribute('data-cod')
    codigo_op.value=cod
}
function MTS(){
    var ppp = parseInt(document.getElementById('ppp').value)||0
    var rpm = parseInt(document.getElementById('rpm').value)||0
    var consta = parseFloat(document.getElementById('consta').value)||1

    var div=rpm*consta
   
   var multi=ppp/div
   document.getElementById('resulmt').value = multi.toFixed(2);
}
function HSF() {
    var v1 = parseInt(selectedOption.getAttribute('data-rpm'))
    var v2 = 1000;
    var v3 = v1 / v2;
    document.getElementById('fhsf').value = v3.toFixed(2); // Asegúrate de usar toFixed si quieres redondear el resultado
    console.log(v1)
    console.log(v3)
}

// Asegúrate de que esta función esté definida y se llame cuando cambie el tipo de máquina
document.getElementById('tipo_maquina').addEventListener('change', actRPM);