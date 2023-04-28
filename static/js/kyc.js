const steps = Array.from(document.querySelectorAll("form .step"));
const nextBtn = document.querySelectorAll(".next-btn");
const prevBtn = document.querySelectorAll(".prev-btn");
const finishBtn = document.querySelector(".finish-btn");
const kycForm = document.querySelector("#kycForm");

function getElemById(id) {
  return document.getElementById(id);
}

nextBtn.forEach((button) => {
  button.addEventListener("click", () => {
    changeStep("next");
  });
});

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
  const fullName = `${kycForm.elements.first_name.value} ${kycForm.elements.middle_name.value} ${kycForm.elements.last_name.value}`;
  getElemById("name").textContent = isOnlyWhitespace(fullName) ? "N/A" : fullName;
  getElemById("dob").textContent = kycForm.elements.dob.value || "N/A";
  getElemById("gender").textContent = kycForm.elements.gender.value || "N/A";
  getElemById("marital").textContent = kycForm.elements.marital.value || "N/A";
  getElemById("nationality").textContent = kycForm.elements.nationality.value || "N/A";
  getElemById("residential").textContent = kycForm.elements.residential.value || "N/A";
  getElemById("citizenship-val").textContent = kycForm.elements.citizenship.value || "N/A";
  getElemById("passport-val").textContent = kycForm.elements.passport.value || "N/A";
  getElemById("father").textContent = kycForm.elements.father.value || "N/A";
  getElemById("mother").textContent = kycForm.elements.mother.value || "N/A";
  getElemById("grandfather").textContent = kycForm.elements.grandfather.value || "N/A";
  getElemById("grandmother").textContent = kycForm.elements.grandmother.value || "N/A";
  getElemById("spouse").textContent = kycForm.elements.spouse.value || "N/A";
  getElemById("son").textContent = kycForm.elements.son.value || "N/A";
  getElemById("daughter").textContent = kycForm.elements.daughter.value || "N/A";
  getElemById("country").textContent = kycForm.elements.country.value || "N/A";
  getElemById("district").textContent = kycForm.elements.district.value || "N/A";
  getElemById("province").textContent = kycForm.elements.province.value || "N/A";
  getElemById("municipality").textContent = kycForm.elements.municipality.value || "N/A";
  getElemById("ward_no").textContent = kycForm.elements.ward_no.value || "N/A";
  getElemById("street").textContent = kycForm.elements.street.value || "N/A";
  const pp_photo = kycForm.elements.pp_photo;
  readURL(pp_photo);
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      const pp_render = getElemById("pp-render");
      pp_render.style.height = "150px";
      pp_render.style.width = "150px";
      pp_render.setAttribute('src', e.target.result);
    };

    reader.readAsDataURL(input.files[0]);
  }
}

// check if string is only whitespace
function isOnlyWhitespace(str) {
  return str.trim().length === 0;
}