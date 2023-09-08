
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
    modifyPercentage("frontLeftWingDmgDAMAGEMODULE",carDamage.frontLeftWingDamage,"Front Left Wing Damage");
    modifyPercentage("frontRightWingDmgDAMAGEMODULE",carDamage.frontRightWingDamage,"Front Right Wing Damage");
    modifyPercentage("floorDmgDAMAGEMODULE",carDamage.floorDamage,"Floor Damage");
    modifyPercentage("sidepodDmgDAMAGEMODULE",carDamage.sidepodDamage,"Sidepod Damage");

    let tmp = document.getElementsByClassName("engineTmpDAMAGEMODULE");
    tmp.textContent = "Engine Temp : "+carTelemetry.engineTemperature+"C";
    if (carTelemetry.engineTemperature<70) {
        tmp.style.backgroundColor="rgba(0,255,0,0.5)"
    } else if (carTelemetry.engineTemperature>130) {
        tmp.style.backgroundColor="rgba(255,0,0,0.5)"
    } else {
        function getPercentageFill(min,max,value) {
            var a = 100/(max-min);
            var b = min*(-a);
            return a*value+b;
        }
        let redtmp = getPercentageFill(70,130,carTelemetry.engineTemperature)*255/100;
        let greentmp = 255-redtemp;
        tmp.style.backgroundColor="rgba("+redtmp+","+greentmp+",0,0.5)"
    }

    modifyPercentage("diffuserDmgDAMAGEMODULE",carDamage.diffuserDamage,"Diffuser Damage");
    modifyPercentage("rearWingDmgDAMAGEMODULE",carDamage.rearWingDamage,"Rear Wing Damage");

    tmp = document.getElementsByClassName("ersDAMAGEMODULE")[0];
    let fault = carDamage.ersFault;
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
    fault = carDamage.drsFault;
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

    modifyPercentage("gearboxDmgDAMAGEMODULE",carDamage.gearBoxDamage,"Gearbox Damage");
    modifyPercentage("engineDmgDAMAGEMODULE",carDamage.engineDamage,"Engine Damage");
}