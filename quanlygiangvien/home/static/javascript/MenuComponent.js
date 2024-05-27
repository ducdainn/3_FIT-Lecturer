const ARRAY_MENU = [
    { id: 0, textMenu: "Quản lý", icon: '<i class="fa-solid fa-house"></i>', to: "/home/", role: [0,1] },
    { id: 1, textMenu: "Diễn đàn", icon: '<i class="fa-solid fa-thumbs-up"></i>', to: "/forumad/", role: [0, 1] },
    { id: 2, textMenu: "About Us", icon: '<i class="fa-solid fa-user-tag"></i>', to: "/aboutus/", role: [0, 1] }
];

function createMenu(user) {
    const filteredMenu = ARRAY_MENU.filter(menu => menu.role.includes(user.isRole));

    const menuContainer = document.createElement('div');
    menuContainer.className = 'menu_container';

    const bodyMenu = document.createElement('div');
    bodyMenu.className = 'body_menu';

    filteredMenu.forEach(menu => {
        const itemMenu = document.createElement('a');
        itemMenu.className = 'item_menu';
        itemMenu.href = menu.to;
        itemMenu.innerHTML = `${menu.icon} <div class="text_menu">${menu.textMenu}</div>`;
        bodyMenu.appendChild(itemMenu);
    });

    menuContainer.appendChild(bodyMenu);
    return menuContainer;
}

const user = { isRole: 0 }; 
document.getElementById('menuContainer').appendChild(createMenu(user));

