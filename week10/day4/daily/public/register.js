const registerForm = document.getElementById('registerForm');
registerForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name, lastName, email, username, password })
    });

    //answer from server with text error1 or register
    const result = await response.text();
    const msg = document.querySelector('#registerMessage');

    if (result === 'register') {
      msg.textContent = 'Hello! Your account created successfully'
      msg.textContent = 'Username or password already exists!'
    }
});