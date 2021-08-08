import React, { useEffect, useState } from 'react'
import Edit from './components/Edit'
import List from './components/List'
import Loader from './components/Loader/Loader'
import './index.css'
import { readData } from './api/Api'

async function fetchData(setData, workerId){
    const result = await readData(workerId)
    let tmpData = []
    result.forEach(post => {
        tmpData = [
            ...tmpData,
            {
                "todo_id": post.todo_id,
                "todo_name": post.todo_name,
                "todo_date": post.todo_date,
                "todo_update_date": post.todo_update_date,
                "todo_contents": post.todo_contents
            }
        ]
    })
    setData(tmpData)
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
            fetchData(setData, workerId)
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