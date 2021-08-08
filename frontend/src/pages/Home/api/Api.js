import axios from 'axios';

export async function putData(data, workerId){
    let user_id = await axios.get(`https://tsmcbot-404notfound.du.r.appspot.com/api/todo/web/${workerId}`)
    await fetch(`https://tsmcbot-404notfound.du.r.appspot.com/api/todo/${user_id.data}`, {
        method: "POST",
        headers: {
            'content-type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify( data )          // convert JS value to JSON string
    })
}

export async function readData(workerId){
    let user_id = await axios.get(`https://tsmcbot-404notfound.du.r.appspot.com/api/todo/web/${workerId}`)
    let result = await fetch(`https://tsmcbot-404notfound.du.r.appspot.com/api/todo/${user_id.data}`)
    .then(j => j.json())

    return result
}

export async function deleteData(workerId, todo_id){
    let user_id = await axios.get(`https://tsmcbot-404notfound.du.r.appspot.com/api/todo/web/${workerId}`)
    await fetch(`https://tsmcbot-404notfound.du.r.appspot.com/api/todo/${user_id.data}/${todo_id}`, {
        method: "DELETE",
        headers: {
            'content-type': 'application/json'
        }
    })
}

export async function modifyData(data, workerId, todo_id){
    let user_id = await axios.get(`https://tsmcbot-404notfound.du.r.appspot.com/api/todo/web/${workerId}`)
    console.log(`https://tsmcbot-404notfound.du.r.appspot.com/api/todo/${user_id.data}/${todo_id}`);
    await fetch(`https://tsmcbot-404notfound.du.r.appspot.com/api/todo/${user_id.data}/${todo_id}`, {
        method: "PUT",
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify( data )
    })
}