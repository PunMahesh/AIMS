function validateForm() {
    const form = document.querySelector('#add_equipment');
    const inputs = form.querySelectorAll('input[required], select[required]');
    let isValid = true;
    inputs.forEach((input) => {
      if (!input.value) {
        isValid = false;
        const error = input.nextElementSibling;
        if (error && error.classList.contains('error-msg')) {
          error.textContent = 'This field is required';
        } else {
          input.insertAdjacentHTML('afterend', '<div class="error-msg">This field is required</div>');
        }
      } else {
        const error = input.nextElementSibling;
        if (error && error.classList.contains('error-msg')) {
          error.remove();
        }
      }
    });
    return isValid;
  }
  
  const form = document.querySelector('#add_equipment');
  form.addEventListener('submit', function(event) {
    event.preventDefault();
    const isValid = validateForm();
    if (isValid) {
      // Submit the form
      form.submit();
    } else {
      // Display error message(s)
      const errorContainer = document.querySelector('#error-container');
      errorContainer.innerHTML = '<div class="error-msg">Please fill out all required fields.</div>';
    }
  });