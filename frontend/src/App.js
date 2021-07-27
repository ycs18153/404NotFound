import React, { useState, useEffect} from 'react';
import './App.css';
import TodoView from './components/TodoListView';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';




function App() {

  const [todoList, setTodoList] = useState([{}])
  const [title, setTitle] = useState('')
  const [desc, setDesc] = useState('')
  const [user, setUser] = useState('')


  const useStyles = makeStyles((theme) => ({
    container: {
      display: 'flex',
      flexWrap: 'wrap',
    },
    textField: {
      marginLeft: theme.spacing(1),
      marginRight: theme.spacing(1),
      width: '220px',
    },
  }));


  // Read all todos
  useEffect(() => {
    axios.get('http://localhost:8000/api/todo')
      .then(res => {
        setTodoList(res.data)
      })
  });

  // Post a todo
  const addTodoHandler = () => {
    axios.post('http://localhost:8000/api/todo/', {'user':user, 'title': title, 'description': desc })
      .then(res => console.log(res))
    };

    const classes = useStyles();

  return (
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"100%", "backgroundColor":"white", "marginTop":"15px"}} >
      <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">ToDoList Management</h1>
     <div className="card-body">
      <h5 className="card text-white bg-dark mb-3">Add Your Task</h5>
      <span className="card-text">
        <input className="mb-2 form-control titleIn" onChange={event => setUser(event.target.value)} placeholder='User'/>
        <input className="mb-2 form-control titleIn" onChange={event => setTitle(event.target.value)} placeholder='Title'/>
        <input className="mb-2 form-control desIn" onChange={event => setDesc(event.target.value)}   placeholder='Description'/>
        <form className={classes.container} noValidate >
          <TextField
            id="datetime-local"
            label="ToDo Date:"
            type="datetime-local"
            defaultValue="2021-07-25T20:30"
            className={classes.textField}
            InputLabelProps={{
              shrink: true,
            }}
          />
        </form>
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}}  onClick={addTodoHandler}>Add Task</button>
      </span>
      <h5 className="card text-white bg-dark mb-3">Your Tasks</h5>
      <div >
      <TodoView todoList={todoList} />
      </div>
      </div>
    </div>
  );
}

export default App;