import React from 'react'
import { Link } from 'react-router-dom'

const ForumItem = ({imgPost, link, textPost, hashtag, author, answered}) => {
    return (
        <div className='item_forum' >
            <div className='img_forum'>
                <img src={imgPost} alt="image" />
            </div>
            <div className='flex_column'>
                <Link to={link} className='text_post'>
                    {textPost}
                </Link>
                <div className='line_hashtag'>
                    {hashtag.map((tag)=>(<Link>#{tag}</Link>))}
                    
                </div>
                <div className='line_author'>
                    <div>Đăng bởi <span style={{fontWeight:"600"}}>{author}</span></div>
                    <div>Có {answered} lượt trả lời</div>
                </div>
            </div>
        </div>
    )
}

export default ForumItem