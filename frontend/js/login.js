const loginForm = document.querySelector('#login-form');
const email = document.querySelector('#email');
const password = document.querySelector('#password');


loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const response = await fetch('http://127.0.0.1:8000/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email.value,
            password: password.value
        })
    });

    const data = await response.json();
    console.log(data);
    localStorage.setItem('username', data.username);
    window.location.href = './index.html';
    
});