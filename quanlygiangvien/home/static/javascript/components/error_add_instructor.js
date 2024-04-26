document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('.form2').addEventListener('submit', function(event) {
        var avtInput = document.getElementById('avt');
        var nameInput = document.getElementById('name_add');
        var genderInput = document.getElementById('gender_add');
        var birthInput = document.getElementById('birthdate_add');
        var phoneInput = document.getElementById('phone_add');
        var placeInput = document.getElementById('placeoforigin_add');
        var emailInput = document.getElementById('email_add');
        var departmentInput = document.getElementById('department_add');
        var educationInput = document.getElementById('education_add');
        var positionInput = document.getElementById('position_add');
        var statusInput = document.getElementById('status_add');
        //Thêm các trường dữ liệu khác cần kiểm tra
        
        var errorMessages = {};
        
        // Kiểm tra trường avatar
        if (avtInput.value.trim() === '') {
            errorMessages['avt'] = "Vui lòng cung cấp avatar.";
        }
        
        // Kiểm tra trường tên
        if (nameInput.value.trim() === '') {
            errorMessages['name'] = "Vui lòng nhập tên.";
        }
        if (genderInput.value.trim() === '') {
            errorMessages['gender'] = "Vui lòng nhập giới tính.";
        }
        if (birthInput.value.trim() === '') {
            errorMessages['birthdate'] = "Vui lòng nhập ngày sinh.";
        }
        if (phoneInput.value.trim() === '') {
            errorMessages['phone'] = "Vui lòng nhập phone.";
        }
        if (placeInput.value.trim() === '') {
            errorMessages['placeoforigin'] = "Vui lòng nhập nơi sinh.";
        }
        if (emailInput.value.trim() === '') {
            errorMessages['email'] = "Vui lòng nhập email.";
        }
        if (departmentInput.value.trim() === '') {
            errorMessages['department'] = "Vui lòng nhập khoa.";
        }
        if (educationInput.value.trim() === '') {
            errorMessages['education'] = "Vui lòng nhập học vị.";
        }
        if (positionInput.value.trim() === '') {
            errorMessages['position'] = "Vui lòng nhập chức vụ.";
        }
        if (statusInput.value.trim() === '') {
            errorMessages['status'] = "Vui lòng nhập trạng thái.";
        }
        // Thêm các kiểm tra cho các trường dữ liệu khác
        
        // Nếu có lỗi, ngăn chặn việc gửi form và hiển thị thông báo lỗi
        if (Object.keys(errorMessages).length > 0) {
            event.preventDefault(); // Ngăn chặn việc gửi form
            for (var field in errorMessages) {
                var errorMessage = errorMessages[field];
                var errorElement = document.querySelector('.error-' + field);
                if (errorElement) {
                    errorElement.innerHTML = errorMessage;
                }
            }
        }
    });
});