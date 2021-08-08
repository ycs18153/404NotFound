import React, { useState } from 'react';
import { putData } from '../api/Api';

const Edit = ({ workerId, setRefetch, setLoading }) => {
    const [note, setNote] = useState("")
    function noteChange(event){
        setNote(event.target.value)
    }
    const [date, setDate] = useState("")
    function dateChange(event){
        setDate(event.target.value)
    }
    const [time, setTime] = useState("")
    function timeChange(event){
        setTime(event.target.value)
    }
    const [content, setContent] = useState("")
    function contentChange(event){
        setContent(event.target.value)
    }

    
    async function Add(){
        if(note === ""){
            window.alert("請輸入記事！")
            return
        }
        if(date === ""){
            window.alert("請輸入日期！")
            return
        }
        if(time === ""){
            window.alert("請輸入時間！")
            return
        }

        const data = {
            "todo_name": note,
            "todo_date": date + ' ' + time,
            "todo_update_date": date + ' ' + time,
            "todo_contents": content
        }
        //console.log(data);
        //console.log(JSON.stringify({ data }));
        setLoading(true)
        await putData(data, workerId)
        setRefetch(true)
        
        // clear input
        setNote("")
        setDate("")
        setTime("")
        setContent("")
    }

    return <div>
        <h1>{workerId}，你好！</h1>
        <label for="thing">代辦事項：</label>
        <input id="thing" type='text' value={note} onChange={noteChange}/>
        <div><br></br></div>
        <label for="date">日期：</label>
        <input id="date" type='date' value={date} onChange={dateChange}/>
        <div><br></br></div>
        <label for="time">時間：</label>
        <input id="time" type='time' value={time} onChange={timeChange}/>
        <div><br></br></div>
        <label for="content">代辦事項內容：</label>
        <input id="content" type='text' value={content} onChange={contentChange}/>
        <button className='add' onClick={Add}>新增待辦事項</button>
    </div>
}

export default Edit