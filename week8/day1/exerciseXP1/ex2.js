// 🌟 Exercise 2 : Forms

document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector('form');
    console.log(form);

    var firstNameInput = document.getElementById('fname');
    var lastNameInput = document.getElementById('lname');
    console.log(firstNameInput, lastNameInput);

    var submitButton = document.getElementById('submit');
    submitButton.addEventListener('click', function(event) {
        event.preventDefault();

        var firstNameValue = firstNameInput.value;
        var lastNameValue = lastNameInput.value;

        if (firstNameValue !== '' && lastNameValue !== '') {
            var usersAnswerList = document.querySelector('.usersAnswer');
            var firstNameLi = document.createElement('li');
            var lastNameLi = document.createElement('li');

            firstNameLi.textContent = firstNameValue;
            lastNameLi.textContent = lastNameValue;

            usersAnswerList.appendChild(firstNameLi);
            usersAnswerList.appendChild(lastNameLi);

            firstNameInput.value = '';
            lastNameInput.value = '';
        }
    });
});