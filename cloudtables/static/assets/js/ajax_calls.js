function contactCall() {
	$.ajax({
		url: '/contacto/',
		type: 'POST',
		data: {
			csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
			nombre: $("#contact form input[name='nombre']").val(),
			email: $("#contact form input[name='email']").val(),
			mensaje: $("#contact form textarea[name='mensaje']").val(),
		},

		beforeSend : function() {
			$("#contact .box").prepend("<h3 class='gracias'>Gracias!</h3>");
			$("#contact form input, #contact form textarea").val("");
		},

		success: function(response) {
			console.log(response);
			setTimeout(function(){$("#contact .box h3.gracias").remove();}, 5000);
		},

		error : function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});
}

function cancelarPedido(pedido) {
	$.ajax({
		url: '/exchange/borrar/',
		type: 'GET',
		data: {
			pedido: pedido,
		},

		success: function(response) {
			console.log(response);
			$("#perfil_dashboard").html(response)
		},

		error : function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});
}

function searchCall(ex) {
	$.ajax({
		url: '/search/',
		type: 'GET',
		data: {
			ex: ex
		},

		success: function(response) {
			console.log(this.url);
			page = this.url;
			console.log(page);
            ga('set', 'page', page);
            ga('send', 'pageview');
			$('<style type="text/css"></style>')
    		.html(response['css'])
    		.appendTo("head");
			$("#searchResultsParent").html(response['html']);
			if(window.history.pushState && response['ex'] !== ' '){
				window.history.pushState({}, null, '/?ex=' + response['ex']);
			}
			$('html, body').stop().animate({
            'scrollTop': $("#searchResultsParent").offset().top
            }, 800, 'swing');
		},

		error: function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});
}

function completeSpotListCall() {
	$.ajax({
		url: '/api/complete-spot-list/',
		type: 'GET',
		data: {},

		success: function(response) {
			console.log(this.url);
			page = this.url;
			console.log(page);
            ga('set', 'page', page);
            ga('send', 'pageview');
			$('<style type="text/css"></style>')
    		.html(response['css'])
    		.appendTo("head");
			$("#searchResultsParent").html(response['html']);
			if(window.history.pushState && response['ex'] !== ' '){
				window.history.pushState({}, null, '/' + response['ex'] + '/');
			}
			$('html, body').stop().animate({
            'scrollTop': $("#searchResultsParent").offset().top
            }, 800, 'swing');
		},

		error: function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});
}
