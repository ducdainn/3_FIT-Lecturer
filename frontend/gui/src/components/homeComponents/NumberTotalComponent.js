import React from 'react'
import { MdPeopleAlt } from "react-icons/md";
import { MdPostAdd } from "react-icons/md";
import { BsFillThunderboltFill } from "react-icons/bs";

const NumberTotalComponent = () => {

    const ARRAY_LIST_NUMBER_TOTAL = [
        {
            id: 0,
            textTotal: "Tổng số giảng viên",
            number: 14,
            iconTotal: <MdPeopleAlt />,
            dateAt: ""
        },
        {
            id: 1,
            textTotal: "Tổng số bài viết",
            number: 44,
            iconTotal: <MdPostAdd />,
            dateAt: "Updated 3 hour ago"
        },
        {
            id: 2,
            textTotal: "Tổng thành viên",
            number: 99,
            iconTotal: <BsFillThunderboltFill />,
            dateAt: ""
        },
    ]

    return (
        <div className='container_numberTotal'>
            {ARRAY_LIST_NUMBER_TOTAL.map((index) => (
                <div key={index.id} className='item_total_number'>
                    <div>
                        {index.iconTotal}
                    </div>
                    <div>
                        <div className='text_total'>{index.textTotal}</div>
                        <div className='number_total'>{index.number}</div>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default NumberTotalComponent