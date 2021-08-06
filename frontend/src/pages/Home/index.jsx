import React, { useEffect, useState, useRef } from 'react'
import Edit from './components/Edit'
import List from './components/List'
import Loader from './components/Loader/Loader'
import './index.css'
import { readData } from './api/Api'

async function fetchData(setData, workerId, setLoading){
    const result = await readData(workerId)
    setData([])
    result.forEach(post => {
        setData(prev => {
            return [
                ...prev,
                {
                    "todo_id": post.todo_id,
                    "todo_name": post.todo_name,
                    "todo_date": post.todo_date,
                    "todo_update_date": post.todo_update_date,
                    "todo_contents": post.todo_contents
                }
            ]
        })
    })
}

const Home = ( {workerId} ) => {
    // an array to store items
    const [data, setData] = useState([])
    const [refetch, setRefetch] = useState(true)
    const [loading, setLoading] = useState(true)

    // set the title
    useEffect(() => {
        document.title = "Memo"
    })

    // fetch data from db
    useEffect(() => {
        if(refetch){
            setLoading(true)
            fetchData(setData, workerId, setLoading)
            setRefetch(false)
            setLoading(false)
        }
    }, [workerId, refetch])

    return <div className='app'>
        <Edit workerId={workerId} setRefetch={setRefetch} setLoading={setLoading}/>
        {
            loading? 
            <Loader loading={loading}/> : 
            <List listData={data} workerId={workerId} setRefetch={setRefetch} setLoading={setLoading}/>
        }
    </div>
}

export default Home