$('#launchPlan').on('click', function() {
    // $("#modal-background").toggleClass("active", 1000);
    $('#createManifestModal').modal({backdrop: 'static', keyboard: false});
    $("div[role=tooltip]").remove();

});

$('#addService').on('click', function() {
    // $("#modal-background").toggleClass("active", 1000);
    $('#createServiceModal').modal({backdrop: 'static', keyboard: false});


    $("div[role=tooltip]").remove();

});

$(".dropdown-menu a").click(function(){
    $(this).parents(".dropdown").find('.btn').html($(this).text() );
    $(this).parents(".dropdown").find('.btn').val($(this).data('value'));

});

$(document).on('change', '.selectpicker', function() {
  var target = $(this).data('target');
  var show = $("option:selected", this).data('show');
  $(target).children().addClass('hide');
  $(show).removeClass('hide');
});
$(document).ready(function(){
	$('.div-toggle').trigger('change');
});