<footer class="footer ">
    <div class="container">
        <div class="copyright center">
            &copy; <script>document.write(new Date().getFullYear())</script>, adapted with <i class="material-icons">favorite</i> by <a href="https://github.com/ademord" target="_blank">Ademord</a> for a better web.
        </div>
    </div>
</footer>

<!--<script src="https://playground.abysscorp.org/chartjs/livecharts/dist/Chart.min.js"></script>-->
<!--<script src="<?php echo e(asset('js/bootstrap.min.js')); ?>"></script>-->
<script src="<?php echo e(asset('js/app.js')); ?>"></script>


<!--   Core JS Files   -->
<!--<script src="<?php echo e(asset('js/jquery-3.3.1.min.js')); ?>"></script>-->

<!--<script src="<?php echo e(asset('js/jquery.steps.min.js')); ?>"></script>-->

<!--<script src="<?php echo e(asset('js/popper.min.js')); ?>"></script>-->

<script src="<?php echo e(asset('js/bootstrap-material-design.min.js')); ?>"></script>

<script src="<?php echo e(asset('js/perfect-scrollbar.jquery.min.js')); ?>"></script>


<!--  Google Maps Plugin  -->
<!--<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB2Yno10-YTnLjjn_Vtk0V8cdcY5lC4plU"></script>-->

<!--  Plugin for Date Time Picker and Full Calendar Plugin  -->
<!--<script src="<?php echo e(asset('js/moment.min.js')); ?>"></script>-->

<!--	Plugin for the Datepicker, full documentation here: https://github.com/Eonasdan/bootstrap-datetimepicker -->
<!--<script src="<?php echo e(asset('js/bootstrap-datetimepicker.min.js')); ?>"></script>-->

<!--	Plugin for the Sliders, full documentation here: http://refreshless.com/nouislider/ -->
<!--<script src="<?php echo e(asset('js/nouislider.min.js')); ?>"></script>-->

<!--	Plugin for Select, full documentation here: http://silviomoreto.github.io/bootstrap-select -->
<!--<script src="<?php echo e(asset('js/bootstrap-selectpicker.js')); ?>"></script>-->

<!--	Plugin for Tags, full documentation here: http://xoxco.com/projects/code/tagsinput/  -->
<!--<script src="<?php echo e(asset('js/bootstrap-tagsinput.js')); ?>"></script>-->

<!--	Plugin for Fileupload, full documentation here: http://www.jasny.net/bootstrap/javascript/#fileinput -->
<!--<script src="<?php echo e(asset('js/jasny-bootstrap.min.js')); ?>"></script>-->

<!-- Plugins for presentation and navigation-->
<script src="<?php echo e(asset('js/modernizr.js')); ?>"></script>

<!-- Include a polyfill for ES6 Promises (optional) for IE11, UC Browser and Android browser support SweetAlert -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/core-js/2.4.1/core.js"></script>

<!-- Library for adding dinamically elements -->
<script src="<?php echo e(asset('js/arrive.min.js')); ?>" type="text/javascript"></script>

<!-- Material Kit Core initialisations of plugins and Bootstrap Material Design Library-->
<script src="<?php echo e(asset('js/material-dashboard-angular.js')); ?>"></script>

<!--  Charts Plugin, full documentation here: https://gionkunz.github.io/chartist-js/ -->
<script src="<?php echo e(asset('js/chartist.min.js')); ?>"></script>

<!--  Plugin for the Wizard, full documentation here: https://github.com/VinceG/twitter-bootstrap-wizard -->
<script src="<?php echo e(asset('js/jquery.bootstrap-wizard.js')); ?>"></script>
<script src="<?php echo e(asset('js/jquery.validate.min.js')); ?>"></script>

<!-- Vector Map plugin, full documentation here: http://jvectormap.com/documentation/ -->
<script src="<?php echo e(asset('js/jquery-jvectormap.js')); ?>"></script>

<!-- Material Dashboard DEMO methods -->
<script src="<?php echo e(asset('js/demo.js')); ?>"></script>

<script type="text/javascript">

    $(document).ready(function(){

        //init wizard

        demo.initMaterialWizard();

        // Javascript method's body can be found in assets/js/demos.js
        demo.initDashboardPageCharts();

        demo.initCharts();

    });

</script>

<?php echo $__env->yieldContent('footer'); ?>