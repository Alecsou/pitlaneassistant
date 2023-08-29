function showSetupValues() {
    console.log("Iwascalled");
    let frontwing = document.getElementById("front");
    let rearwing = document.getElementById("rear");
    let diffonthrottle = document.getElementById("onThrottle");
    let diffoffthrottle = document.getElementById("offThrottle");
    let suspFrontCamber = document.getElementById("frontCamber");
    let suspRearCamber = document.getElementById("rearCamber");
    let suspFrontToe = document.getElementById("frontToe");
    let suspRearToe = document.getElementById("rearToe");
    let suspFrontSusp = document.getElementById("frontSuspension");
    let suspRearSusp = document.getElementById("rearSuspension");
    let suspFrontRoll = document.getElementById("frontAntiRollBar");
    let suspRearRoll = document.getElementById("rearAntiRollBar");
    let suspFrontHeight = document.getElementById("frontRideHeight");
    let suspRearHeight = document.getElementById("rearRideHeight");
    let brakePressure = document.getElementById("pressure");
    let brakeBias = document.getElementById("bias");
    let tyreRLP = document.getElementById("rearLeftPressure");
    let tyreRRP = document.getElementById("rearRightPressure");
    let tyreFLP = document.getElementById("frontLeftPressure");
    let tyreFRP = document.getElementById("frontRightPressure");
    let fuelBallast = document.getElementById("ballast");
    let fuelLoad = document.getElementById("load");

    frontwing.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.frontWing;
    frontwing.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.frontWing+"%;");

    rearwing.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.rearWing;
    rearwing.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.rearWing+"%;");

    diffonthrottle.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.onThrottle;
    diffonthrottle.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.onThrottle+"%;");

    diffoffthrottle.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.offThrottle;
    diffoffthrottle.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.offThrottle+"%;");

    suspFrontCamber.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.frontCamber;
    suspFrontCamber.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.frontCamber+"%;");

    suspRearCamber.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.rearCamber;
    suspRearCamber.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.rearCamber+"%;");

    suspFrontToe.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.frontToe;
    suspFrontToe.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.frontToe+"%;");

    suspRearToe.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.rearToe;
    suspRearToe.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.rearToe+"%;");

    suspFrontSusp.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.frontSuspension;
    suspFrontSusp.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.frontSuspension+"%;");

    suspRearSusp.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.rearSuspension;
    suspRearSusp.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.rearSuspension+"%;");

    suspFrontRoll.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.frontAntiRollBar;
    suspFrontRoll.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.frontAntiRollBar+"%;");

    suspRearRoll.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.rearAntiRollBar;
    suspRearRoll.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.rearAntiRollBar+"%;");

    suspFrontHeight.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.frontSuspensionHeight;
    suspFrontHeight.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.frontSuspensionHeight+"%;");

    suspRearHeight.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.rearSuspensionHeight;
    suspRearHeight.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.rearSuspensionHeight+"%;");

    brakePressure.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.brakePressure;
    brakePressure.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.brakePressure+"%;");

    brakeBias.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.brakeBias;
    brakeBias.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.brakeBias+"%;");

    tyreRLP.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.rearLeftTyrePressure;
    tyreRLP.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.rearLeftTyrePressure+"%;");

    tyreRRP.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.rearRightTyrePressure;
    tyreRRP.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.rearRightTyrePressure+"%;");

    tyreFLP.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.frontLeftTyrePressure;
    tyreFLP.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.frontLeftTyrePressure+"%;");

    tyreFRP.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.frontRightTyrePressure;
    tyreFRP.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.frontRightTyrePressure+"%;");

    fuelBallast.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.ballast;
    fuelBallast.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.ballast+"%;");

    fuelLoad.getElementsByClassName('bar-valueSETUPMODULE')[0].innerHTML = carSetup.fuelLoad;
    fuelLoad.getElementsByClassName('bar-fillerSETUPMODULE')[0].setAttribute("style","width:"+carSetup.fuelLoad+"%;");
}