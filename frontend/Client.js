const messageForm = document.querySelector('#message-form');
const messagesUl = document.querySelector('.messages-ul');
const input = document.querySelector('.message-input');


const ws = new WebSocket('ws://localhost:8000/ws/123');

const newMessage = (msg) => {
    messagesUl.innerHTML += `<li>${msg.data}</li>`;
}

ws.onmessage = newMessage;

messageForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const input = document.querySelector('.message-input');
    ws.send(input.value);
    input.value = '';

})