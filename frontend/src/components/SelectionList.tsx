import {
  ActionButton,
  DefaultPalette,
  IStackStyles,
  Stack
} from '@fluentui/react';

// Styles definition
const stackStyles: IStackStyles = {
  root: {
    background: DefaultPalette.themeTertiary,
    alignItems: 'center',
    justifyContent: 'center',
    width: 400
  }
};

const SelectionList = () => {
  return (
    <div>
      <Stack styles={stackStyles}>
        <h1>SelectionList</h1>
        <ActionButton>
          <span>Click me</span>
        </ActionButton>
      </Stack>
    </div>
  );
};

export default SelectionList;
