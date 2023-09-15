
var clockMapPostsChart;
function updateClockMap(){
    if (session==undefined) {
        return;
    }
    var labels = [];
    var sectorSizes = [];
    var sectorFlags = [];
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
        labels.push("Marshal post "+(i+1));
        let size = nextZone.zoneStart-zone.zoneStart
        sectorSizes.push((size>0)? size: 1+size);
        sectorFlags.push(flagColor(zone.zoneFlag));
    }
    var lastZone = session.marshalZones[session.numMarshalZones-1]
    labels.push("Marshal post "+(session.numMarshalZones));
    sectorSizes.push(1-lastZone.zoneStart);
    sectorFlags.push(flagColor(lastZone.zoneFlag));
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
        clockMapPostsChart.data.datasets[0].backgroundColor=sectorFlags;
        clockMapPostsChart.update();
    }
}

function updateDriverLine() {
    if (session==undefined || lapData==undefined || participants==undefined) {
        return;
    }
    var lapLength = session.trackLength;
    var bar = document.getElementsByClassName("verticalBarCLOCKMAPMODULE")[0];
    bar.innerHTML = "";
    participants.forEach(e => {
        var lapDistance = lapData.lapData[participants.indexOf(e)].lapDistance;
        var pctg = ((lapDistance/lapLength)*100).toFixed(2);
        var point = document.createElement("div");
        point.setAttribute("class","driverCLOCKMAPMODULE");
        point.style.backgroundColor = e.teamColor;
        point.style.top = "calc("+pctg+"% - 10px)";
        var name = document.createElement("div");
        name.setAttribute("class","driverNameCLOCKMAPMODULE");
        name.innerHTML = e.name.substring(0,3);
        point.append(name);
        bar.append(point);
    });
}

