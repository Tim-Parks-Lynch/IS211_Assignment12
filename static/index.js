if(document.querySelector(".button-alert")){
  alertButton = document.querySelector(".button-alert")
  alertDiv = document.querySelector(".div-alert")
  
  alertButton.addEventListener("click", () => {
    alertDiv.classList.toggle("div-stop-alert")
  })
}
