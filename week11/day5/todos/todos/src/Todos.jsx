import React from 'react';

const Todos = ({todos, deleteTodo}) => {

  //get from localstorage
  //todos = JSON.parse(localStorage.getItem('todos'));

  const todoList = todos.length ? (
    todos.map(todo => {
      return (
        <div className="item" key={todo.id}>
          <span onClick={() => {deleteTodo(todo.id)}}>{todo.content}</span>
        </div>
      )
    })
  ) : (
    <p>You have no todo's left, yay!</p>
  );

  return (
    <div>
      {todoList}
    </div>
  )
}

export default Todos;
