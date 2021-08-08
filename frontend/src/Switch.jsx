import React, { useEffect, useState } from 'react';
import Home from './pages/Home'
import Login from './pages/Login'

let Switch = () => {
    const [login, setLogin] = useState(false)
    const [workerId, setWorkerId] = useState('')

    useEffect(() => {
        console.log(workerId);
    }, [workerId])

    return (login)?
    <Home workerId={workerId}/>:
    <Login login={login} setLogin={setLogin} setWorkerId={setWorkerId} />
}

export default Switch