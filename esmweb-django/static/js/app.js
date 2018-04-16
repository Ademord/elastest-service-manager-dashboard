// Catalog/Show | Launch (PreviewModal)
$('#launch_preview').on('click', function() {
    // $("#modal-background").toggleClass("active", 1000);
    $("div[role=tooltip]").remove();
    // adjust form
    var $selected_plan = $('#launch_preview').children()[1].innerHTML;
    var $new_action = "/instances/create/" + $selected_plan;
    $('#launch_instance').attr('action', $new_action);
    // show the modal
    $('#launch_modal_preview').modal({backdrop: 'static', keyboard: false});

});
// Catalog | Add Service
$('#addService').on('click', function() {
    // $("#modal-background").toggleClass("active", 1000);
    $('#modal_create_service').modal({backdrop: 'static', keyboard: false});
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

// Catalog/Show | Launch
$('#launch').on('click', function() {
    $("div[role=tooltip]").remove();

    var $new = $('#launch_modal_success');
    $('#launch_modal_preview').modal('hide');

    $new.prop('class', 'modal fade') // revert to default
        .addClass($(this).data('direction'));
    setTimeout(function() {
        $new.modal('show');
    }, 1500);


    // setTimeout(function() {
    //     $new.modal('hide');
    // }, 4000);
});

// Catalog/Show | Edit (Test)
$('#edit').on('click', function() {
    $("div[role=tooltip]").remove();
    var $new = $('#launch_modal_success');

    $new.prop('class', 'modal fade') // revert to default
        .addClass($(this).data('direction'));
    $new.modal('show');

    // setTimeout(function() {
    //     $new.modal('hide');
    // }, 4000);
});

$('#delete_instance_button').click(function(){
    var $new = $('#launch_modal_success');

    $new.prop('class', 'modal fade') // revert to default
        .addClass($(this).data('direction'));
    $new.modal('show');
    $('#delete_instance').submit();
});

