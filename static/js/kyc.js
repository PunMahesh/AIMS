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
          error.textContent = "Please select an option.";
        } else {
          input.insertAdjacentHTML("afterend", '<div class="error-msg">Please select an option.</div>');
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
  getElemById("name_preview").textContent = isOnlyWhitespace(fullName) ? "N/A" : fullName;
  getElemById("Dob_preview").textContent = kyc_form.elements.Dob.value || "N/A";
  getElemById("Gender_preview").textContent = kyc_form.elements.Gender.value || "N/A";
  getElemById("MaritualStatus_preview").textContent = kyc_form.elements.MaritualStatus.value || "N/A";
  getElemById("Nationality_preview").textContent = kyc_form.elements.Nationality.value || "N/A";
  getElemById("Residential_preview").textContent = kyc_form.elements.Residential.value || "N/A";
  getElemById("Citizenship_preview").textContent = kyc_form.elements.Citizenship.value || "N/A";
  getElemById("Passport_preview").textContent = kyc_form.elements.Passport.value || "N/A";
  getElemById("FatherName_preview").textContent = kyc_form.elements.FatherName.value || "N/A";
  getElemById("MotherName_preview").textContent = kyc_form.elements.MotherName.value || "N/A";
  getElemById("GrandfatherName_preview").textContent = kyc_form.elements.GrandfatherName.value || "N/A";
  getElemById("GrandMotherName_preview").textContent = kyc_form.elements.GrandMotherName.value || "N/A";
  getElemById("SpouseName_preview").textContent = kyc_form.elements.SpouseName.value || "N/A";
  getElemById("SonName_preview").textContent = kyc_form.elements.SonName.value || "N/A";
  getElemById("DaughterName_preview").textContent = kyc_form.elements.DaughterName.value || "N/A";
  getElemById("Country_preview").textContent = kyc_form.elements.Country.value || "N/A";
  getElemById("Province_preview").textContent = kyc_form.elements.Province.value || "N/A";
  getElemById("District_preview").textContent = kyc_form.elements.District.value || "N/A";
  getElemById("Municipality_preview").textContent = kyc_form.elements.Municipality.value || "N/A";
  getElemById("WardNo_preview").textContent = kyc_form.elements.WardNo.value || "N/A";
  getElemById("Street_preview").textContent = kyc_form.elements.Street.value || "N/A";
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