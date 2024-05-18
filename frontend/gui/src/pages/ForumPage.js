import React from 'react'
import ForumItem from '../components/ForumComponents/ForumItem'
import CreateForum from '../components/ForumComponents/CreateForum'

import img from "../assets/images/learn-python.webp"

const ForumPage = () => {

    const ARRAY_LIST_POST = [
        {
            id: 0,
            imgPost: img,
            link: "",
            textPost: "Parsing aTimeLogger Android app data to graphs using pandas  graphs using pandas...",
            hashtag: ["python", "fixbug"],
            author: "Trần Văn Quyến",
            answered: 43
        },
        {
            id: 1,
            imgPost: img,
            link: "",
            textPost: "Những vấn để về đăng ký tài khoản github",
            hashtag: ["python", "git", "github"],
            author: "Nguyễn Văn Phong",
            answered: 12
        },
        {
            id: 2,
            imgPost: img,
            link: "",
            textPost: "Parsing aTimeLogger An Parsing aTimeLogger An Parsing aTimeLogger An..",
            hashtag: ["git", "hello"],
            author: "Nguyễn Văn Phong",
            answered:63
        },
        {
            id: 3,
            imgPost: img,
            link: "",
            textPost: "Timr An Parsing aTimeLogger An Parsing aTimeLogger An..",
            hashtag: ["zit", "bug"],
            author: "Nguyễn Văn Phong",
            answered:1
        },
    ]



    return (
        <div className="container_forum">
            <CreateForum />
            <div className='td_heading'>BÀI VIẾT MỚI NHẤT</div>
            {ARRAY_LIST_POST.map((post) => (
                <ForumItem
                    key={post.id}
                    imgPost={post.imgPost}
                    link={post.link}
                    textPost={post.textPost}
                    hashtag={post.hashtag}
                    author={post.author}
                    answered={post.answered}
                />
            ))}
        </div>
    )
}

export default ForumPage