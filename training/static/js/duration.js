const newElec = document.getElementById("start-election-btn");
const comfermMenue = document.getElementById("conferm");

newElec.addEventListener("click", (event) => {
  event.preventDefault();

  comfermMenue.style.display = "block";


});



const confirmYesBtn = document.getElementById("yes-btn");

confirmYesBtn.addEventListener("click", () => {
  fetch("/clear_nominees/")
    .then(response => {
        
    })
    .catch(error => {

    });
});

const noComfermation = document.getElementById('no-btn')
noComfermation.addEventListener("click", () => {

    comfermMenue.style.display = "none";


});
  