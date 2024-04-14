import streamlit as st
import functions

todo_list = functions.get_todo_list()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todo_list.append(todo)
    functions.write_todo_list(todo_list)



st.title("My To-Do App")
st.subheader("This is my to-do app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        functions.write_todo_list(todo_list)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a to-do: ", placeholder="Add new to-do...", 
              on_change=add_todo, key="new_todo")