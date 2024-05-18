import React, { useEffect } from 'react'
import NumberTotalComponent from '../components/homeComponents/NumberTotalComponent'
import { useNavigate } from 'react-router-dom'
import ManagerUser from '../components/homeComponents/ManagerUser'

const HomePage = () => {

    return (
        <div>
            <NumberTotalComponent />
            <ManagerUser/>
        </div>
    )
}

export default HomePage