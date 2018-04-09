$('#launchPlan').on('click', function() {
    // $("#modal-background").toggleClass("active", 1000);
    $('#createManifestModal').modal({backdrop: 'static', keyboard: false});
    $("div[role=tooltip]").remove();

});

$('#addService').on('click', function() {
    // $("#modal-background").toggleClass("active", 1000);
    $('#createServiceModal').modal({backdrop: 'static', keyboard: false});
    //init wizard
    demo.initMaterialWizard();
    component = $('.btn-next');
    if (component && component.hasClass('btn')) {
        component.removeClass('disabled');
    }
    $("div[role=tooltip]").remove();

});

$(".dropdown-menu a").click(function(){
    $(this).parents(".dropdown").find('.btn').html($(this).text() );
    $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
});

