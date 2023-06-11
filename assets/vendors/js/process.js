$(document).ready(function(){
    $("#bode").hide();
    $("#bode2").hide();
    $("#bode3").hide();
    $("#esconde").show();
  
    $('#mostra').click(function(){
        $("#bode").slideToggle("slow");
        $("#bode2").slideUp("slow");
        $("#bode3").slideUp("slow");
    });
    
    $('#mostra2').click(function(){
        $("#bode").slideUp("slow");
        $("#bode2").slideToggle("slow");
        $("#bode3").slideUp("slow");
    });

    $('#mostra3').click(function(){
        $("#bode").slideUp("slow");
        $("#bode2").slideUp("slow");
        $("#bode3").slideToggle("slow");
    });
});

function loadAnim(){
    $("#form_generator").hide();
    setTimeout(function(){ $("#form_header").fadeIn("slow"); }, 500);
    setTimeout(function(){ $("#form_checker").fadeIn("slow"); }, 1000);
    setTimeout(function(){ $("#form_response").fadeIn("slow"); }, 1500);
}

function checker_clk(){
    $("#form_checker").slideToggle("slow");
    $("#form_generator").slideUp("slow");
}
function generator_clk(){
    $("#form_checker").slideUp("slow");
    $("#form_generator").slideToggle("slow");
}

    function enviar() {
        var linha = $("#lista").val();
        var sk = document.getElementById("sk").value;
        var linhaenviar = linha.split("\n");
        var total = linhaenviar.length;
        var lv = 0;
        var cn = 0;
        var dd = 0;
        linhaenviar.forEach(function(value, index) {
            setTimeout(
                function() {
                    $.ajax({
                        url: 'api.php?lista=' + value + '&sk=' + sk,
                        type: 'GET',
                        async: true,
                        success: function(resultado) {
                            if (resultado.match("#CVV")) {
                                removelinha();
                                lv++;
                                live(resultado + "");
                            }else if(resultado.match("#CCN")){
                            	removelinha();
                            cn++;
                                live2(resultado + "");
                             }else {
                                removelinha();
                                dd++;
                                dead(resultado + "");
                            }
                            $('#carregadas').html(total);
                            var fila = parseInt(lv) + parseInt(cn) + parseInt(dd);
                            $('#cLive').html(lv);
                            $('#cWarn').html(cn);
                            $('#cDie').html(dd);
                            $('#total').html(fila);
                            $('#cLive2').html(lv);
                            $('#cWarn2').html(cn);
                            $('#cDie2').html(dd);
                        }
                    });
                }, 2500 * index);
        });
    }
    function live(str) {
        $(".live").append(str + "<br>");
    }
    function dead(str) {
        $(".dead").append(str + "<br>");
    }
    function live2(str) {
        $(".live2").append(str + "<br>");
    }
    function removelinha() {
        var lines = $("#lista").val().split('\n');
        lines.splice(0, 1);
        $("#lista").val(lines.join("\n"));
    }
