const ARRAY_MENU = [
    { id: 0, textMenu: "Thông tin của tôi", icon: '<i class="fa-solid fa-house"></i>', to: (id) => `/instructor/${id}/`, role: [0, 1] },
    { id: 1, textMenu: "Diễn đàn", icon: '<i class="fa-solid fa-thumbs-up"></i>', to: (id) => `/forumins/${id}/`, role: [0, 1] },
    { id: 2, textMenu: "Bài viết của tôi", icon: '<i class="fa-sharp fa-solid fa-mailbox"></i>', to: (id) => `/article/${id}/`, role: [0, 1] },
    { id: 3, textMenu: "About Us", icon: '<i class="fa-solid fa-user-tag"></i>', to: (id) => `/aboutusins/${id}/`, role: [0, 1] }
];

function createMenu(user, instructorId) {
    const filteredMenu = ARRAY_MENU.filter(menu => menu.role.includes(user.isRole));

    const menuContainer = document.createElement('div');
    menuContainer.className = 'menu_container';

    const bodyMenu = document.createElement('div');
    bodyMenu.className = 'body_menu';

    filteredMenu.forEach(menu => {
        const itemMenu = document.createElement('a');
        itemMenu.className = 'item_menu';
        itemMenu.href = menu.to(instructorId);
        itemMenu.innerHTML = `${menu.icon} <div class="text_menu">${menu.textMenu}</div>`;
        bodyMenu.appendChild(itemMenu);
    });

    menuContainer.appendChild(bodyMenu);
    return menuContainer;
}

const user = { isRole: 0 }; 
const menu = document.getElementById('menuContainer');
const instructorId = menu.getAttribute("data-instructor-id");

document.getElementById('menuContainer').appendChild(createMenu(user, instructorId));
