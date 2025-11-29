const messageForm = document.querySelector('#message-form');
const messagesUl = document.querySelector('.messages-ul');
const input = document.querySelector('.message-input');


const userId = localStorage.getItem('userId') || 0;

window.addEventListener('DOMContentLoaded', () => {
    const Id = localStorage.getItem('userId');

    if (Id) {
        console.log("ID do usuário:", Id);
        userId = Id;
        
    } else {
        console.log("Nenhum usuário logado.");
        // opcional: redirecionar para login se não houver ID
        window.location.href = './login.html';
    }
});

const ws = new WebSocket(`ws://localhost:8000/ws/${userId}`);

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