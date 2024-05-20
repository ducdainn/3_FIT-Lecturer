function HeaderComponent() {
    const header = document.getElementById("header_component")


    const template = `
        <div class="header">
            <div>
                <h2>TEACH TRACK</h2>
            </div>
            <div class="box_control">
                <div>
                    <i class="fa-sharp fa-solid fa-bell"></i>
                </div>
                <div>
                    <i class="fa-solid fa-envelope"></i>
                </div>
                <div>
                    <i class="fa-solid fa-user"></i>
            
                </div>
            
            </div>
        </div>
    `;
    header.innerHTML = '';
    header.insertAdjacentHTML("beforeend", template);
    // document.addEventListener("DOMContentLoaded", function() {
    //     const userIcon = document.querySelector('.user-icon');
    //     const userDropdown = document.getElementById('user-dropdown');
    
    //     // Thêm sự kiện click vào biểu tượng user
    //     userIcon.addEventListener('click', function() {
    //         // Hiển thị hoặc ẩn dropdown bằng cách thay đổi thuộc tính display
    //         if (userDropdown.style.display === "block") {
    //             userDropdown.style.display = "none";
    //         } else {
    //             userDropdown.style.display = "block";
    //         }
    //     });
    // });
}

HeaderComponent();