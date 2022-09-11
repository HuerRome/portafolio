
button = document.querySelector(".presentation > ion-icon");
menu = document.querySelector(".presentation2 > div:last-child");

button.addEventListener('click',()=>{
    menu.classList.toggle("active");
})

//--------------botones--------------
/*box1 = document.querySelector(".about");
box2 = document.querySelector(".resume");
box3 = document.querySelector(".projects");
box4 = document.querySelector(".contact");

button1 = document.querySelector(".about1");
button2 = document.querySelector(".resume1");
button3 = document.querySelector(".projects1");
button4 = document.querySelector(".contact1");

button1.addEventListener('click',()=>{
    box1.classList.add("active1");
    box2.classList.add("active2");
    box3.classList.add("active2");
    box4.classList.add("active2");
})

button2.addEventListener('click',()=>{
  box2.classList.add("active1");
  box1.classList.add("active2");
  box3.classList.add("active2");
  box4.classList.add("active2");
})
button3.addEventListener('click',()=>{
  box3.classList.add("active1");
  box2.classList.add("active2");
  box1.classList.add("active2");
  box4.classList.add("active2");
})
button4.addEventListener('click',()=>{
  box4.classList.add("active1");
  box2.classList.add("active2");
  box3.classList.add("active2");
  box1.classList.add("active2");
})*/

//-----------------Menu-----------------
// Get the container element
var btnContainer = document.querySelector(".menu");  
// Get all buttons with class="btn" inside the container
var btns = btnContainer.getElementsByClassName("btn");       
// Loop through the buttons and add the active class to the current/clicked button

for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
//----------------------------------------------------------
var about = document.querySelector(".about")
var resume = document.querySelector(".resume")
var projects = document.querySelector(".projects")
var contact = document.querySelector(".contact")

btns[0].addEventListener("click", function (){
  about.style.setProperty("display", "flex"); 
  about.style.setProperty("flex-direction", "column"); 
  resume.style.setProperty("display", "none");
  projects.style.setProperty("display", "none");
  contact.style.setProperty("display", "none");
})

btns[1].addEventListener("click", function (){
  resume.style.setProperty("display", "flex"); 
  resume.style.setProperty("flex-direction", "column"); 
  about.style.setProperty("display", "none");
  projects.style.setProperty("display", "none");
  contact.style.setProperty("display", "none");
})

btns[2].addEventListener("click", function (){
  projects.style.setProperty("display", "flex"); 
  projects.style.setProperty("flex-direction", "column"); 
  resume.style.setProperty("display", "none");
  about.style.setProperty("display", "none");
  contact.style.setProperty("display", "none");
})

btns[3].addEventListener("click", function (){
  contact.style.setProperty("display", "flex"); 
  contact.style.setProperty("flex-direction", "column"); 
  resume.style.setProperty("display", "none");
  projects.style.setProperty("display", "none");
  about.style.setProperty("display", "none");
})



/*
btns[0].addEventListener("click", function (){
  if (about.className != 'active2'){
    about.classList.add("active2");
    resume.className.replace(" active2", "");
    projects.className.replace(" active2", "");
    contact.className.replace(" active2", "");
  }else{
    about.className.replace("active2", "");
    resume.className.replace(" active2", "");
    projects.className.replace(" active2", "");
    contact.className.replace(" active2", "");
  }
})

btns[1].addEventListener("click", function (){
  if (resume.className != 'active2'){
    resume.classList.add("active2");
    about.className.replace(" active2", "");
    projects.className.replace(" active2", "");
    contact.className.replace(" active2", "");
  }else{
    resume.className.replace("active2", "");
    about.className.replace(" active2", "");
    projects.className.replace(" active2", "");
    contact.className.replace(" active2", "");
  }
})

btns[2].addEventListener("click", function (){
  if (projects.className != 'active2'){
    projects.classList.add("active2");
    resume.className.replace(" active2", "");
    about.className.replace(" active2", "");
    contact.className.replace(" active2", "");
  }else{
    projects.className.replace("active2", "");
    resume.className.replace(" active2", "");
    about.className.replace(" active2", "");
    contact.className.replace(" active2", "");
  }
})

btns[3].addEventListener("click", function (){
  if (contact.className != 'active2'){
    contact.classList.add("active2");
    resume.className.replace(" active2", "");
    projects.className.replace(" active2", "");
    about.className.replace(" active2", "");
  }else{
    contact.className.replace("active2", "");
    resume.className.replace(" active2", "");
    projects.className.replace(" active2", "");
    about.className.replace(" active2", "");
  }
})
*/