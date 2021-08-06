import React from 'react';
import { deleteData } from '../api/Api'

const Item = ({ todo_id, todo_name, todo_date, todo_update_date, todo_contents, workerId, setRefetch, setLoading}) => {

    async function del(){
        setLoading(true)
        await deleteData(workerId, todo_id)
        setRefetch(true)
    }

    todo_date = todo_date.replaceAll('-', '/')
    let idx = todo_date.indexOf('T')
    let date = todo_date.slice(0, idx)
    let time = todo_date.slice(idx+1, -3)

    return <div className='item'>
        <div> 
            <h4>待辦事項：{todo_name}</h4>
            <h4>時間：{`${date} (${time})`}</h4>
            <h4>內容：{todo_contents}</h4>
        </div>
        <button className='remove' onClick={del}> Delete </button>
    </div>
}

export default Item