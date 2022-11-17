function create() {
        const name = $("#nameInput").val();
        const message = $("#commentInput").val();

        const memberId = 1
        const data = {
            name: name || 'GUEST',
            message: message || 'WOW!'
        }

        requestPostBoards(memberId, data, (response) => {
            alert(response['msg'])
            // window.location.reload()
        })
    }

