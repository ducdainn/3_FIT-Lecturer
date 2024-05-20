function MenuComponent() {
    const menu = document.getElementById("menuIntructor_component");
    // dùng id của giảng viên được truyền từ server
    const instructorId = menu.getAttribute("data-instructor-id");


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
                <span>Bài báo của bạn</span>
            </a>

            <a href="/forumins/${instructorId}/" id="a_qlgv">
                <i class="fa-solid fa-business-time"></i>
                <span>Diễn đàn</span>
            </a>

        </div>
    </div>
    `;
    menu.insertAdjacentHTML("beforeend", template);
}

MenuComponent();
