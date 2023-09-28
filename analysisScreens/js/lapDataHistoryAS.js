
var fastestS1 = {};
var fastestS2 = {};
var fastestS3 = {};

function updateLapDataHistoryAS() {
    if (session==undefined || lapData==undefined || participants==undefined) {
        return;
    }
    function gapCalculator(bestSector,sector) {
        if (bestSector.time==undefined) {
        	bestSector.time=sector;
        	return "";
        }
        var bestTime = bestSector.time;
        if (bestTime > sector) {
            var gap = gapFormat(bestTime-sector).replace("+","-");
            bestSector.time=sector;
            return gap
        } else {
            return gapFormat(sector-bestTime);
        }
    }
    var ranking = Array(participants.length).fill(undefined);
    function buildFloor(teamcolor,name,pos,besttime,gaptobest,gaptonext,bests1time,bests1overall,bests2time,bests2overall,bests3time,bests3overall,lastlap,currents1,currents2,currents3,tyrehistory) {
        function buildDiv(floor,className,content="",additionalTreatement=function(){}) {
            let div = document.createElement("div");
            div.setAttribute("class",className);
            div.textContent = content;
            additionalTreatement(div);
            floor.append(div);
        }

        var floor = document.createElement("div");
        floor.setAttribute("class","floorLAPDATAHISTORYAS");

        buildDiv(floor,"teamColorLAPDATAHISTORYAS","", function (div) {
            div.style.backgroundColor = teamcolor
        });
        buildDiv(floor,"nameLAPDATAHISTORYAS",name);

        if (session.sessionType>=10 && session.sessionType<=12) { //race mode
            buildDiv(floor,"bestTimeLAPDATAHISTORYAS",pos);
            document.getElementsByClassName("floorLegendLAPDATAHISTORYAS")[0].getElementsByClassName("bestTimeLAPDATAHISTORYAS")[0].textContent = "Position";
        } else if (session.sessionType != 0) { //quali fp and tt mode
            buildDiv(floor,"bestTimeLAPDATAHISTORYAS",msToMinSecMs(besttime));
            document.getElementsByClassName("floorLegendLAPDATAHISTORYAS")[0].getElementsByClassName("bestTimeLAPDATAHISTORYAS")[0].textContent = "Best Time";
        }

        buildDiv(floor,"gapToBestLAPDATAHISTORYAS",gapFormat(gaptobest));
        buildDiv(floor,"gapToNextLAPDATAHISTORYAS",gapFormat(gaptonext));

        function buildBestSector(className,time,gap) {
            if (gap=="+0.000") {
                buildDiv(floor,className,time, function (div) {
                    div.style.backgroundColor="fuchsia"
                });
            } else {
                buildDiv(floor,className,"", function (div) {
                    let timesubdiv = document.createElement("div");
                    let gapsubdiv = document.createElement("div");
                    timesubdiv.setAttribute("class","timeLAPDATAHISTORYAS");
                    gapsubdiv.setAttribute("class","gapLAPDATAHISTORYAS");
                    timesubdiv.innerHTML = time;
                    gapsubdiv.innerHTML = gap;
                    div.append(timesubdiv);
                    div.append(gapsubdiv);
                });
            }
        }
        buildBestSector("bestS1LAPDATAHISTORYAS",bests1time,gapCalculator(bests1overall,bests1time));
        buildBestSector("bestS2LAPDATAHISTORYAS",bests2time,gapCalculator(bests2overall,bests2time));
        buildBestSector("bestS3LAPDATAHISTORYAS",bests3time,gapCalculator(bests3overall,bests3time));

        buildDiv(floor,"lastLapLAPDATAHISTORYAS",lastlap);
        function improveColor(div,current,personalBest,overallBest) {
            if (overallBest > current) {
                div.style.backgroundColor = "fuschia";
            } else if (personalBest > current) {
                div.style.backgroundColor = "limegreen";
            } else {
                div.style.backgroundColor = "yellow";
            }
        }
        buildDiv(floor,"currentS1LAPDATAHISTORYAS",currents1, function (div) {improveColor(div,currents1,bests1time,bests1overall.time)});
        buildDiv(floor,"currentS2LAPDATAHISTORYAS",currents2, function (div) {improveColor(div,currents2,bests2time,bests2overall.time)});
        buildDiv(floor,"currentS3LAPDATAHISTORYAS",currents3, function (div) {improveColor(div,currents3,bests3time,bests3overall.time)});
        
        buildDiv(floor,"tyreHistoryLAPDATAHISTORYAS","", function (div) {
            for (let e of tyrehistory) {
                let sub = document.createElement("img");
                sub.setAttribute("src",tyreID(e.tyreVisualCompound));
                div.append(sub);
            }
        })
    }
    for (let i=0; i<participants.length; i++) {
        let fullData = data.lapData[i];
        let par = participants[i];
        let hist = lapDataHistory[i];
        if (par.name!=""){
            buildFloor(par.teamColor,par.name.substring(0,3),fullData.carPosition,hist.lapHistoryData[hist.bestLapTimeLapNum].lapTimeInMS,
            fullData.deltaToRaceLeaderinMS,fullData.deltaToCarInFrontInMS,
            hist.lapHistoryData[hist.bestSector1LapNum].sector1TimeInMS,fastestS1,
            hist.lapHistoryData[hist.bestSector2LapNum].sector2TimeInMS,fastestS2,
            hist.lapHistoryData[hist.bestSector3LapNum].sector3TimeInMS,fastestS3,
            msToMinSecMs(fullData.lastLapTimeInMS), fullData.sector1TimeInMS,fullData.sector2TimeInMS,/*currents3time*/0,// Pour les secteurs, algo à designer selon les valeurs par défaut des temps en ms des secteurs dans le session history.
            hist.tyreStintHistoryData.slice(0,hist.numTyreStints))
        }
    }
    let tower = document.getElementById("towerLAPDATAHISTORYAS");
    Array.from(tower.getElementsByClassName("floorLAPDATAHISTORYAS")).forEach(element => {
        element.remove();
    });
    for (let j=0; j<participants.length; j++) {
        if (ranking[j]!= undefined) {
            tower.append(ranking[j]);
        }
    }
}

