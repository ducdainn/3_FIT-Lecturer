import React, { useEffect, useRef, useState } from 'react'
import logo from '../assets/images/logo.png'
import avt_df from '../assets/images/avt_df.jpg'
import { MdLogout } from "react-icons/md";

import { MdManageAccounts } from "react-icons/md";

const HeaderComponent = ({ user }) => {

    const [dropBoxAccount, setDropBoxAccount] = useState(false);


    let refBoxAccount = useRef();


    useEffect(() => {
        let hanlder = (e) => {
            if (!refBoxAccount.current.contains(e.target))
                setDropBoxAccount(false);
        }
        document.addEventListener("mousedown", hanlder);
        return () => document.removeEventListener("mousedown", hanlder);
    });

    const handleLogout = () => {
        localStorage.removeItem('user');
        window.location.href = '/';
    };


    return (
        <div className='header_container'>
            <div className='logo_image'>
                <a href="/" ><img src={logo} alt="logo" /></a>
            </div>
            <div className='right_line_header'>
                <div className={`render_role ${user.isRole === 0 ? "admin_role" : "gv_role"}`}>
                    {user.isRole == 0 ? "ADMIN" : "GIẢNG VIÊN"}
                </div>


                <div className='account_dropdown' onClick={() => setDropBoxAccount(!dropBoxAccount)}>
                    <img src={avt_df} alt="defaut_avata" className='avt_df' />
                    <div className='name_user_header'>
                        <div> {user.firstname} {user.lastname}</div>
                        <div>MGV : {user.username}</div>
                    </div>
                </div>
                <div className={`box_drop_account ${dropBoxAccount ? "active_drop_box" : "unactive_drop_box"}`} ref={refBoxAccount}>
                    <div className='item_select_acc'>
                        <MdManageAccounts />
                        <div className='text_sl_acc'>Cập nhật thông tin</div>
                    </div>
                    <div className='item_select_acc' onClick={handleLogout}>
                        <MdLogout />
                        <div className='text_sl_acc'>Đăng xuất</div>
                    </div>
                </div>



            </div>
        </div>
    )
}

export default HeaderComponent