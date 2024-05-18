import React from 'react'
import { GoHomeFill } from "react-icons/go";
import { NavLink } from "react-router-dom";
import { MdForum } from "react-icons/md";
import { MdManageAccounts } from "react-icons/md";
import { BsFileEarmarkPost } from "react-icons/bs";
import { IoDocumentSharp } from "react-icons/io5";
import { MdLiveHelp } from "react-icons/md";

const ARRAY_MENU = [
    {
        id: 0,
        textMenu: "Q. Lý Giảng Viên",
        icon: <GoHomeFill />,
        to: "/manager",
        role: [0]
    },
    {
        id: 1,
        textMenu: "Diễn đàn",
        icon: <MdForum />,
        to: "/forum",
        role: [0, 1]
    },
    {
        id: 3,
        textMenu: "Bài viết của tôi",
        icon: <BsFileEarmarkPost />,
        to: "/my-post",
        role: [1]
    },
    {
        id: 4,
        textMenu: "Tài liệu",
        icon: <IoDocumentSharp />,
        to: "/document",
        role: [0, 1]
    },
    {
        id: 5,
        textMenu: "Về chúng tôi",
        icon: <MdLiveHelp />,
        to: "/about-us",
        role: [0, 1]
    },
]


const MenuComponent = ({ user }) => {

    const filteredMenu = ARRAY_MENU.filter(menu => menu.role.includes(user.isRole));

    return (
        <div className='menu_container'>
            <div className='body_menu'>
                {filteredMenu.map((menu) => (
                    <NavLink className='item_menu' key={menu.id} to={menu.to}>
                        {menu.icon}
                        <div className='text_menu'>{menu.textMenu}</div>
                    </NavLink>
                ))}
            </div>
        </div>
    )
}

export default MenuComponent