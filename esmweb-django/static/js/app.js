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
function addFields_variables(){
    var number = document.getElementById("num_variables").value;
    var container = document.getElementById("container_variables");
    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }
    for (i=0;i<number;i++){

        var subcontainer = document.createElement("div");
        subcontainer.setAttribute("class", "input-group form-control-lg");

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


        // var subcontainer = '<div class="input-group form-control-lg"></div>';
        var icon = '<div class="input-group-prepend">' +
            '<span class="input-group-text"><i class="material-icons">toc</i></span></div>';

        subcontainer.insertAdjacentHTML( 'beforeend', icon );
        subcontainer.appendChild(form_control);
        container.appendChild(subcontainer);
        // container.appendChild(document.createElement("br"));
    }
}

function removeDiv(btn){
    var index = id_array.indexOf(Number(btn.id));
    if (index > -1) {
      id_array.splice(index, 1);
    }
    (((btn.parentNode).parentNode).parentNode).removeChild((btn.parentNode).parentNode);
}
function textAreaAdjust(o) {
    // these dont work
    // o.height = "1px";
    // $(o).height = "1px";
    // $(o).css("height", "1px");
    o.rows = 6;
    var new_height = 25 + o.scrollHeight;
    o.rows = new_height/20;
}

function generate_plan_field(id){
    var id_name = "service_plan_" + id;
    var subcontainer = document.createElement("div");
    subcontainer.setAttribute("class", "input-group form-control-lg");
    var input_container = document.createElement("div");
    input_container.setAttribute("class", "form-group");
    input_container.setAttribute("style", "width:100%;");

    var input = document.createElement("textarea");
    input.id = id_name;
    input.name = id_name;
    input.setAttribute("rows", "24");
    input.setAttribute("onkeyup", "textAreaAdjust(this)");
    // input.keyup = function(){
    //         $(this).style.height = "1px";
    //         $(this).style.height = (25+o.scrollHeight)+"px";
    //     };
    input.setAttribute("style", "overflow:hidden");
    input.setAttribute("class", "form-control");
    input.setAttribute("placeholder", "Insert your Plan details here as JSON.");
    input.value = '' +
    '{  \n' +
    '    \t"name": "Test Plan 1.0",\n' +
    '    \t"bindable": false,\n' +
    '    \t"description": "This is my plan description",\n' +
    '    \t"free": true,\n' +
    '    \t"metadata": {  \n' +
    '        \t\t"bullets": "basic plan",\n' +
    '        \t\t"costs": {  \n' +
    '            \t\t\t"components": {},\n' +
    '            \t\t\t"description": "On Demand 5 per deployment, 50 per core, 10 per GB ram and 1 per GB disk",\n' +
    '            \t\t\t"fix_cost": {  \n' +
    '                \t\t\t\t"deployment": 5\n' +
    '            },\n' +
    '            \t\t\t"name": "On Demand 5 + Charges",\n' +
    '            \t\t\t"type": "ONDEMAND",\n' +
    '            \t\t\t"var_rate": {  \n' +
    '                \t\t\t\t"cpus": 50,\n' +
    '                \t\t\t\t"disk": 1,\n' +
    '                \t\t\t\t"memory": 10\n' +
    '            \t\t\t}\n' +
    '        \t\t}\n' +
    '    \t}\n' +
    '}';
    input.setAttribute('required', true);
    input_container.appendChild(input);

    // var subcontainer = '<div class="input-group form-control-lg"></div>';

    var icon = '<div class="input-group-prepend" style="align-items: center;">' +
        '<button class="y hC" style="\n' +
        '    color: white;\n' +
        '    width: 20px;\n' +
        '    height: 20px;\n' +
        '    margin-right: 10px;\n' +
        '    font-size: small;\n' +
        '    position: absolute;\n' +
        '    top: 0;\n' +
        '    right: 0;\n' +
        '    border-radius: 20%;\n" id="'+ id +'" onclick="removeDiv(this);">X</button>' +
        '</div>';
    subcontainer.insertAdjacentHTML( 'beforeend', icon );
    subcontainer.appendChild(input_container);
    return subcontainer;
}
var id_array = [];

function addFields_plans(){
    var container = document.getElementById("container_plans");

    var num_plans = document.getElementById("num_plans");
    num_plans.value = id = Number(num_plans.value) + 1;
    id_array.push(id);
    var subcontainer = generate_plan_field(id);

    container.appendChild(subcontainer);
    // container.appendChild(document.createElement("br"));
}

function submitService() {
    var num_plans = document.getElementById("num_plans");
    num_plans.value = id_array.join("#");
    $('#create_service').submit();
}
function showAfterDeleteModal() {
    var $new = $('#launch_modal_success');
    // todo fix this
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

function showNotifyModal(title, message, fa_icon, fa_color, button_message) {
    var container = document.getElementById("main_container_fluid");

    var message_modal =
        '<div id="notify_modal" class="modal fade">' +
            '<div class="modal-dialog" >         ' +
                '<div class="modal-content" style="background:transparent; box-shadow:none; border:none;">' +
                    '<div class="modalbox '+ fa_color +' col-sm-10 col-md-10 col-lg-10 center animate">' +
                    '<div class="icon"><span class="fa '+ fa_icon +'" style="padding-top: 20px;"></span>  </div>' +
                    '<h1>'+ title +'</h1> <p>'+ message +' </p>' +
                    '<button type="button" class="redo btn" style="border: solid 1px;" data-dismiss="modal">' + button_message +'</button>' +
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