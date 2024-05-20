function MenuComponent() {
    const menu = document.getElementById("menu_component")
    const template = `
    <div class="box_menu_container">
        <div class="menu_body">
            <a href="/home/" id="a_home">
                <i class="fa-regular fa-house-heart"></i>
                <span>Trang Chủ</span>
            </a>

            <a href="/instmanage/" id="a_qlgv">
                <i class="fa-solid fa-business-time"></i>
                <span>Giảng Viên</span>
            </a>

            <a href="/forumad/" id="a_tk">
                <i class="fa-solid fa-business-time"></i>
                <span>Diễn đàn</span>
            </a>

        </div>
    </div>
    
    `;
    menu.insertAdjacentHTML("beforeend", template);
}
MenuComponent();