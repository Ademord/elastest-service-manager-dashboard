<footer class="footer ">
    <div class="container">
        <div class="copyright center">
            &copy; <script>document.write(new Date().getFullYear())</script>, adapted with <i class="material-icons">favorite</i> by <a href="https://github.com/ademord" target="_blank">Ademord</a> for a better web.
        </div>
    </div>
</footer>

<!--<script src="https://playground.abysscorp.org/chartjs/livecharts/dist/Chart.min.js"></script>-->
<!--<script src="{{ asset('js/bootstrap.min.js') }}"></script>-->
<script src="{{ asset('js/app.js') }}"></script>


<!--   Core JS Files   -->
<!--<script src="{{ asset('js/jquery-3.3.1.min.js') }}"></script>-->

<!--<script src="{{ asset('js/jquery.steps.min.js') }}"></script>-->

<!--<script src="{{ asset('js/popper.min.js') }}"></script>-->

<script src="{{ asset('js/bootstrap-material-design.min.js') }}"></script>

<!--<script src="{{ asset('js/perfect-scrollbar.jquery.min.js') }}"></script>-->


<!--  Google Maps Plugin  -->
<!--<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB2Yno10-YTnLjjn_Vtk0V8cdcY5lC4plU"></script>-->

<!--  Plugin for Date Time Picker and Full Calendar Plugin  -->
<!--<script src="{{ asset('js/moment.min.js') }}"></script>-->

<!--	Plugin for the Datepicker, full documentation here: https://github.com/Eonasdan/bootstrap-datetimepicker -->
<!--<script src="{{ asset('js/bootstrap-datetimepicker.min.js') }}"></script>-->

<!--	Plugin for the Sliders, full documentation here: http://refreshless.com/nouislider/ -->
<!--<script src="{{ asset('js/nouislider.min.js') }}"></script>-->

<!--	Plugin for Select, full documentation here: http://silviomoreto.github.io/bootstrap-select -->
<!--<script src="{{ asset('js/bootstrap-selectpicker.js') }}"></script>-->

<!--	Plugin for Tags, full documentation here: http://xoxco.com/projects/code/tagsinput/  -->
<!--<script src="{{ asset('js/bootstrap-tagsinput.js') }}"></script>-->

<!--	Plugin for Fileupload, full documentation here: http://www.jasny.net/bootstrap/javascript/#fileinput -->
<!--<script src="{{ asset('js/jasny-bootstrap.min.js') }}"></script>-->

 Plugins for presentation and navigation
<!--<script src="{{ asset('js/modernizr.js') }}"></script>-->

<!-- Include a polyfill for ES6 Promises (optional) for IE11, UC Browser and Android browser support SweetAlert -->
<!--<script src="https://cdnjs.cloudflare.com/ajax/libs/core-js/2.4.1/core.js"></script>-->

<!-- Library for adding dinamically elements -->
<!--<script src="{{ asset('js/arrive.min.js') }}" type="text/javascript"></script>-->

<!-- Material Kit Core initialisations of plugins and Bootstrap Material Design Library -->
<script src="{{ asset('js/material-dashboard-angular.js') }}"></script>

<!--  Charts Plugin, full documentation here: https://gionkunz.github.io/chartist-js/ -->
<script src="{{ asset('js/chartist.min.js') }}"></script>

<!-- Vector Map plugin, full documentation here: http://jvectormap.com/documentation/ -->
<script src="{{ asset('js/jquery-jvectormap.js') }}"></script>

<!-- Material Dashboard DEMO methods -->
<script src="{{ asset('js/demo.js') }}"></script>

<script type="text/javascript">
    $(document).ready(function(){
        demo.initVectorMap();
    });

</script>

