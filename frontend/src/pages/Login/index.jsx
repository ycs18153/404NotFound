import React, { useState } from 'react';
import './index.css'

let Login = ( {login, setLogin, setWorkerId} ) => {
    const [tempId, setTempId] = useState('')

    function click(){
        if(tempId === '')
            alert("請輸入工號！")
        setWorkerId(tempId)
        setLogin(true)
    }

    return login? null:
        <div id="card-wrap">
            <div id="card">
                <div id="card-content">
                    <div id="card-title">
                        <h2>LOGIN</h2>
                        <div className="underline-title"></div>
                    </div>
                    <div className="form">
                        <label for="user-password">
                            工號：
                        </label>
                        <input id="user-password" className="form-content" type="text" value={tempId} onChange={e => setTempId(e.target.value)}/>
                        <div className="form-border"></div>
                        <button id="submit-btn" onClick={click}>Login</button>
                    </div>
                </div>
            </div>
        </div>
}

export default Login