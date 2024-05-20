document.addEventListener("DOMContentLoaded", function() {
    // Lắng nghe sự kiện click vào nút xoá
    var deleteButtons = document.querySelectorAll(".delete-button");
    deleteButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Lấy giá trị của instructor_id từ thuộc tính data-instructor-id của nút xoá
            var instructorId = button.getAttribute("data-instructor-id");
            // Gán giá trị instructor_id vào input hidden trong form xoá
            document.getElementById("instructor_id").value = instructorId;
        });
    });
});