<script>
    var header_height;
    var fixed_section;
    var floating = false;
    var breakCards = true;

    var searchVisible = 0;
    var transparent = true;

    var transparentDemo = true;
    var fixedTop = false;

    var mobile_menu_visible = 0,
        mobile_menu_initialized = false,
        toggle_initialized = false,
        bootstrap_nav_initialized = false;

    var seq = 0, delays = 80, durations = 500;
    var seq2 = 0, delays2 = 80, durations2 = 500;
    $().ready(function() {
        $('#menuresize a').click(function(){
            var href = $(this).attr('href');
            $('html,body').animate({
                'scrollTop': $($(this).attr('href')).offset().top - 100
            }, 200);
        })
        suggestions_distance = $("#suggestions").offset();
        pay_height = $('.fixed-section').outerHeight();
        if(breakCards == true){
            // We break the cards headers if there is too much stress on them :-)
            $('[data-header-animation="true"]').each(function(){
                var $fix_button = $(this)
                var $card = $(this).parent('.card');

                $card.find('.fix-broken-card').click(function(){
                    console.log(this);
                    var $header = $(this).parent().parent().siblings('.card-header, .card-image');

                    $header.removeClass('hinge').addClass('fadeInDown');

                    $card.attr('data-count',0);

                    setTimeout(function(){
                        $header.removeClass('fadeInDown animate');
                    },480);
                });

                $card.mouseenter(function(){
                    var $this = $(this);
                    hover_count = parseInt($this.attr('data-count'), 10) + 1 || 0;
                    $this.attr("data-count", hover_count);

                    if (hover_count >= 20){
                        $(this).children('.card-header, .card-image').addClass('hinge animated');
                    }
                });
            });
        }

        $(window).on('scroll', checkScrollForTransparentNavbar);
        /* ----------==========     Daily Sales Chart initialization    ==========---------- */

        dataDailySalesChart = {
            labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
            series: [
                [12, 17, 7, 17, 23, 18, 38]
            ]
        };

        optionsDailySalesChart = {
            lineSmooth: Chartist.Interpolation.cardinal({
                tension: 0
            }),
            low: 0,
            high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
            chartPadding: { top: 0, right: 0, bottom: 0, left: 0},
        }

        var dailySalesChart = new Chartist.Line('#dailySalesChart', dataDailySalesChart, optionsDailySalesChart);

        md.startAnimationForLineChart(dailySalesChart);



        /* ----------==========     Completed Tasks Chart initialization    ==========---------- */

        dataCompletedTasksChart = {
            labels: ['12p', '3p', '6p', '9p', '12p', '3a', '6a', '9a'],
            series: [
                [230, 750, 450, 300, 280, 240, 200, 190]
            ]
        };

        optionsCompletedTasksChart = {
            lineSmooth: Chartist.Interpolation.cardinal({
                tension: 0
            }),
            low: 0,
            high: 1000, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
            chartPadding: { top: 0, right: 0, bottom: 0, left: 0}
        }

        var completedTasksChart = new Chartist.Line('#completedTasksChart', dataCompletedTasksChart, optionsCompletedTasksChart);

        // start animation for the Completed Tasks Chart - Line Chart
        md.startAnimationForLineChart(completedTasksChart);


        /* ----------==========     Emails Subscription Chart initialization    ==========---------- */

        var dataWebsiteViewsChart = {
            labels: ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'],
            series: [
                [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895]

            ]
        };
        var optionsWebsiteViewsChart = {
            axisX: {
                showGrid: false
            },
            low: 0,
            high: 1000,
            chartPadding: { top: 0, right: 5, bottom: 0, left: 0}
        };
        var responsiveOptions = [
            ['screen and (max-width: 640px)', {
                seriesBarDistance: 5,
                axisX: {
                    labelInterpolationFnc: function (value) {
                        return value[0];
                    }
                }
            }]
        ];
        var websiteViewsChart = Chartist.Bar('#websiteViewsChart', dataWebsiteViewsChart, optionsWebsiteViewsChart, responsiveOptions);

        //start animation for the Emails Subscription Chart
        md.startAnimationForBarChart(websiteViewsChart);

    });



    function showNotification(from, align) {
        $.notify({
            icon: "notifications",
            message: "Welcome to <b>Material Dashboard Pro</b> - a beautiful dashboard for every web developer."

        }, {
            type: 'success',
            timer: 4000,
            placement: {
                from: from,
                align: align
            }
        });
    }
    function debounce(func, wait, immediate) {
        var timeout;
        return function() {
            var context = this, args = arguments;
            clearTimeout(timeout);
            timeout = setTimeout(function() {
                timeout = null;
                if (!immediate) func.apply(context, args);
            }, wait);
            if (immediate && !timeout) func.apply(context, args);
        };
    };
    function checkScrollForTransparentNavbar(){
        if($(document).scrollTop() > 381 ) {
            if(transparent) {
                transparent = false;
                $('.navbar-color-on-scroll').removeClass('navbar-transparent');
                $('.navbar-title').removeClass('hidden');
            }
        } else {
            if( !transparent ) {
                transparent = true;
                $('.navbar-color-on-scroll').addClass('navbar-transparent');
                $('.navbar-title').addClass('hidden');
            }
        }
    };

</script>

@yield('footer')