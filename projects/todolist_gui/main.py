import streamlit as st
from classes.todolist import TodoList
from classes.task import Task
from classes.storage import Storage


def get_id(todolist: TodoList):
    return len(todolist.tasks) + 1


def main():
    storage = Storage()
    if "todolist" not in st.session_state:
        st.session_state.todolist = storage.read()
    todolist = st.session_state.todolist

    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("TODOLIST")
    with st.expander("ADD TASK"):
        st.header("ADD TASK")
        title = st.text_input("TITLE")
        description = st.text_input("DESCRIPTION")
        priority = st.selectbox("PRIORITY", ["low", "medium", "high"])
        status = st.selectbox("STATUS", ["pending", "completed"])

        if st.button("ADD TASK"):
            task = Task(
                id=get_id(todolist=todolist),
                title=title,
                desc=description,
                priority=priority,  # type:ignore
                status=status,  # type:ignore
            )
            todolist.add(task=task)
            st.success(
                f"Task '{task.title}' with taskID '{task.id}' is created successfully!"
            )
            storage.write(todolist)
    for i, task in enumerate(todolist.tasks, 1):
        with st.expander(f"{task.title}  [{task.status}]"):
            st.write(f"ID:{task.id:0>2}")
            st.write(task.desc)
            st.write(f"PRIORITY : {task.priority}")
            st.write(f"TIME : {task.time}")

            check = st.checkbox("MARK AS DONE", key=f"check_{task.id}")
            if check:
                task.status = "completed"
            else:
                task.status = "pending"
            if st.button("REMOVE", key=f"remove_key_{task.id}"):
                todolist.remove(task_id=task.id)
            with st.expander("UPDATE"):
                title = st.text_input("TITLE", key=f"title_{task.id}")
                description = st.text_input("DESCRIPTION", key=f"desc_{task.id}")
                priority = st.selectbox(
                    "PRIORITY", ["low", "medium", "high"], key=f"priority_{task.id}"
                )
                status = st.selectbox(
                    "STATUS", ["pending", "completed"], key=f"status_{task.id}"
                )
                updates = {
                    "title": title,
                    "desc": description,
                    "priority": priority,
                    "status": status,
                }
                if st.button("UPDATE", key=f"update_{task.id}"):
                    todolist.update(task_id=task.id, updates=updates)
                    storage.write(todolist=todolist)
            st.button("DONE", key=f"btn_{task.id}")


if __name__ == "__main__":
    main()
