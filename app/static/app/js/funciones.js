function actRPM(){
    var tipoMaquina=document.getElementById('tipo_maquina');
    var selectedOption = tipoMaquina.options[tipoMaquina.selectedIndex];
    var rpm = selectedOption.getAttribute('data-rpm');
    var ppp=selectedOption.getAttribute('data-ppp');
    document.getElementById('rpm').value = rpm;
    
    
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
    console.log(consta)
   var multi=ppp/div
   document.getElementById('resulmt').value = multi;
}