import axios from 'axios'
import React from 'react'

function TodoItem(props) {
    const deleteTodoHandler = (title) => {
    axios.delete(`http://localhost:8000/api/todo/${title}`)
        .then(res => console.log(res.data)) }

    return (
        <div>
            <p>
                <div>USER: {props.todo.user}</div>
                <span style={{ fontWeight: 'bold, underline', color: 'red'}}>{props.todo.title} : </span> {props.todo.description}
                <button onClick={() => deleteTodoHandler(props.todo.title)} className="btn btn-outline-danger my-1 mx-1" style={{'borderRadius':'40px','padding': '8px', 'width': '100%'}}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default TodoItem;