import { Stack } from 'office-ui-fabric-react';
import React from 'react';
import { Store, URL } from '../store';

interface gor3aViewProps {
  todos: Store['todos'];
  gor3aId: number;
}

export const Gor3aView = (props: gor3aViewProps) => {
  const { todos, gor3aId } = props;
  const participants = Object.keys(todos).map((id) => todos[id].label);

  return (
    <>
      <Stack>
        <Stack.Item>
          <a href={`/gor3a?id=${gor3aId}`}>Gor3a {gor3aId}</a>
        </Stack.Item>
        {participants.map((participant) => (
          <a href={`${URL}/gor3a/${gor3aId}/${participant}`}>{participant}</a>
        ))}
      </Stack>
    </>
  );
};
