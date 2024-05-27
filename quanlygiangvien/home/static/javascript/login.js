// Lấy tham chiếu đến form đăng nhập
var loginForm = document.getElementById('loginForm');

// Thêm sự kiện submit vào form
loginForm.addEventListener('submit', function(event) {
    // Ngăn chặn hành động mặc định của form
    event.preventDefault();
    
    // Mở modal
    openModal();
});