var timeEvolutionChart;

function updateTimeEvolutionChart(oppIdx) {
    // Vérifier TOUT. Peu susceptible de marcher du premier coup, notamment la partie reglin

    if (lapDataHistory[driverCarIdx]==undefined || lapDataHistory[oppIdx]==undefined) {
        return;
    }

    var laps = Array.from({length: 21}, (_, i) => i-10); // [-10,-9,...,-1,0,1,...,9,10]
    var driverTimes = lapDataHistory[driverCarIdx].lapHistoryData.slice(lapDataHistory[driverCarIdx].numLaps-10).map(e => e.lapTimeInMS);
    var opponentTimes = lapDataHistory[oppIdx].lapHistoryData.slice(lapDataHistory[oppIdx].numLaps-10).map(e => e.lapTimeInMS);
    /*FILL WITH PREDICTIONS*/
    /*REGLIN*/
    function reglin(times) {
        /* times must be in ms untreated*/
        var x=laps.slice(0,10);
        var y=times;
        if (x.length!=y.length) {
            throw new Error('Not same length for both arrays')
        }
        var l = x.length;
        var xavg = x.reduce((a,c)=>a+c)/l;
        var yavg = y.reduce((a,c)=>a+c)/l;
        var covxy, varx;
        for (var i=0; i<l; i++) {
            covxy += (x[i]-xavg)*(y[i]-yavg);
            varx += (x[i]-xavg)*(x[i]-xavg);
        }
        covxy/=l;
        varx/=l;
        var a = covxy/varx;
        var b = yavg - a*xavg;
        return [a,b];
    }
    function evalreg(a,b,x) {
        return a*x+b;
    }
    var coeff = reglin(driverTimes);
    var oppcoeff = reglin(opponentTimes);
    for (var i = 0; i<10; i++) {
        driverTimes.append(evalreg(coeff[0],coeff[b],i));
        opponentTimes.append(evalreg(oppcoeff[0],oppcoeff[b],i));
    }
    driverTimes.map(x => msToMinSecMs(x));
    opponentTimes.map(x => msToMinSecMs(x));
    if (timeEvolutionChart==undefined) {
        const dataTime = {
            labels: laps,
            datasets: [{
                label: participants[driverCarIdx].name+" lap times",
                data: driverTimes,
                fill: false,
                borderColor: participants[driverCarIdx].teamColor,
                tension: 0.4,
                segment: {
                    borderDash: function(ctx) {
                        if (ctx.p0 >0) {
                            return [6,6];
                        } 
                        return undefined;
                    }
                },
                spanGaps: true
            },{
                label: participants[oppIdx].name+" lap times",
                data: opponentTimes,
                fill: false,
                borderColor: participants[oppIdx].teamColor,
                tension: 0.4,
                segment: {
                    borderDash: function(ctx) {
                        if (ctx.p0 >0) {
                            return [6,6];
                        } 
                        return undefined;
                    }
                },
                spanGaps: true
            }]
        };
        const configTime = {
            type: "line",
            data: dataTime,
        };
        timeEvolutionChart = new Chart(document.getElementById("timeEvolutionChart"),configTime);
    } else {
        timeEvolutionChart.data.datasets[0].data=driverTimes;
        timeEvolutionChart.data.datasets[1].data=opponentTimes;
        timeEvolutionChart.update();
    }
}

