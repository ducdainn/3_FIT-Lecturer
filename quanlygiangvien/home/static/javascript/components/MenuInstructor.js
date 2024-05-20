function MenuComponent() {
    const menu = document.getElementById("menuIntructor_component");
    const instructorId = "GV00001";  // Thay thế bằng ID thực tế của giảng viên nếu có

    const template = `
    <div class="box_menu_container">
        <div class="menu_body">
            <a href="/instructor/${instructorId}/" id="a_home">
                <i class="fa-regular fa-house-heart"></i>
                <span>Tài khoản</span>
            </a>


            <a href="/articlepost/" id="a_st">
                <i class="fa-solid fa-business-time"></i>
                <span>Đăng bài</span>
            </a>

            <a href="/article/${instructorId}/" id="a_tk">
                <i class="fa-solid fa-business-time"></i>
                <span>Diễn đàn</span>
            </a>

            <a href="" id="a_qlgv">
                <i class="fa-solid fa-business-time"></i>
                <span>Thông báo</span>
            </a>

        </div>
    </div>
    `;
    menu.insertAdjacentHTML("beforeend", template);
}

MenuComponent();
