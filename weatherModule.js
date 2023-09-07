
var rainPercentageChart;
var airTempChart;
var trackTempChart;

function updateWeather () {
    if (session==undefined) {
        return;
    }
    function weatherID(id) {
        switch (id) {
            case 0:
                return "sunny";
            case 1:
                return "partly_cloudy_day"
            case 2:
                return "cloud";
            case 3:
                return "rainy_light"
            case 4:
                return "rainy_heavy"
            case 5:
                return "thunderstorm"
        }
    }
    document.getElementsByClassName("weatherWEATHERMODULE")[0].getElementsByClassName("material-symbols-outlined")[0].textContent = weatherID(session.weather);
    document.getElementsByClassName("airTempWEATHERMODULE")[0].textContent = "Air Temp : "+session.airTemperature;
    document.getElementsByClassName("trackTempWEATHERMODULE")[0].textContent = "Track Temp : "+session.trackTemperature;
    
    var weatherSamples = session.weatherForecastSamples;
    var sessionType = session.sessionType;
    var times = [];
    var rainPercentages = [];
    var airTemperatures = [];
    var trackTemperatures = [];
    for (let e of weatherSamples) {
        if (e.sessionType==sessionType) {
            times.append(e.timeOffset);
            rainPercentages.append(e.rainPercentage);
            airTemperatures.append(e.airTemperature);
            trackTemperatures.append(e.trackTemperature);
        }
    }
    
    
    
    if (rainPercentageChart==undefined) {
        const dataRain = {
            labels: times,
            datasets: [{
                label: "Rain percentage forecast",
                data: rainPercentages,
                fill: false,
                borderColor: "rgb(75, 192, 192)",
                tension: 0.1
            }]
        };
        const configRain = {
            type: "line",
            data: dataRain,
        };
        rainPercentageChart = new Chart(document.getElementById("rainPercentageChart"),configRain);
    } else {
        rainPercentageChart.data.datasets.data=rainPercentages;
        rainPercentageChart.update();
    }
    if (trackTempChart==undefined) {
        const dataTrack = {
            labels: times,
            datasets: [{
                label: "Track temperature forecast",
                data: trackTemperatures,
                fill: false,
                borderColor: "rgb(117, 117, 117)",
                tension: 0.1
            }]
        };
        const configTrack = {
            type: "line",
            data: dataTrack,
        };
        trackTempChart = new Chart(document.getElementById("trackTempChart"),configTrack);
    } else {
        trackTempChart.data.datasets.data=trackTemperatures;
        trackTempChart.update();
    }
    if (airTempChart==undefined) {
        const dataAir = {
            labels: times,
            datasets: [{
                label: "Air temperature forecast",
                data: airTemperatures,
                fill: false,
                borderColor: "rgb(230, 230, 230)",
                tension: 0.1
            }]
        };
        const configAir = {
            type: "line",
            data: dataAir,
        };
        airTempChart = new Chart(document.getElementById("airTempChart"),configAir);
    } else {
        airTempChart.data.datasets.data=airTemperatures;
        airTempChart.update();
    }
    
}