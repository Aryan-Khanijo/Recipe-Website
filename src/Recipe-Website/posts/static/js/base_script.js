

$('document').ready(function(){
    $('a.notactive').mouseenter(function(){
        $(this).addClass('w3-theme');
    })
    $('a.notactive').mouseleave(function(){
        $(this).removeClass('w3-theme');
    })
    $("#dropNav").click(function (){
        var oper = $(this).html();
        if(oper==="menu"){
            $(this).html("close");
        }
        else{
            $(this).html("menu");
        }
        $("#navBar").toggleClass("dropdown")
    })
})