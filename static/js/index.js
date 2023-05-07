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
