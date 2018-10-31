$("#Index").on("submit", "#hero form", function(event){
	event.preventDefault();
	var ex = $(this).find("input[name='ex']").val();
	$.getScript('/static/assets/js/ajax_calls.js', function(){
		searchCall(ex);
	});
});

$("#tabs").on("click", "a#completeSpotListLink", function(event){
  event.preventDefault();
  $.getScript('/static/assets/js/ajax_calls.js', function(){
    completeSpotListCall();
  });
});

$("#haveFeedbackBtn").on("click", ".row button", function(event){
  event.preventDefault();
  $("#haveFeedbackBtn .alert").hide();
  $("#haveFeedbackBtn").toggleClass("active");
  $("#haveFeedbackBtn form").toggleClass("active");
});

$("#haveFeedbackBtn").on("submit", "form", function(event){
  event.preventDefault();
  $.ajax({
    url: '/feedback/send-message/',
    type: 'POST',
    data: {
      csrfmiddlewaretoken: $("#haveFeedbackBtn input[name='csrfmiddlewaretoken']").val(),
      name: $("#haveFeedbackBtn #id_name").val(),
      email: $("#haveFeedbackBtn #id_email").val(),
      message: $("#haveFeedbackBtn #id_message").val()
    },
    success: function(response) {
      console.log(response);
      // $("#haveFeedbackBtn").toggleClass("active");
      $("#haveFeedbackBtn .alert").hide();
      $("#haveFeedbackBtn .alert-success").show();
    },
    error: function(err) {
      console.log(err);
      $("#haveFeedbackBtn .alert").hide();
      $("#haveFeedbackBtn .alert-danger").show();
    }
  });
});

$(document)
  .ajaxStart(function () {
    $("div.loader").append("<i class='fas fa-spinner fa-spin fa-3x spinnerLoader'></i>");
  })
  .ajaxStop(function () {
    $(".spinnerLoader").remove();
  });