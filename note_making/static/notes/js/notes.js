$(document).ready(function(){
    $('.notes-container .item ul').hide()
    $('.notes-container .item h3').click(function(){
        $(this).next('ul').toggle()
    })
})