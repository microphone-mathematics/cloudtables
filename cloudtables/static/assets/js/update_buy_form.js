$("body").on("keyup", "input[name='amount']", function(event){
	var transaction = $(this).siblings("select[name='transaction']").val();
	if (transaction !== "") {
		if (transaction === "1"){
			var currency = $(this).siblings("select[name='currency']").val();
			var currency_val_span = "span#"+currency+"_sell_price";
			var currency_val = $(currency_val_span).text()
			var amount = $(this).val();
			var price = amount * currency_val;
			$(this).siblings("input[name='price']").val(price);
		}		
		else if (transaction === "2"){
			var currency = $(this).siblings("select[name='currency']").val();
			var currency_val_span = "span#"+currency+"_buy_price";
			var currency_val = $(currency_val_span).text()
			var amount = $(this).val();
			var price = amount * currency_val;
			$(this).siblings("input[name='price']").val(price);
		}
		
	}
	else {
		$(this).siblings("input[name='price']").attr("placeholder", "Compra o Venta?")
	}
});

$("body").on("keyup", "input[name='price']", function(event){
	var transaction = $(this).siblings("select[name='transaction']").val();
	if (transaction !== "") {
		if (transaction === "1"){
			var currency = $(this).siblings("select[name='currency']").val();
			var currency_val_span = "span#"+currency+"_sell_price";
			var currency_val = $(currency_val_span).text()
			var price = $(this).val();
			var amount = price / currency_val;
			$(this).siblings("input[name='amount']").val(amount);
		}
		else if (transaction === "2"){
			var currency = $(this).siblings("select[name='currency']").val();
			var currency_val_span = "span#"+currency+"_buy_price";
			var currency_val = $(currency_val_span).text()
			var price = $(this).val();
			var amount = price / currency_val;
			$(this).siblings("input[name='amount']").val(amount);
		}
	}
	else {
		$(this).siblings("input[name='amount']").attr("placeholder", "Compra o Venta?");
	}
});

$("body").on("change", "select[name='currency']", function(event){
	$(this).siblings("input[name='amount'], input[name='price']").val("");
	$(this).siblings("input[name='amount']").attr("placeholder", "Cantidad");
	$(this).siblings("input[name='price']").attr("placeholder", "Precio ( USD )");
});

$("body").on("change", "select[name='transaction']", function(event){
	var price = $(this).siblings("input[name='price']").val();
	var amount = $(this).siblings("input[name='amount']").val();
	var currency = $(this).siblings("select[name='currency']").val();
	var transaction = $(this).val();
	if (amount !== "" && price !== ""){
		$(this).siblings("input[name='amount'], input[name='price']").val("");
		$(this).siblings("input[name='amount']").attr("placeholder", "Cantidad");
		$(this).siblings("input[name='price']").attr("placeholder", "Precio ( USD )");
	}
	else if (amount !== "" && price === "" && currency !== "") {
		switch (transaction) {
			case "1": {
				var currency_val_span = "span#"+currency+"_sell_price";
				var currency_val = $(currency_val_span).text()
				var price = amount * currency_val;
				$(this).siblings("input[name='price']").val(price);
				break;
			}
			case "2": {
				var currency_val_span = "span#"+currency+"_buy_price";
				var currency_val = $(currency_val_span).text()
				var price = amount * currency_val;
				$(this).siblings("input[name='price']").val(price);
				break;
			}
		}
	}
	else if (amount !== "" && price === "" && currency === "") {
		switch (transaction) {
			case "1": {
				$(this).siblings("input[name='price']").attr("placeholder", "Moneda?");
				break;
			}
			case "2": {
				$(this).siblings("input[name='price']").attr("placeholder", "Moneda?");
				break;
			}
		}
	}
	else if (amount === "" && price !== "" && currency !== "") {
		switch (transaction) {
			case "1": {
				var currency_val_span = "span#"+currency+"_sell_price";
				var currency_val = $(currency_val_span).text()
				var amount = price / currency_val;
				$(this).siblings("input[name='amount']").val(amount);
				break;
			}
			case "2": {
				var currency_val_span = "span#"+currency+"_buy_price";
				var currency_val = $(currency_val_span).text()
				var amount = price / currency_val;
				$(this).siblings("input[name='amount']").val(amount);
				break;
			}
		}
	}
	else if (amount === "" && price !== "" && currency === "") {
		switch (transaction) {
			case "1": {
				$(this).siblings("input[name='amount']").attr("placeholder", "Moneda?");
				break;
			}
			case "2": {
				$(this).siblings("input[name='amount']").attr("placeholder", "Moneda?");
				break;
			}
		}
	}
	else if (amount === "" && price === "" && currency === "") {
		switch (transaction) {
			case "1": {
				$(this).siblings("input[name='amount']").attr("placeholder", "Moneda?");
				$(this).siblings("input[name='price']").attr("placeholder", "Moneda?");
				break;
			}
			case "2": {
				$(this).siblings("input[name='amount']").attr("placeholder", "Moneda?");
				$(this).siblings("input[name='price']").attr("placeholder", "Moneda?");
				break;
			}
		}
	}
});