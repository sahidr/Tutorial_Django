$('#id_button').click(function(){
    console.log('entré');
    $.ajax({
        type:'GET',
        url: this.href,
        success: function () {
            $('#id_button').html("Hellow World!");
        }
    });

});