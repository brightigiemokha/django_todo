// logout warning message

document.getElementById('logout-link').addEventListener('click', function (e) {
    e.preventDefault();
    if (confirm("Are you sure you want to logout?")) {
        window.location.href = "/logout/";  
    }      
});


// Function to hide the messages container after 3 seconds
function hideMessages() {
    var messagesContainer = document.getElementById('messages-container');
    if (messagesContainer) {
      setTimeout(function() {
        messagesContainer.style.display = 'none';
      }, 3000); // 3000 milliseconds (3 seconds)
    }
  }

  // Call the function when the page loads
  window.onload = function() {
    hideMessages();
};