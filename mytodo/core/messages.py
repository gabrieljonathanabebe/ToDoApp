# mytodo/core/messages.py


class ToDoMessage:
    # ===== USER ==============================================================
    @staticmethod
    def user_not_found(username: str) -> str:
        return f'User "{username}" not found.'

    @staticmethod
    def invalid_credentials() -> str:
        return "Invalid username or password."

    @staticmethod
    def welcome_user(username: str) -> str:
        return f"Welcome back, {username}."

    @staticmethod
    def username_already_exists(username: str) -> str:
        return f'Username "{username}" already exists.'

    @staticmethod
    def user_created(username: str) -> str:
        return f'User "{username}" created.'

    # ===== TODO ==============================================================
    @staticmethod
    def todo_not_found() -> str:
        return "To-Do not found."

    @staticmethod
    def todo_created(title: str) -> str:
        return f"{title} created."

    @staticmethod
    def todo_deleted() -> str:
        return "To-Do deleted."

    @staticmethod
    def todo_already_exists(title: str) -> str:
        return f"{title} already exists."

    # ===== TASK ==============================================================
    @staticmethod
    def task_not_found(task_id: str) -> str:
        return f"Task {task_id} not found."

    @staticmethod
    def task_updated(task_id: str) -> str:
        return f"Task {task_id} updated."

    @staticmethod
    def invalid_task_id(task_id: str) -> str:
        return f'"{task_id}" is not a valid task id.'

    @staticmethod
    def task_added(task_id: str) -> str:
        return f"Task {task_id} added."

    @staticmethod
    def task_deleted(task_id: str) -> str:
        return f"Task {task_id} deleted."

    @staticmethod
    def task_status_toggled(task_id: str) -> str:
        return f"Toggle status for Task {task_id}."

    @staticmethod
    def invalid_status(status: str) -> str:
        return f'"{status}" is not a valid status'

    @staticmethod
    def invalid_priority(priority: str) -> str:
        return f'"{priority}" is not a valid Priority'

    @staticmethod
    def task_status_updated(task_id: str, status: str) -> str:
        return f'Task {task_id} status updated to "{status}".'

    @staticmethod
    def task_created(task_id: int) -> str:
        return f"Task {task_id} added."

    @staticmethod
    def invalid_sort_key(key: str) -> str:
        return f"Key {key} not found."

    @staticmethod
    def task_order_updated() -> str:
        return "Task order updated."

    @staticmethod
    def tasks_not_found() -> str:
        return "One or more tasks not found."

    @staticmethod
    def reassigned_task_ids(count: int) -> str:
        return f"Reassigned {count} IDs."
