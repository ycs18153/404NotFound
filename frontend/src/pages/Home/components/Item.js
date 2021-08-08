import React, { useState } from 'react';
import { deleteData, modifyData } from '../api/Api'

const Item = ({ todo_id, todo_name, todo_date, todo_update_date, todo_contents, workerId, setRefetch, setLoading}) => {
    // change format fot date and time
    let idx = todo_date.indexOf('T')
    let date = todo_date.slice(0, idx)
    let time = todo_date.slice(idx+1, -3)

    // for modifying
    const [isModify, setIsModify] = useState(false)
    const [todoName, setTodoName] = useState(todo_name)
    const [todoDate, setTodoDate] = useState(date)
    const [todoTime, setTodoTime] = useState(time)
    const [todoContent, setTodoContent] = useState(todo_contents)

    async function del(){
        setLoading(true)
        await deleteData(workerId, todo_id)
        setRefetch(true)
    }

    async function modify(){
        setIsModify(true)
    }

    async function confirmModify(){
        setLoading(true)
        let data = {
            "todo_name": todoName,
            "todo_date": todoDate + ' ' + todoTime,
            "todo_update_date": todoDate + ' ' + todoTime,
            "todo_contents": todoContent
        }
        console.log(data);
        await modifyData(data, workerId, todo_id)
        setIsModify(false)
        setRefetch(true)
    }

    function cancelModify(){
        setIsModify(false)
        setTodoName(todo_name)
        setTodoDate(date)
        setTodoTime(time)
        setTodoContent(todo_contents)
    }

    return (isModify)?
    (
        <div className='item'>
            <div> 
                <h4>待辦事項：<input className="modify-input" type='text' value={todoName} onChange={e => setTodoName(e.target.value)}></input></h4>
                <h4>時間：
                    <input className="modify-date" type='date' value={todoDate} onChange={e => setTodoDate(e.target.value)}></input>
                    <input className="modify-time" type='time' value={todoTime} onChange={e => setTodoTime(e.target.value)}></input>
                </h4>
                <h4>內容：<input className="modify-content" type='text' value={todoContent} onChange={e => setTodoContent(e.target.value)}></input></h4>
                <button id="confirm-modify" onClick={confirmModify}> 確認 </button>
                <button id="cancel-modify" onClick={cancelModify}> 取消 </button>
            </div>
            <div>
                <button className='modify' onClick={modify}> 修改 </button>
                <button className='remove' onClick={del}> 刪除 </button>
            </div>
        </div>
    )
    :
    (
        <div className='item'>
            <div> 
                <h4>待辦事項：{todo_name}</h4>
                <h4>時間：{`${date} (${time})`}</h4>
                <h4>內容：{todo_contents}</h4>
            </div>
            <div>
                <button className='modify' onClick={modify}> 修改 </button>
                <button className='remove' onClick={del}> 刪除 </button>
            </div>
        </div>
    )
}

export default Item