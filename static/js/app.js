
//calling nav.html
$(function() {
  $("#nav-placeholder").load("Nav.html");
});

// JavaScript for toggling the sidebar
    function toggleSidebar() {
        const sidebar = document.querySelector('aside');
        const content = document.querySelector('section');
        const nav = document.querySelector('nav');
        const toggleBtn = document.getElementById('toggle-btn');

        if (sidebar.style.left === '-200px') {
        sidebar.style.left = '0';
        content.style.marginLeft = '200px';
        nav.style.marginLeft = '200px';
        toggleBtn.innerText = '✖';
        toggleBtn.style.left = '200px';
        } else {
        sidebar.style.left = '-200px';
        content.style.marginLeft = '0';
        nav.style.marginLeft = '0';
        toggleBtn.innerText = '☰';
        toggleBtn.style.left = '0';
    }
    }
    function login() {
      // In a real-world scenario, you would perform server-side authentication here
      // For simplicity, we'll use a basic client-side check
      var username = document.getElementById('username').value;
      var password = document.getElementById('password').value;

      if (username === 'demo' && password === 'password') {
          // Successful login
          document.getElementById('loginForm').style.display = 'none';
          document.getElementById('logoutBtn').style.display = 'block';
          document.getElementById('userDisplay').innerText = username;
      } else {
          alert('Invalid username or password');
      }
  }

  function logout() {
      // Perform logout actions
      document.getElementById('loginForm').style.display = 'block';
      document.getElementById('logoutBtn').style.display = 'none';
      document.getElementById('username').value = '';
      document.getElementById('password').value = '';
  }