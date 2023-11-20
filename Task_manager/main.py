import tkinter as tk
from task_manager import TaskManager


def main():
    root = tk.Tk()
    app = TaskManager(root)

    app.move_past_due_tasks_to_reminders()
    root.after(86400000, app.move_past_due_tasks_to_reminders)
    root.mainloop()


if __name__ == "__main__":
    main()
