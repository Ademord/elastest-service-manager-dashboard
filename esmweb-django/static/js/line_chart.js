var widget = {
    lineChart: function (div_id, y_axis_title, labels, series, y_high){
        dataDailySalesChart = {
                labels: labels,
                series: [series]
            };

        optionsDailySalesChart = {
            low: 0,
            high: y_high,

            axisY: {
                onlyInteger: true
            },

            lineSmooth: Chartist.Interpolation.cardinal({
                tension: 0
            }),

            chartPadding: {
                top: 0,
                right: 0,
                bottom: 0,
                left: 10
            },

            plugins: [
                Chartist.plugins.ctAxisTitle({
                    axisY: {
                        axisTitle: y_axis_title,
                        axisClass: 'ct-axis-title',
                        offset: {
                            x: 0,
                            y: 11
                        },
                        textAnchor: 'middle',
                        flipTitle: true,
                        onlyInteger: true
                    }
                })
            ]
        };

        var dailySalesChart = new Chartist.Line(('#' + div_id), dataDailySalesChart, optionsDailySalesChart);

        md.startAnimationForLineChart(dailySalesChart);
    }
}