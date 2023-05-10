const nameContainer = document.querySelector('.name-container');

nameContainer.addEventListener('click', (event) => {
    const dropdownOptions = document.querySelector(".dropdown-options");
    dropdownOptions.classList.toggle("show");
    event.stopPropagation();
});

// Close the dropdown menu if the user clicks outside of it
window.onclick = (event) => {
    if (!event.target.matches('.dropdown-item')) {
        const dropdownOptions = document.querySelector(".dropdown-options");
        if (dropdownOptions.classList.contains('show')) {
            dropdownOptions.classList.remove('show');
        }
    }
}

function setNameRole(name, role) {
    const nameContainer = document.querySelector('.user-name');
    const roleContainer = document.querySelector('.user-role');

    const userFirstName = JSON.parse(localStorage.getItem('user_info')).firstName;
    const userLastName = JSON.parse(localStorage.getItem('user_info')).lastName;
    const userRole = JSON.parse(localStorage.getItem('user_info')).role;

    nameContainer.innerHTML = `${userFirstName} ${userLastName}`;
    roleContainer.innerHTML = `${userRole}`;
}

setNameRole();
