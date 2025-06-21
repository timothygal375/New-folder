function validateForm(event) {
  const theForm = event.target;
  const errors = [];
  let isValid = true;
  if (theForm.paymentMethod.value === "creditCard") {
    if (theForm.creditCard.value !== "1234123412341234") {
      isValid = false; 
      errors.push("Credit card number is invalid."); 
    }
  }
  if (theForm.fullName.value === "Bob") {
    isValid = false; 
    errors.push("Your name is not Bob."); 
  }

  if (!isValid) {
    event.preventDefault();
    showErrors(errors);
    return false;
  }
}

document.querySelector("#checkoutForm").addEventListener("submit", validateForm);

function togglePaymentDetails(e) {
  const theForm = e.target.form; 
  const creditCardContainer = document.getElementById("creditCardContainer"); 
  const paypalContainer = document.getElementById("paypalContainer"); 

  creditCardContainer.classList.add("hide");
  paypalContainer.classList.add("hide");

  theForm.creditCard.required = false;
  theForm.PayPal.required = false;

  if (e.target.value === "creditCard") {
    creditCardContainer.classList.remove("hide");
    theForm.creditCard.required = true;
  } else if (e.target.value === "paypal") {
    paypalContainer.classList.remove("hide");
    theForm.PayPal.required = true;
  }
}
function showErrors(errors) {
  const errorEl = document.querySelector(".errors");
  const html = errors.map((error) => `<p>${error}</p>`);
  errorEl.innerHTML = html.join("");
}