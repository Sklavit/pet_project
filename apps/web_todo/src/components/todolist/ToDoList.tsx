import { Container, ToDoItemStyled, ToDoListStyled  }    from './ToDoList.styles'

export const TodoList = () => {


    return (
        <div>
            <Container>Todo List</Container>
            <ToDoListStyled>
                <ToDoItemStyled>Buy Milk</ToDoItemStyled>
                <ToDoItemStyled>Buy Bread</ToDoItemStyled>
                <ToDoItemStyled>Buy Cheese</ToDoItemStyled>
            </ToDoListStyled>
        </div>
    )
}