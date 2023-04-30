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
