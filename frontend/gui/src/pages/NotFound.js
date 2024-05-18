import React from 'react'
import image_404 from "../assets/images/404.PNG"

const NotFound = () => {
    return (
        <div style={{ width: "100%" }}>
            <img src={image_404} alt="404" style={{ margin: "100px auto",display:"block" }} />
        </div>
    )
}

export default NotFound