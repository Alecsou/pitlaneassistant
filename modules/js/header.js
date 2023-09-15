
function updateHeader() {
    if (session==undefined || lapData==undefined) {
        return;
    }
    function timeFormat(time){
        var h = Math.floor(time/3600).toString();
        var m = Math.floor(time - h * 3600).toString();
        var s = (time - h*3600 - m*60).toString();
        m=(m.length==1)?"0"+m:m;
        s=(s.length==1)?"0"+s:s;
        return h+":"+m+":"+s;
    }
    var currentLap = lapData.lapData.map((e)=>e.currentLapNum).reduce((p,n)=>((p<n)?n:p));
    document.getElementById("circuitInfoFlag").getElementsByTagName("img")[0].setAttribute("src",session.trackFlag);
    document.getElementById("circuitInfoName").innerHTML=session.trackName;
    document.getElementById("sessionType").innerHTML=session.sessionTypeName;
    document.getElementById("airTemp").innerHTML="Air Temp. : "+session.airTemperature+"&deg;C";
    document.getElementById("trackTemp").innerHTML="Track Temp. : "+session.trackTemperature+"&deg;C";
    document.getElementById("lapCount").innerHTML="Lap "+currentLap+"/"+session.totalLaps;
    document.getElementById("clock").innerHTML=timeFormat(session.sessionDuration);
}