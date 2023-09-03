// logout warning message

document.getElementById('logout-link').addEventListener('click', function (e) {
    e.preventDefault();
    if (confirm("Are you sure you want to logout?")) {
        window.location.href = "{% url 'logout' %}";  
    }
});
