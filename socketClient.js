var ip="127.0.0.2";
var port = 8823;
var wssURL = "wss://"+ip+":"+port;

const wss = new WebSocket(wssURL);
wss.onopen = () => {
    console.log("Opening WSS connection with PLA");
}

wss.onmessage = (event) => {
    console.log("Message recieved from PLA");
    let data = JSON.parse(event.data);
    
}

wss.onclose = (event) => {
    console.log("PLA WSS closed on event number "+event.code);
}