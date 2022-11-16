function open_book() {
    $('#book-box').show()
}

function close_book() {
    $('#book-box').hide()
}

function write_book() {

    let name = $('#floatingInput').val()
    let message = $('#floatingTextarea2').val()

    if (name === '') {
        alert('이름을 써주세요!')
    }
    if (message === '') {
        alert('메세지를 남겨주세요!')
    } else $.ajax({
        type: 'POST',
        url: '/name',
        data: {name_give: name, message_give: message},
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    });

}