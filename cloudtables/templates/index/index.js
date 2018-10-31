$("body").on("submit", "form", event => {
    event.preventDefault();
    let table = $(event.currentTarget).attr('data-table-id');
    let item = $(event.currentTarget).find("select[name='item']").val();
    let quantity = $(event.currentTarget).find("input[name='quantity']").val();
    let place = $(event.currentTarget).attr('data-place-id');
    console.log(table, item, quantity, place);
    $.ajax({
        url: '/places/add-order-item/',
        type: 'GET',
        data: {
            table: table,
            item: item,
            quantity: quantity,
            place: place
        },
        success: response => {
            console.log(response);
            $("div.table-check[data-table-id='" + table + "']").html(response.table_check);
            $("div#totals").html(response.totals);
        },
        error: err => console.log(err)
    });
});

$("body").on("click", "table button.btn-success", event => {
    event.preventDefault();
    let order = $(event.currentTarget).attr('data-order-id')
    let table = $(event.currentTarget).attr('data-table-id')
    $.ajax({
        url: '/places/pay-order-item/',
        type: 'GET',
        data: {
            order
        },
        success: response => {
            console.log(response);
            $("div.table-check[data-table-id='" + table + "']").html(response.table_check);
            $("div#totals").html(response.totals);
        },
        error: err => console.log(err)
    });
});

$("body").on("click", "table button.btn-danger", event => {
    event.preventDefault();
    if(confirm('seguro?')){
        let order = $(event.currentTarget).attr('data-order-id')
        let table = $(event.currentTarget).attr('data-table-id')
        $.ajax({
            url: '/places/delete-order-item/',
            type: 'GET',
            data: {
                order,
                table
            },
            success: response => {
                console.log(response);
                $("div.table-check[data-table-id='" + table + "']").html(response.table_check);
                $("div#totals").html(response.totals);
            },
            error: err => console.log(err)
        });
    }
});

$("body").on("click", "div.subtotals button.btn-success", event => {
    event.preventDefault();
    let table = $(event.currentTarget).attr('data-table-id')
    $.ajax({
        url: '/places/pay-full-order/',
        type: 'GET',
        data: {
            table
        },
        success: response => {
            console.log(response);
            $("div.table-check[data-table-id='" + table + "']").html(response.table_check);
            $("div#totals").html(response.totals);
        },
        error: err => console.log(err)
    });
});

$("body").on("click", "div.subtotals button.btn-danger", event => {
    event.preventDefault();
    if(confirm('seguro?')){
        let table = $(event.currentTarget).attr('data-table-id')
        $.ajax({
            url: '/places/delete-full-order/',
            type: 'GET',
            data: {
                table
            },
            success: response => {
                console.log(response);
                $("div.table-check[data-table-id='" + table + "']").html(response.table_check);
                $("div#totals").html(response.totals);
            },
            error: err => console.log(err)
        });
    }
});

$("body").on("click", ".deleteTable", event => {
    event.preventDefault();
    if(confirm('seguro?')){
        let table = $(event.currentTarget).attr('data-table-id')
        $.ajax({
            url: '/places/delete-table/' + table + '/',
            type: 'GET',
            data: {},
            success: response => {
                console.log(response);
                response == 'OK' ?
                    $("#table-" + table).remove() : console.log(response);
            },
            error: err => console.log(err)
        });
    }
});