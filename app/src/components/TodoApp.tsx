import React from 'react';
import { Stack } from 'office-ui-fabric-react';
import { TodoFooter } from './TodoFooter';
import { TodoHeader } from './TodoHeader';
import { TodoList } from './TodoList';
import { Store, URL } from '../store';
import { Gor3aView } from './Gor3aView';

let index = 0;

export class TodoApp extends React.Component<any, Store> {
  constructor(props: any) {
    super(props);
    this.state = {
      todos: {},
      filter: 'all',
      buttonClicked: false,
      gor3aId: -1,
    };
  }

  render() {
    const { filter, todos, buttonClicked, gor3aId } = this.state;
    return (
      <Stack horizontalAlign="center">
        <Stack style={{ width: 400 }} gap={25}>
          <TodoHeader addTodo={this._addTodo} setFilter={this._setFilter} filter={filter} />
          <TodoList complete={this._complete} todos={todos} filter={filter} remove={this._remove} edit={this._edit} />
          <TodoFooter clear={this._clear} todos={todos} />
          {buttonClicked ? <Gor3aView todos={todos} gor3aId={gor3aId}></Gor3aView> : null}
        </Stack>
      </Stack>
    );
  }

  private _addTodo = (label: any) => {
    const { todos } = this.state;
    const id = index++;

    this.setState({
      todos: { ...todos, [id]: { label } },
    });
  };

  private _remove = (id: string | number) => {
    const newTodos = { ...this.state.todos };
    delete newTodos[id];

    this.setState({
      todos: newTodos,
    });
  };

  private _complete = (id: string | number) => {
    const newTodos = { ...this.state.todos };
    newTodos[id].completed = !newTodos[id].completed;

    this.setState({
      todos: newTodos,
    });
  };

  private _edit = (id: string | number, label: any) => {
    const newTodos = { ...this.state.todos };
    newTodos[id] = { ...newTodos[id], label };

    this.setState({
      todos: newTodos,
    });
  };

  private _clear = () => {
    const { todos } = this.state;
    const participants = Object.keys(todos).map((id) => todos[id].label);

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(participants),
    };

    fetch(`${URL}/gor3a`, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        this.setState({ gor3aId: data.id, buttonClicked: true });
      });
  };

  private _setFilter = (filter: any) => {
    this.setState({
      filter: filter,
    });
  };
}
