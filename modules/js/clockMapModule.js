
var clockMapPostsChart;
function updateClockMap(){
    if (session==undefined) {
        return;
    }
    var labels;
    var sectorSizes;
    var sectorFlags;
    function flagColor(id) {
        switch(id) {
            case "-1":
            case "0":
                return "transparent";
            case "1":
                return "limegreen";
            case "2":
                return "blue";
            case "3":
                return "yellow";
        }
    }
    for (let i=0; i<session.numMarshalZones-1; i++) {
        zone = session.marshalZones[i];
        nextZone = session.marshalZones[i+1];
        labels.push("Marshal post n°"+(i+1));
        sectorSizes.push(nextZone.zoneStart-zone.zoneStart);
        sectorFlags.push(flagColor(zone.zoneFlag));
    }
    var lastZone = session.marshalZones[session.numMarshalZones-1]
    labels.push("Marshal post n°"+(session.numMarshalZones-1));
    sectorSizes.push(1-lastZone.zoneStart);
    sectorFlags.push(flagColor(lastZone.zoneFlag))
    if (clockMapPostsChart==undefined) {
        const data = {
            labels: labels,
            datasets: [{
                data: sectorSizes,
                backgroundColor: sectorFlags 
            }]
        };
          
        const config = {
            type: 'doughnut',
            data: data,
            options: {
                cutout: "95%",
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        };
          
        clockMapPostsChart = new Chart(document.getElementById("clockMapPosts"),config);
    } else {
        clockMapPostsChart.data.datasets.backgroundColor=sectorFlags;
        clockMapPostsChart.update();
    }
}

