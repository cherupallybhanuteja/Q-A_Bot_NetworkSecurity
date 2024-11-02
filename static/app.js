document.addEventListener('DOMContentLoaded', function () {
    const chatArea = document.getElementById('chat-area');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    function formatTime(date) {
        let hours = date.getHours();
        let minutes = date.getMinutes();
        const ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12;
        hours = hours ? hours : 12;
        minutes = minutes < 10 ? '0' + minutes : minutes;
        return `${hours}:${minutes} ${ampm}`;
    }

    function createUserMessage(text) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', 'user-message');
        const timeElement = document.createElement('span');
        timeElement.classList.add('message-time', 'user-time');
        timeElement.innerText = formatTime(new Date());
        const textElement = document.createElement('div');
        textElement.innerText = text;
        messageElement.appendChild(textElement);
        messageElement.appendChild(timeElement);
        chatArea.appendChild(messageElement);
        chatArea.scrollTop = chatArea.scrollHeight;
    }

    function createBotMessage(text, source) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', 'bot-message');
        const textElement = document.createElement('div');
        textElement.innerHTML = text.split('\n').map(para => `<p>${para}</p>`).join('');
        messageElement.appendChild(textElement);

        if (source) {
            const sourceElement = document.createElement('div');
            sourceElement.classList.add('source-text');
            sourceElement.innerText = `Source: ${source}`;
            messageElement.appendChild(sourceElement);
        }

        const timeElement = document.createElement('span');
        timeElement.classList.add('message-time', 'bot-time');
        timeElement.innerText = formatTime(new Date());
        messageElement.appendChild(timeElement);
        chatArea.appendChild(messageElement);
        chatArea.scrollTop = chatArea.scrollHeight;
    }

    sendButton.addEventListener('click', async function () {
        const userInputText = userInput.value;
        if (!userInputText.trim()) return;

        createUserMessage(userInputText);
        userInput.value = '';

        try {
            const response = await fetch('/ask', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user_input: userInputText })
            });

            const data = await response.json();
            createBotMessage(data.answer, data.source);
        } catch (error) {
            createBotMessage("Error fetching response.");
        }
    });
});
