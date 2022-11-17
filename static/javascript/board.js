/**
 *
 * 서버에 방명록 목록을 요청하는 Ajax 함수
 *
 * @param {number} memberId (1-5) 멤버 아이디
 * @param {callback} handler Ajex 성공시에 실행되는 콜백. (response) => void
 */
function requestGetBoards(memberId, handler) {
    $.ajax({
        type: 'GET',
        url: `/api/boards/${memberId}`,
        data: {},
        success: handler
    })
}

/**
 *
 * 서버에 방명록 작성을 요청하는 Ajax 함수
 *
 * @param {number} memberId (1-5) 멤버 아이디
 * @param {object} data
 * @param {callback} handler Ajex 성공시에 실행되는 콜백. (response) => void
 */
function requestPostBoards(memberId, data, handler) {
    const {name, message} = data
    $.ajax({
        type: 'POST',
        url: `/api/boards/${memberId}`,
        data: {name_give: name, message_give: message},
        success: handler
    });
}

