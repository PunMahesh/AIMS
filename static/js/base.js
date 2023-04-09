const nameContainer = document.querySelector('.name-container');

nameContainer.addEventListener('click', () => {
    const dropdownOptions = document.querySelector(".dropdown-options");
    dropdownOptions.classList.toggle("show");
});
