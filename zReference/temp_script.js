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
