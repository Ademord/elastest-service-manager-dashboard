// Catalog/Show | Launch (PreviewModal)
$('#launch_preview').on('click', function() {
    // $("#modal-background").toggleClass("active", 1000);
    $("div[role=tooltip]").remove();
    // adjust form
    var $selected_service = $('#launch_preview').children()[1].innerHTML;
    var $selected_plan = $('#launch_preview').children()[2].innerHTML;
    var $new_action = "/instances/create/" + $selected_service + "k" + $selected_plan;
    $('#launch_instance').attr('action', $new_action);
    // show the modal
    $('#launch_modal_preview').modal({backdrop: 'static', keyboard: false});

});
// Catalog | Add Service
$('#add_service_button').on('click', function() {
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

window.onload=function(){
  $slideshow = $('.slider').slick({
    dots:true,
  autoplay:true,
  arrows:true,
  prevArrow:'<button type="button" class="slick-prev"></button>',
  nextArrow:'<button type="button" class="slick-next"></button>',
  slidesToShow:1,
  slidesToScroll:1
  });
  $('.slide').click(function() {
    $slideshow.slick('slickNext');
  });
};


function addFields(){
    var number = document.getElementById("num_variables").value;
    var container = document.getElementById("container_variables");
    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }
    for (i=0;i<number;i++){
        var form_control = document.createElement("div");
        form_control.setAttribute("class", "form-group");

        var id_name = "service_variable_" + (i+1);
        // var label = document.createElement("Label");
        // label.setAttribute("for", id_name);
        // label.setAttribute("class", "bmd-label-floating");
        // label.innerHTML = "key: value";
        // form_control.appendChild(label);

        var input = document.createElement("input");
        input.type = "text";
        input.id = id_name;
        input.name = id_name;
        input.setAttribute("class", "form-control");
        input.setAttribute("placeholder", "Key: Value");
        input.setAttribute('required', true);
        form_control.appendChild(input);

        var icon = '<div class="input-group-prepend">' +
            '<span class="input-group-text"><i class="material-icons">toc</i></span></div>';
        container.insertAdjacentHTML( 'beforeend', icon );
        container.appendChild(form_control);
        // container.appendChild(document.createElement("br"));
    }
}