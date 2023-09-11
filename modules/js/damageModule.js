
/**
 * Updates the damage module
 * Uses the carDamage packet and the carTelemetry packet
 */
function updateDamage() {
    if (carDamage==undefined || carTelemetry==undefined) {
        return;
    }
    function modifyPercentage(className, value, name) {
        let e = document.getElementsByClassName(className)[0];
        e.textContent = name + " : " + value + "%";
        let red = value*255/100;
        let green = 255-red;
        e.style.backgroundColor="rgba("+red+","+green+",0,0.5)"
    }
    dmg = carDamage.carDamageData[carDamage.header.playerCarIndex];
    tel = carTelemetry.carTelemetryData[carTelemetry.header.playerCarIndex];
    modifyPercentage("frontLeftWingDmgDAMAGEMODULE",dmg.frontLeftWingDamage,"Front Left Wing Damage");
    modifyPercentage("frontRightWingDmgDAMAGEMODULE",dmg.frontRightWingDamage,"Front Right Wing Damage");
    modifyPercentage("floorDmgDAMAGEMODULE",dmg.floorDamage,"Floor Damage");
    modifyPercentage("sidepodDmgDAMAGEMODULE",dmg.sidepodDamage,"Sidepod Damage");

    let tmp = document.getElementsByClassName("engineTmpDAMAGEMODULE")[0];
    tmp.innerHTML = "Engine Temp : "+tel.engineTemperature+"&deg;C";
    if (tel.engineTemperature<70) {
        tmp.style.backgroundColor="rgba(0,255,0,0.5)"
    } else if (tel.engineTemperature>130) {
        tmp.style.backgroundColor="rgba(255,0,0,0.5)"
    } else {
        function getPercentageFill(min,max,value) {
            var a = 100/(max-min);
            var b = min*(-a);
            return a*value+b;
        }
        let redtmp = getPercentageFill(90,140,tel.engineTemperature)*255/100;
        let greentmp = 255-redtmp;
        tmp.style.backgroundColor="rgba("+redtmp+","+greentmp+",0,0.5)"
    }

    modifyPercentage("diffuserDmgDAMAGEMODULE",dmg.diffuserDamage,"Diffuser Damage");
    modifyPercentage("rearWingDmgDAMAGEMODULE",dmg.rearWingDamage,"Rear Wing Damage");

    tmp = document.getElementsByClassName("ersDAMAGEMODULE")[0];
    let fault = dmg.ersFault;
    if (fault==0) {
        tmp.textContent = "ERS : OK";
        tmp.style.backgroundColor = "rgba(0,255,0,0.5)";
    } else if (fault==1) {
        tmp.textContent = "ERS : FAILURE";
        tmp.style.backgroundColor = "rgba(255,0,0,0.5)";
    } else {
        tmp.textContent = "ERS : UNKNOWN";
        tmp.style.backgroundColor = "rgba(100,100,100,0.5)";
    }

    tmp = document.getElementsByClassName("drsDAMAGEMODULE")[0];
    fault = dmg.drsFault;
    if (fault==0) {
        tmp.textContent = "DRS : OK";
        tmp.style.backgroundColor = "rgba(0,255,0,0.5)";
    } else if (fault==1) {
        tmp.textContent = "DRS : FAILURE";
        tmp.style.backgroundColor = "rgba(255,0,0,0.5)";
    } else {
        tmp.textContent = "DRS : UNKNOWN";
        tmp.style.backgroundColor = "rgba(100,100,100,0.5)";
    }

    modifyPercentage("gearboxDmgDAMAGEMODULE",dmg.gearBoxDamage,"Gearbox Damage");
    modifyPercentage("engineDmgDAMAGEMODULE",dmg.engineDamage,"Engine Damage");
}