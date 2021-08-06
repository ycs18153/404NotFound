import React from 'react';
import Item from './Item'

const List = ({ listData, workerId, setRefetch}) => {
    return <div className='list'>
    {
        listData.map( item => {
            const { todo_name, todo_date , todo_update_date, todo_contents, todo_id } = item       // 解構item，可以設預設值，undifined的時候會回傳預設值
            return(
                <Item 
                    key={todo_id}
                    todo_id={todo_id}
                    todo_name={todo_name}
                    todo_date={todo_date}
                    todo_update_date={todo_update_date}
                    todo_contents={todo_contents}
                    workerId={workerId}
                    setRefetch={setRefetch}
                />
            )
        } )
    }
    </div>
}

export default List