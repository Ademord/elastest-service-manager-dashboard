$('#add_service_button').on('click', function() {
    showCreateModal();
});

$('#launch_preview').on('click', function() {
    showLaunchModal();
});

$('#launch').on('click', function() {
    showAfterLaunchModal();
});

// Catalog/Show | Edit (Test)
$('#edit').on('click', function() {
    showAfterLaunchModal()
});

$('#delete_instance_button').click(function(){
    showAfterDeleteModal();
});

// Change Dropdown Value on Select
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


// function for the create service form
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

function showAfterDeleteModal() {
    var $new = $('#launch_modal_success');

    $new.prop('class', 'modal fade') // revert to default
        .addClass($(this).data('direction'));
    $new.modal('show');
    $('#delete_instance').submit();
}

function showAfterLaunchModal() {
    $("div[role=tooltip]").remove();
    // code improved for showNotifyModal
}

function showLaunchModal() {
    // $("#modal-background").toggleClass("active", 1000);
    $("div[role=tooltip]").remove();
    // adjust form
    var $selected_service = $('#launch_preview').children()[1].innerHTML;
    var $selected_plan = $('#launch_preview').children()[2].innerHTML;
    var $new_action = "/instances/create/" + $selected_service + "k" + $selected_plan;
    $('#launch_instance').attr('action', $new_action);
    // show the modal
    $('#launch_modal_preview').modal({backdrop: 'static', keyboard: false});
}

function showCreateModal() {
    // $("#modal-background").toggleClass("active", 1000);
    $('#modal_create_service').modal({backdrop: 'static', keyboard: false});
    $("div[role=tooltip]").remove();
}

function showNotifyModal(title, message, fa_icon, fa_color) {
    var container = document.getElementById("main_container_fluid");

    var message_modal =
        '<div id="notify_modal" class="modal fade">' +
            '<div class="modal-dialog" >         ' +
                '<div class="modal-content" style="background:transparent; box-shadow:none; border:none;">' +
                    '<div class="modalbox '+ fa_color +' col-sm-10 col-md-10 col-lg-10 center animate">' +
                    '<div class="icon"><span class="fa '+ fa_icon +'" style="padding-top: 20px;"></span>  </div>' +
                    '<h1>'+ title +'</h1> <p>'+ message +' </p>' +
                    '<button type="button" class="redo btn" style="border: solid 1px;" data-dismiss="modal">Try again</button>' +
        '</div> </div> </div> </div>';

    container.insertAdjacentHTML( 'beforeend', message_modal );

    var $new = $('#notify_modal');

    $new.prop('class', 'modal fade') // revert to default
        .addClass($(this).data('direction'));
    setTimeout(function() {
        $new.modal('show');
    }, 1000);

    // setTimeout(function() {
    //     $new.modal('hide');
    // }, 3000);
}