export type FilterTypes = 'all' | 'active' | 'completed';

export const URL = 'http://localhost:8000';
export interface TodoItem {
  label: string;
  completed: boolean;
}

export interface Store {
  todos: {
    [id: string]: TodoItem;
  };

  filter: FilterTypes;
  buttonClicked: boolean;
  gor3aId: number;
}
