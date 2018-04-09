var samples = 100;
var speed = 250;
var values = [];
var labels = [];
var charts = [];
var value = 0;

values.length = samples;
labels.length = samples;
values.fill(0);
labels.fill(0);

function initialize() {
  charts.push(new Chart(document.getElementById("chart0"), {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        data: values,
        backgroundColor: 'rgba(255, 99, 132, 0.9)',
        borderColor: 'rgb(255, 99, 132)',
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      animation: {
        duration: speed * 1.5,
        easing: 'linear'
      },
      legend: false,
      scales: {
        xAxes: [{
          display: false
        }],
        yAxes: [{
          ticks: {
            max: 10,
            min: 0,
            stepSize: 1
          }
        }]
      }
    }
  }));
}


function advanceLiveChart(data) {
  // value = Math.min(Math.max(value + (0.1 - Math.random() / 5), 0), 1);
  value = data;
  values.push(value);
  values.shift();
  charts.forEach(function(chart) { chart.update(); });
}

