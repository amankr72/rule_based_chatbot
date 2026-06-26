async function sendMessage() {

    const input = document.getElementById("message");

    const message = input.value;

    if(message === "") return;

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `
        <div class="user">
             <p>${message}</p>
        </div>
    `;

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });
    
    const data = await response.json();

    chatBox.innerHTML += `
        <div class="bot">
           <p> ${data.response}</p>
        </div>
    `;

    input.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;
}
document.addEventListener("DOMContentLoaded", function () {

    const input = document.getElementById("message");

    input.addEventListener("keydown", function (event) {

        if (event.key === "Enter") {

            event.preventDefault();

            sendMessage();

        }

    });

});
