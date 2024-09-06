function validate(event){
    event.preventfault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const age = document.getElementById('age').value;
    const messageBox = document.getElementById('message');

    let message = '';
    if(email === ''){
        message = "Please enter your email";
        messageBox.style.color = "red";
    } else if(password === ''){
        message = "Password must be at least 8 characters";
        messageBox.style.color = "red";
    } else if(age === ''){
        message = "Age must be between 12 and 60";
        messageBox.style.color = "red";
    }
    else {
        message = "LOGIN SUCCESSFUL";
        messageBox.style.color = "green";
    }
    messageBox.innerText = message;
}