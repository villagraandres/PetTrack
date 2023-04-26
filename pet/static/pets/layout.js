
document.addEventListener('DOMContentLoaded',()=>{
    const menuBtn = document.querySelector(".menu-btn");
    const menu = document.querySelector(".menu");
    console.log('das');
    menuBtn.addEventListener("click", function() {
      if (menu.style.display === "block") {
        menu.style.display = "none";
      } else {
        menu.style.display = "block";
      }
    });
})
