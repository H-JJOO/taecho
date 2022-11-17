// 방명록 관련 Ajax 함수를 모아놓은 장소
// 이 js 파일을 개인 페이지에서 불러오고 requestGetBoards 함수를 써주시면 됩니다.
// 아마 방명록 작성에 개인 작성 함수(ex. create)를 script에 작성하여 그 안에 이 함수를 호출해주면 됩니다.

/**
 * 예시코드
 *
 * function create() {
 *      const name = $("이름 입력칸의 selector").val();
 *      const message = $("내용 입력칸의 selector").val();
 *
 *      const memberId = 3  <== 박진의 Id
 *      const data = {
 *          name: name,
 *          message: message
 *      }
 *
 *      requestPostBoards(memberId, data, (response) => {
 *          alert(response['msg'])
 *          원하면 window.location.reload()
 *      })
 *
 * }
 */

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
        data: {name: name, message: message},
        success: handler
    });
}

/**
 *
 * 서버에 방명록 수정을 요청하는 Ajax 함수
 *
 * @param {number} memberId (1-5) 멤버 아이디
 * @param {object} data { id: (받아왔던 것의 _id), message: 수정할 것}
 * @param {callback} handler Ajex 성공시에 실행되는 콜백. (response) => void
 */
function requestPutBoards(memberId, data, handler) {
    const {id, message} = data
    $.ajax({
        type: 'PUT',
        url: `/api/boards/${memberId}`,
        data: {id: id, message: message},
        success: handler
    });
}


/**
 *
 * 서버에 방명록 수정을 요청하는 Ajax 함수
 *
 * @param {number} memberId (1-5) 멤버 아이디
 * @param {string} id { 받아온 것의 _id}
 * @param {callback} handler Ajex 성공시에 실행되는 콜백. (response) => void
 */
function requestDeleteBoards(memberId, id, handler) {
    $.ajax({
        type: 'DELETE',
        url: `/api/boards/${memberId}`,
        data: {id: id},
        success: handler
    });
}



