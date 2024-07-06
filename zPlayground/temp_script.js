const hamBurger = document.querySelector(".toggle-btn");
const hidebar = document.querySelector("#hide-sidebar");


const toggleSidebar = () => {
  document.querySelector("#sidebar").classList.toggle("expand");
};


document.getElementById('chat-button').addEventListener('click', function() {
  var chatPage = document.getElementById('chat');
  var allPages = document.querySelectorAll('.page');
  allPages.forEach(function(page) {
      page.style.display = 'none';
  });
  chatPage.style.display = 'block';
});


hamBurger.addEventListener("click", toggleSidebar);
hidebar.addEventListener("click", toggleSidebar);


// document.addEventListener("DOMContentLoaded", function () {
//     const tooltipHover = document.getElementById("tooltipHover");
//     const tooltipBox = document.getElementById("tooltipBox");

//     tooltipHover.addEventListener("mouseenter", function () {
//         tooltipBox.style.visibility = "visible";
//         tooltipBox.style.opacity = "1";
//     });

//     tooltipHover.addEventListener("mouseleave", function () {
//         tooltipBox.style.visibility = "hidden";
//         tooltipBox.style.opacity = "0";
//     });

//     document.addEventListener("click", function (event) {
//         if (!tooltipHover.contains(event.target)) {
//             tooltipBox.style.visibility = "hidden";
//             tooltipBox.style.opacity = "0";
//         }
//     });
// });