function updateStrikingDistance(oppIdx) {
    document.querySelector('#teamColorDriverLAPDATAHISTORYAS').classList.background = participants[driverCarIdx].teamColor;
    document.querySelector('#teamColorOpponentLAPDATAHISTORYAS').classList.background = participants[oppIdx].teamColor;
    document.querySelector('#nameDriverLAPDATAHISTORYAS').innerHTML = participants[driverCarIdx].name;
    document.querySelector('#nameOpponentLAPDATAHISTORYAS').innerHTML = participants[oppIdx].name;

    //Calcul de la striking distance 50% 1 lap 10% 10+lap
    function strikingDistance() {
        var ldhdriver = lapDataHistory[driverCarIdx];
        var ldhopp = lapDataHistory[oppIdx];

        var lastPitLapDriver = Math.min(10,ldhdriver.numLaps-ldhdriver.tyreStintHistoryData.slice(0,ldhdriver.numTyreStints).map(e=>e.endLap).reduce((a,c)=>Math.max(a,c)));
        var lastPitLapOpponent = Math.min(10,ldhopp.numLaps-ldhopp.tyreStintHistoryData.slice(0,ldhopp.numTyreStints).map(e=>e.endLap).reduce((a,c)=>Math.max(a,c)));

        var avgPaceDriver = (ldhdriver.lapHistoryData.slice(lastPitLapDriver).map(e=>e.lapTimeInMS).reduce((a,c)=>a+c))/lastPitLapDriver;
        var avgPaceOpponent = (ldhopp.lapHistoryData.slice(lastPitLapOpponent).map(e=>e.lapTimeInMS).reduce((a,c)=>a+c))/lastPitLapOpponent;

        var timeGap = Math.abs(lapData[driverCarIdx].deltaToRaceLeaderinMS - lapData[oppIdx].deltaToRaceLeaderinMS);

        return Math.ceil(timeGap / Math.abs(avgPaceDriver-avgPaceOpponent))
    }

    var sd = strikingDistance();
    var pct = Math.max(50 - sd*4,10)

    document.querySelector('#textSDLAPDATAHISTORYAS').innerHTML="Striking Distance : "+((sd>10)?"10+":sd)+" Laps";
    document.documentElement.style.setProperty('--distance-width', pct+'%');
}