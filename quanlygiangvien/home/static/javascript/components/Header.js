function HeaderComponent() {
    const header = document.getElementById("header_component");

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
                <div class="logout">
                    <i class="fa-solid fa-user"></i>
                </div>
            </div>
        </div>
    `;
    header.innerHTML = '';
    header.insertAdjacentHTML("beforeend", template);

    // Lắng nghe sự kiện click vào phần tử có class "logout"
    const logoutButton = document.querySelector(".logout");
    logoutButton.addEventListener("click", function() {
        // Thực hiện các thao tác khi người dùng click vào nút đăng xuất
        // Ví dụ: chuyển hướng đến trang đăng xuất
        window.location.href = "/login/";
        console.log("Đã click vào nút đăng xuất");
    });
}

HeaderComponent();
