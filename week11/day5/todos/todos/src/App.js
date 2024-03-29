import React, { Component } from 'react';
import Todos from './Todos'
import AddTodo from './AddTodo'

class App extends Component {
  
  state = {
    todos: []
  }

   componentDidMount() {
    localStorage.getItem('todos');
   }

  deleteTodo = (id) => {
    const todos = this.state.todos.filter(todo =>  todo.id !== id);
    localStorage.setItem('todos', JSON.stringify(todos));

    this.setState({
      todos
    });
  }

  addTodo = (todo) => {
    todo.id = Math.random();
    let todos = [...this.state.todos, todo];
    this.setState({
      todos
    });

     localStorage.setItem('todos', JSON.stringify(todos));

  }
  
  
  render() {
    return (
      <div className="todo-app">
        <h1 className="blue-text">Todo's</h1>
        <Todos todos={this.state.todos} deleteTodo={this.deleteTodo} />
        <AddTodo addTodo={this.addTodo} />
      </div>
    );
  }
}

export default App;
