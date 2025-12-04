const messageForm = document.querySelector('#message-form');
const messagesUl = document.querySelector('.messages-ul');
const input = document.querySelector('.message-input');

let usersList = document.querySelector('.users-list');
let userId = localStorage.getItem('userId') || 0;

window.addEventListener('DOMContentLoaded', () => {
    const Id = localStorage.getItem('userId');

    if (Id) {
        console.log("ID do usuário:", Id);
        userId = Id;
        
    } else {
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

const getUsers = async () => {
    const gUsers = await fetch('http://localhost:8000/users/')
    const users = await gUsers.json();
    return users;
}

const updateUserList = async () => {
    users = await getUsers();
    
    usersList.innerHTML = '';
    users.users.forEach((user) => {
        console.log(user)
        usersList.innerHTML +=`<li>${user.username}</li>`;
    });
}

setInterval(updateUserList(), 100000);