function actRPM(){
    var tipoMaquina=document.getElementById('tipo_maquina');
    var selectedOption = tipoMaquina.options[tipoMaquina.selectedIndex];
    var rpm = selectedOption.getAttribute('data-rpm');
    var ppp=selectedOption.getAttribute('data-ppp');
    document.getElementById('rpm').value = rpm;
    document.getElementById('ppp').value = ppp;
    
}
function actcodOp(){
    var codigo=document.getElementById("operacion")
    var seleccion=codigo.options[codigo.selectedIndex]
    var cod=seleccion.getAttribute('data-cod')
    codigo_op.value=cod
}