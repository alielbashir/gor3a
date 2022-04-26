import React from 'react';
import { Store } from '../store';
import { DefaultButton, Stack, Text } from 'office-ui-fabric-react';

interface TodoFooterProps {
  clear: () => void;
  todos: Store['todos'];
}

export const TodoFooter = (props: TodoFooterProps) => {
  const itemCount = Object.keys(props.todos).filter(id => !props.todos[id].completed).length;

  return (
    <Stack horizontal horizontalAlign="space-between">
      <Text>
        {itemCount} participants
      </Text>
      <DefaultButton onClick={() => props.clear()}>Generate gor3a!</DefaultButton>
    </Stack>
  );
};
