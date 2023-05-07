const dropdownItems = document.querySelectorAll('.dropdown-item');
const dropdowns = document.querySelectorAll(".dropdown-options");

dropdownItems.forEach((dropdownItem, index) => {
    dropdownItem.addEventListener('click', (event) => {
        dropdowns[index].classList.toggle("show");
        event.stopPropagation();
    });
});

// Close the dropdown menu if the user clicks outside of it
window.onclick = (event) => {
    if (!event.target.matches('.dropdown-item')) {
        dropdowns.forEach(dropdown => {
            if (dropdown.classList.contains('show')) {
                dropdown.classList.remove('show');
            }
        });
    }
}