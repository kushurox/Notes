$(document).ready(function(){
    $('.delform').hide()
    $('#real_edit_note').hide()
    $('#fake').click(function(){
        $('.delform').show()
        $(this).hide()
    })
    $('#content').css('height', $("#content").prop('scrollHeight') + 'px')

    $('#fake_edit_note').click(function(){
        $(this).hide()
        $('#content').removeAttr('disabled')
        $('#real_edit_note').show()
    })
})