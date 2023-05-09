const steps = Array.from(document.querySelectorAll("form .step"));
const nextBtn = document.querySelectorAll(".next-btn");
const prevBtn = document.querySelectorAll(".prev-btn");
const finishBtn = document.querySelector(".finish-btn");
const kyc_form = document.querySelector("#kyc_form");

function getElemById(id) {
  return document.getElementById(id);
}

nextBtn.forEach((button) => {
  button.addEventListener("click", () => {
    if (validateCurrentStep()) {
      changeStep("next");
    }  
  });
});

function validateCurrentStep() {
  const currentStep = document.querySelector(".step.active");
  const inputs = currentStep.querySelectorAll("input[required], select[required], input[type='radio'][required]");
  let isValid = true;
  inputs.forEach((input) => {
    if (input.type === "radio") {
      const name = input.getAttribute("name");
      const radios = currentStep.querySelectorAll(`input[type='radio'][name='${name}']`);
      if (!Array.from(radios).some((radio) => radio.checked)) {
        isValid = false;
        const error = input.parentElement.querySelector(".error-msg");
        if (error) {
          error.textContent = "This field is required";
        } else {
          input.insertAdjacentHTML("afterend", '<div class="error-msg">This field is required</div>');
        }
      } else {
        const error = input.parentElement.querySelector(".error-msg");
        if (error) {
          error.remove();
        }
      }
    } else {
      if (!input.value) {
        isValid = false;
        const error = input.nextElementSibling;
        if (error && error.classList.contains("error-msg")) {
          error.textContent = "This field is required";
        } else {
          input.insertAdjacentHTML("afterend", '<div class="error-msg">This field is required</div>');
        }
      } else {
        const error = input.nextElementSibling;
        if (error && error.classList.contains("error-msg")) {
          error.remove();
        }
      }
    }
  });
  return isValid;
}

prevBtn.forEach((button) => {
  button.addEventListener("click", () => {
    changeStep("prev");
  });
});

function changeStep(btn) {
  let index = 0;
  const active = document.querySelector(".active");
  index = steps.indexOf(active);
  steps[index].classList.remove("active");
  if (btn === "next") {
    index++;
  } else if (btn === "prev") {
    index--;
  }
  steps[index].classList.add("active");
}


finishBtn.addEventListener("click", (e) => {
  e.preventDefault();
  const fullName = `${kyc_form.elements.first_name.value} ${kyc_form.elements.MiddleName.value} ${kyc_form.elements.Last_name.value}`;
  getElemById("name-preview").textContent = isOnlyWhitespace(fullName) ? "N/A" : fullName;
  getElemById("Dob-preview").textContent = kyc_form.elements.Dob.value || "N/A";
  getElemById("Gender-preview").textContent = kyc_form.elements.Gender.value || "N/A";
  getElemById("MaritualStatus-preview").textContent = kyc_form.elements.MaritualStatus.value || "N/A";
  getElemById("Nationality-preview").textContent = kyc_form.elements.Nationality.value || "N/A";
  getElemById("Residential-preview").textContent = kyc_form.elements.Residential.value || "N/A";
  getElemById("Citizenship-preview").textContent = kyc_form.elements.Citizenship.value || "N/A";
  getElemById("Passport-preview").textContent = kyc_form.elements.Passport.value || "N/A";
  getElemById("FatherName-preview").textContent = kyc_form.elements.FatherName.value || "N/A";
  getElemById("MotherName-preview").textContent = kyc_form.elements.MotherName.value || "N/A";
  getElemById("GrandfatherName-preview").textContent = kyc_form.elements.GrandfatherName.value || "N/A";
  getElemById("GrandMotherName-preview").textContent = kyc_form.elements.GrandMotherName.value || "N/A";
  getElemById("SpouseName-preview").textContent = kyc_form.elements.SpouseName.value || "N/A";
  getElemById("SonName-preview").textContent = kyc_form.elements.SonName.value || "N/A";
  getElemById("DaughterName-preview").textContent = kyc_form.elements.DaughterName.value || "N/A";
  getElemById("Country-preview").textContent = kyc_form.elements.Country.value || "N/A";
  getElemById("District-preview").textContent = kyc_form.elements.District.value || "N/A";
  getElemById("Province-preview").textContent = kyc_form.elements.Province.value || "N/A";
  getElemById("Municipality-preview").textContent = kyc_form.elements.Municipality.value || "N/A";
  getElemById("WardNo-preview").textContent = kyc_form.elements.WardNo.value || "N/A";
  getElemById("Street-preview").textContent = kyc_form.elements.Street.value || "N/A";
  const pp_photo = kyc_form.elements.PassportPhoto;
  readURL(pp_photo);
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      const pp_render = getElemById("pp_photo");
      pp_render.style.height = "150px";
      pp_render.style.width = "150px";
      pp_render.style.objectFit = "cover";
      pp_render.setAttribute('src', e.target.result);
    };

    reader.readAsDataURL(input.files[0]);
  }
}

// check if string is only whitespace
function isOnlyWhitespace(str) {
  return str.trim().length === 0;
}


// function validateCurrentStep() {
//   const currentStep = document.querySelector(".step.active");
//   const inputs = currentStep.querySelectorAll("input[required], select[required]");
//   let isValid = true;
//   inputs.forEach((input) => {
//     if (!input.value) {
//       isValid = false;
//       input.insertAdjacentHTML('afterend', '<div class="error-msg">This field is required</div>');
//     } else {
//       const error = input.nextElementSibling;
//       if (error && error.classList.contains("error-msg")) {
//         error.remove();
//       }
//     }   
//   });
//   return isValid;
// }