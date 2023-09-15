
function realTyreId(id) {
    switch (id) {
        case "7":
            return "Inter";
        case "8":
            return "Wet";
        case "16":
            return "C5";
        case "17":
            return "C4";
        case "18":
            return "C3";
        case "19":
            return "C2";
        case "20":
            return "C1";
        case "21":
            return "C0";
    }
}
/**
 * Updates the tyreStatus module
 * Uses the carStatus packet, the carTelemetry packet and the carDamage packet
 */
function updateTyreStatus() {
    if (carStatus==undefined || carTelemetry==undefined || carDamage==undefined) {
        return;
    }
    let status = carStatus.carStatusData[parseInt(carStatus.header.playerCarIndex)];
    let telemetry = carTelemetry.carTelemetryData[parseInt(carTelemetry.header.playerCarIndex)];
    let damage = carDamage.carDamageData[parseInt(carDamage.header.playerCarIndex)];
    function updateTyre(frontrear,leftright,tyreIdx) {
        let tyre = document.getElementsByClassName(frontrear + " " + leftright)[0];
        function modifyElement(bigclass,value,valuediv=true) {
            if (valuediv) {
                tyre.getElementsByClassName(bigclass)[0].getElementsByClassName("valueTYRESTATUSMODULE")[0].innerHTML = value;
            } else {
                tyre.getElementsByClassName(bigclass)[0].innerHTML = value;
            }
        }
        modifyElement("actualCompoundTYRESTATUSMODULE",realTyreId(status.actualTyreCompound),false);
        tyre.getElementsByClassName("visualCompoundTYRESTATUSMODULE")[0].setAttribute("src",tyreID(status.visualTyreCompound));
        modifyElement("brakeTempTYRESTATUSMODULE",telemetry.brakesTemperature[tyreIdx]+" &deg;C");
        modifyElement("tyreSurfaceTempTYRESTATUSMODULE",telemetry.tyresSurfaceTemperature[tyreIdx]+" &deg;C");
        modifyElement("tyreInnerTempTYRESTATUSMODULE",telemetry.tyresInnerTemperature[tyreIdx]+" &deg;C");
        modifyElement("tyrePressureTYRESTATUSMODULE",telemetry.tyresPressure[tyreIdx]+" PSI");
        modifyElement("surfaceContactTYRESTATUSMODULE",telemetry.surfaceType[tyreIdx]);
        modifyElement("tyreWearTYRESTATUSMODULE",damage.tyresWear[tyreIdx]+" %");
        modifyElement("tyreDmgTYRESTATUSMODULE",damage.tyresDamage[tyreIdx]+" %");
        modifyElement("brakeDmgTYRESTATUSMODULE",damage.brakesDamage[tyreIdx]+" %");
    }
    updateTyre("frontTYRESTATUSMODULE","leftTYRESTATUSMODULE",2);
    updateTyre("frontTYRESTATUSMODULE","rightTYRESTATUSMODULE",3);
    updateTyre("rearTYRESTATUSMODULE","leftTYRESTATUSMODULE",0);
    updateTyre("rearTYRESTATUSMODULE","rightTYRESTATUSMODULE",1);
}