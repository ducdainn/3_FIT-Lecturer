import React from 'react'
import { Outlet } from 'react-router-dom'
import MenuComponent from './MenuComponent'
import HeaderComponent from './HeaderComponent'
// Hàm để truyền data vào routes con

function Layout ({ user , listData }) {
    return (
        <div>
            {user ? <HeaderComponent user={user} /> : ""}
            <div className="body_container">
        
                    {user ? <div> <MenuComponent user={user} /> </div> :""}
     
                <div className="body_page" style={user ? { width: "calc( 100% - 250px )" } : { width: "100%", padding: "0px" }}>
                    <Outlet context = {{ listData}}/>
                </div>
            </div>

        </div>
    );
}

export default Layout