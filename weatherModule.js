const labels = ["-15 min","-10 min","-5 min","0 min","+5 min","+10 min","+15 min"];
const data = {
  labels: labels,
  datasets: [{
    label: "Rain percentage",
    data: [65, 59, 80, 81, 56, 55, 40],
    fill: false,
    borderColor: "rgb(75, 192, 192)",
    tension: 0.1
  }]
};
const config = {
    type: "line",
    data: data,
};
function showWeatherCharts() {
    new Chart(document.getElementById("rainPercentageChart"),config);
    new Chart(document.getElementById("trackTempChart"),config);
    new Chart(document.getElementById("airTempChart"),config);
}