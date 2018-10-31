$("body").on("click", ".deleteItem", event => {
    event.preventDefault();
    if(confirm('seguro?')){
        let item = $(event.currentTarget).attr('data-item-id')
        $.ajax({
            url: '/places/delete-item/' + item + '/',
            type: 'GET',
            data: {},
            success: response => {
                console.log(response);
                response == 'OK' ?
                    $("#item-" + item).remove() : console.log(response);
            },
            error: err => console.log(err)
        });
    }
});