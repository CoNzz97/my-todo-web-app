import streamlit as st
import functions

todos = functions.read_file()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_file(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("Use this app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="todo input",
              label_visibility="hidden",
              placeholder="Add new todo...", on_change=add_todo, key="new_todo")
st.button("Enter")

# st.session_state
