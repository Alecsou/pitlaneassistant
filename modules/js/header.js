
function updateHeader() {
    if (session==undefined) {
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
    let header = document.getElementById("header");
    header.getElementById("circuitInfo").getElementById("circuitInfoFlag").getElementsByTagName("img")[0].setAttribute("src",session.trackflag);
    header.getElementById("circuitInfo").getElementById("circuitInfoName").innerHTML=session.trackName;
    header.getElementById("sessionType").innerHTML=session.sessionTypeName;
    header.getElementById("airTemp").innerHTML="Air Temp. : "+session.airTemperature+"&deg;C";
    header.getElementById("trackTemp").innerHTML="Track Temp. : "+session.trackTemperature+"&deg;C";
    header.getElementById("lapCount").innerHTML="Lap ?/"+session.totalLaps;
    header.getElementById("clock").innerHTML=timeFormat(session.sessionTimeLeft);
}