async function sendMessage() {

    const input = document.getElementById("userInput");
    const chatMessages = document.getElementById("chatMessages");

    const question = input.value.trim();

    if (question === "") {
        return;
    }

    // Display user message
    const userMessage = document.createElement("div");
    userMessage.className = "message user";
    userMessage.innerHTML = `<strong>You:</strong> ${question}`;

    chatMessages.appendChild(userMessage);

    input.value = "";

    // Display loading message
    const loadingMessage = document.createElement("div");
    loadingMessage.className = "message bot";
    loadingMessage.innerHTML = "<strong>EduGenie:</strong> Thinking... 🤔";

    chatMessages.appendChild(loadingMessage);

    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        loadingMessage.innerHTML =
            `<strong>EduGenie:</strong> ${data.answer}`;

    } catch (error) {

        loadingMessage.innerHTML =
            "<strong>EduGenie:</strong> Sorry, something went wrong. ❌";

        console.error(error);
    }

    chatMessages.scrollTop = chatMessages.scrollHeight;
}


// Press Enter to send message
document.getElementById("userInput").addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});
