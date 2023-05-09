const passwordVisibilityIcon = document.getElementById('show-icon');
const passwordInputField = document.getElementById('password-input-field');

passwordVisibilityIcon.addEventListener('click', () => {
    if (passwordInputField.type === 'password') {
        passwordInputField.type = 'text';
        passwordVisibilityIcon.className = "view-hide";
    } else {
        passwordInputField.type = 'password';
        passwordVisibilityIcon.className = "view-show";
    }
});
const passwordVisibilityIcon2 = document.getElementById('show-icon2');
const passwordInputField2 = document.getElementById('password-input-field2');

passwordVisibilityIcon2.addEventListener('click', () => {
    if (passwordInputField2.type === 'password') {
        passwordInputField2.type = 'text';
        passwordVisibilityIcon2.className = "view-hide";
    } else {
        passwordInputField2.type = 'password';
        passwordVisibilityIcon2.className = "view-show";
    }
});
const passwordVisibilityIcon3 = document.getElementById('show-icon3');
const passwordInputField3 = document.getElementById('password-input-field3');

passwordVisibilityIcon3.addEventListener('click', () => {
    if (passwordInputField3.type === 'password') {
        passwordInputField3.type = 'text';
        passwordVisibilityIcon3.className = "view-hide";
    } else {
        passwordInputField3.type = 'password';
        passwordVisibilityIcon3.className = "view-show";
    }
});
