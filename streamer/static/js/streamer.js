var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var stream_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);
document.getElementById('#keyword').addEventListner('click', function(event) {
    var message = {
        keyword: document.getElementById('#keyword').value
    }
    stream_socket.send(JSON.stringify(message));
    return false;
});