document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on('connect', () => {
        socket.emit('joined');
        document.querySelector('#addChannel').addEventListener('click', () => {
            localStorage.removeItem('last_channel');
        });

        document.querySelector('#logout').addEventListener('click', () => {
            localStorage.removeItem('last_channel');
        });

        document.querySelector('#messageBox').addEventListener("keydown", event => {
            if (event.key == "Enter") {
                document.getElementById("sendButton").click();
            }
        });
        
        document.querySelector('#sendButton').addEventListener("click", () => {
            
            let timestamp = new Date;
            timestamp = timestamp.toLocaleTimeString();

            let msg = document.getElementById("messageBox").value;

            socket.emit('send message', msg, timestamp);
            
            document.getElementById("messageBox").value = '';
        });
    });
    
    socket.on('status', data => {

        let row = '<' + `${data.msg}` + '>'
        document.querySelector('#channelChat').value += row + '\n';

        localStorage.setItem('last_channel', data.channel)
    })

    socket.on('announce message', data => {

        let row = '<' + `${data.timestamp}` + '> - ' + '[' + `${data.user}` + ']:         ' + `${data.msg}`
        document.querySelector('#channelChat').value += row + '\n'
    })

    
});