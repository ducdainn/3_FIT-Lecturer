
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//     </div>
//   );
// }

// export default App;
import React, { useCallback, useEffect, useState } from "react";
import { Navigate, Route, Routes, useNavigate } from "react-router-dom";
import HomePage from "./pages/HomePage";
import Login from "./pages/Login";
import NotFound from "./pages/NotFound";
import ForumPage from "./pages/ForumPage";
import MyPostPage from "./pages/MyPostPage";
import DocumentPage from "./pages/DocumentPage";
import AboutUsPage from "./pages/AboutUsPage";
import Layout from "./components/Layout";
import axios from 'axios'


function App() {

  const [user, setUser] = useState(() => {
    const storedUser = localStorage.getItem('user');
    return storedUser ? JSON.parse(storedUser) : null;
  });
  const [listData, setListData] = useState([]);
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/")
      .then(res => {
        setListData(res.data);
      })
      .catch(error => console.log(error));
  }, []);
  const handleLogin = (user) => {
    setUser(user);
    localStorage.setItem('user', JSON.stringify(user));
  };


  return (
    <>
      <Routes>
        
        <Route path="/login" element={<Login onLogin={handleLogin} user123={user}/>} />
        <Route path="*" element={<Navigate to="/login" />} />

        <Route path="/" element={user ? <Layout user={user} listData={listData} /> : <Login onLogin={handleLogin} />}>
          {user?.isRole === 0 ? <Route index path="/manager" element={<HomePage />} /> : ""}
          <Route index path="/forum" element={<ForumPage />} />
          <Route index element={user?.isRole === 0 ? <Navigate to="/manager"/> : <Navigate to="/forum"/>}/>
          <Route path="/my-post" element={<MyPostPage />} />
          <Route path="/document" element={<DocumentPage />} />
          <Route path="/about-us" element={<AboutUsPage />} />
          <Route path="*" element={<NotFound />} />
        </Route>


      </Routes>
    </>
  );
}

export default App;
