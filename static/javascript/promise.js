
function requestGetPromises(handler) {
    $.ajax({
        type: 'GET',
        url: `/api/promises`,
        data: {},
        success: handler
    })
}
function requestPostPromises(data, handler) {
    const {name, content, promise_style} = data
    $.ajax({
        type: 'POST',
        url: `/api/promises`,
        data: {name: name, content: content, promise_style: promise_style},
        success: handler
    });
}
function requestPutPromises(data, handler) {
    const {id, content} = data
    $.ajax({
        type: 'PUT',
        url: `/api/promises`,
        data: {id: id, content: content},
        success: handler
    });
}


function requestDeletePromises(id, handler) {
    $.ajax({
        type: 'DELETE',
        url: `/api/promises`,
        data: {id: id},
        success: handler
    });
}



