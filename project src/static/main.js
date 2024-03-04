document.addEventListener("DOMContentLoaded", function () {
    var socket = io.connect("http://" + document.domain + ":" + location.port);

    socket.on("connect", function () {
        console.log("Connected to server");
    });

    // Update the message field
    socket.on("update_message", function (data) {
        document.getElementById("message").textContent = "Message: " + data.message;
    });

    // Update the result field
    socket.on("update_result", function (data) {
        document.getElementById("result").textContent = "Result: " + data.result;
    });

    // Send user input to the server
    document.getElementById("send-button").addEventListener("click", function () {
        var userInput = document.getElementById("user-input").value;
        socket.emit("user_input", { message: userInput });
    });
});
