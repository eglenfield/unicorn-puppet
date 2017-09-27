$(document).ready(function() {

    var text = ["Gathering data from Puppet runs", "Parsing data", "Extracting resources"];
    var counter = 0;
    var textElem = document.getElementById("welcomeText");
    $(".begin-button").on('click', function(){
        $(this).remove();
        $(".begin-header").remove();
        $("#loader").css("display", "block");
        setInterval(changeText, 3000);
    })

    function changeText() {
        textElem.innerHTML = text[counter];
        counter++;
        if (counter - 1 >= text.length) {
            $('#welcomeText').remove();
            $('#loader').remove();
            $('.continue-header').css("display", "block");
            $('.continue-div').css("display", "block");
        }
    }
});