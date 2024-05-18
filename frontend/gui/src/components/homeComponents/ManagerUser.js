import React, { useState } from 'react';
import { ARRAY_LIST } from '../../DATA_TEST';
import { FaPen } from "react-icons/fa";
import { MdDelete } from "react-icons/md";
import avt from "../../assets/images/girt.PNG";
import { Modal, Popconfirm } from 'antd';
import { useOutletContext } from 'react-router-dom';



const ManagerUser = () => {
    const [openModal, setOpenModal] = useState(false);
    const [selectedUser, setSelectedUser] = useState(null);
    const {listData} = useOutletContext(); // thêm listdataa từ api
    return (
        <div className='container_mg'>
            <div className='text_mg'>Quản lý giảng viên</div>
            <div className='body_table'>
                <div>

                </div>
                <div className='table_container'>
                    <table >
                        <thead>
                            <tr className='header_tb'>
                                <td>#</td>
                                <td>AVATAR</td>
                                <td>MGV</td>
                                <td>HỌ TÊN</td>
                                <td>TRẠNG THÁI</td>
                                <td style={{ textAlign: "right", fontWeight: "700" }}>ACTION</td>
                            </tr>
                        </thead>
                        
                        <tbody>
                            {(ARRAY_LIST.filter(user => user.isRole === 1)).map((user, index) => (
                                <tr key={index}>
                                    <td>{index + 1}.</td>
                                    <td><img src={avt} /></td>
                                    <td>{user.username}</td>
                                    <td> {user.firstname} {user.lastname}</td>
                                    <td>{user.isWork ? <div className='nl'> Nghỉ làm</div> : <div className='dl'>Đang làm</div>}</td>
                                    <td style={{ textAlign: "right" }}>
                                        <button className='btn_act btn_upd'
                                            onClick={() => {
                                                setSelectedUser(user);
                                                setOpenModal(true);
                                            }
                                            }>
                                            <FaPen />
                                        </button>

                                        <Popconfirm
                                            placement="topRight"
                                            title={"XOÁ GIẢNG VIÊN CÓ MGV : " + user.username}
                                            okText="Yes"
                                            cancelText="No"
                                        // onConfirm={}
                                        >
                                            <button className='btn_act btn_del'><MdDelete /></button>
                                        </Popconfirm>


                                    </td>
                                </tr>
                            ))}
                            <Modal
                                title="THÔNG TIN CHI TIẾT GIẢNG VIÊN"
                                centered
                                open={openModal}
                                onOk={() => setOpenModal(false)}
                                onCancel={() => {
                                    setSelectedUser(null);
                                    setOpenModal(false);
                                }}
                                width={1200}
                                okText="LƯU"
                            >
                                {selectedUser && (
                                    <>

                                        <h2>{selectedUser.username}</h2>
                                        <p>Họ và tên: {selectedUser.firstname} {selectedUser.lastname}</p>
                                    </>
                                )}
                            </Modal>
                        </tbody>
                    </table>
                </div>
            </div>





        </div>
    )
}

export default ManagerUser