
function updateCarStatus() {
    if (session==undefined || carStatus==undefined) {
        return;
    }
    var status = carStatus.carStatusData[carStatus.header.playerCarIndex];
    //Flag
    var flag = document.getElementsByClassName("flagCARSTATUSMODULE")[0];
    switch (status.vehicleFiaFlags) {
        case "-1":
        case "0":
            flag.style.animation="none";
            break;
        case "1":
            flag.style.animation="greenFlag 1s infinite";
            break;
        case "2":
            flag.style.animation="blueFlag 1s infinite";
            break;
        case "3":
            flag.style.animation="yellowFlag 1s infinite";
            break;
    }
    //SC/VSC/FL
    var sc = document.getElementsByClassName("safetyCarCARSTATUSMODULE")[0];
    switch (session.safetyCarStatus) {
        case "0":
            sc.style.background = "transparent";
            sc.innerHTML = "";
            break;
        case "1":
            sc.style.background = "yellow";
            sc.innerHTML = "SC";
            break;
        case "2":
            sc.style.background = "yellow";
            sc.innerHTML = "VSC";
            break;
        case "3":
            sc.style.background = "yellow";
            sc.innerHTML = "FL";
            break;
    }
    var MAXERS = 4000000
    document.getElementsByClassName("fuelGaugeIndicatorCARSTATUSMODULE")[0].style.width = ((status.fuelInTank / status.fuelCapacity)*100).toFixed(1)+"%";
    document.getElementsByClassName("fuelValueCARSTATUSMODULE")[0].innerHTML = status.fuelInTank.toFixed(2)+"/"+status.fuelCapacity.toFixed(2)+"("+status.fuelRemainingLaps.toFixed(2)+")";

    document.getElementsByClassName("ERSdeployGaugeIndicatorCARSTATUSMODULE")[0].style.width = ((status.ersDeployedThisLap/MAXERS)*100).toFixed(1)+"%";
    document.getElementsByClassName("ERSdeployValueCARSTATUSMODULE")[0].innerHTML = ((status.ersDeployedThisLap/MAXERS)*100).toFixed(1)+"%";

    document.getElementsByClassName("ERSharvestGaugeIndicatorCARSTATUSMODULE")[0].style.width = (((status.ersHarvestedThisLapMGUK+status.ersHarvestedThisLapMGUH)/MAXERS)*100).toFixed(1)+"%";
    document.getElementsByClassName("ERSharvestValueCARSTATUSMODULE")[0].innerHTML = (((status.ersHarvestedThisLapMGUK+status.ersHarvestedThisLapMGUH)/MAXERS)*100).toFixed(1)+"%";

    document.getElementsByClassName("ERSstoredGaugeIndicatorCARSTATUSMODULE")[0].style.width = ((status.ersStoreEnergy/MAXERS)*100).toFixed(1)+"%";
    document.getElementsByClassName("ERSstoredValueCARSTATUSMODULE")[0].innerHTML = ((status.ersStoreEnergy/MAXERS)*100).toFixed(1)+"%";

    var deploy = document.getElementsByClassName("ERSdeployModeCARSTATUSMODULE")[0];
    switch (status.ersDeployMode) {
        case "0":
            deploy.innerHTML='Deploy mode : None <span class="material-symbols-outlined">block</span>';
            break;
        case "1":
            deploy.innerHTML='Deploy mode : Medium <span class="material-symbols-outlined">expand_less</span>';
            break;
        case "2":
            deploy.innerHTML='Deploy mode : HotLap <span class="material-symbols-outlined">bolt</span>'
            break;
        case "3":
            deploy.innerHTML='Deploy mode : Overtake <span class="material-symbols-outlined">stat_2</span>'
            break;
    }
    document.getElementsByClassName("frontBrakeBiasCARSTATUSMODULE")[0].innerHTML = "Brake bias : "+status.frontBrakeBias+" %";
}