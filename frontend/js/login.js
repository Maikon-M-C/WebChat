const loginForm = document.querySelector('#login-form');
const user = document.querySelector('#username');
const email = document.querySelector('#email');
export let id = 0;


loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const response = await fetch('http://127.0.0.1:8000/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: user.value,
            email: email.value,
            password: 'password' // temporary
        })
    });

    const data = await response.json();
    id = data.id;
    console.log('Logged in with ID:', id);

});
