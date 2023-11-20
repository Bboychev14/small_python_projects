import tkinter as tk
from tkinter import messagebox
import datetime
from task import Task


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("To-Do List App")
        self.tasks = []

        self.title_label = tk.Label(root, text="Task Manager", font=("arial", 20))
        self.title_label.pack()

        self.entry_label = tk.Label(root, text="Enter a task", font=("arial", 12))
        self.entry_label.pack()
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()

        self.priority_label = tk.Label(root, text="Priority")
        self.priority_label.pack()
        self.priority_var = tk.StringVar()
        self.priority_var.set("Low")
        self.priority_menu = tk.OptionMenu(root, self.priority_var, "Low", "Medium", "High")
        self.priority_menu.pack()

        self.date_label = tk.Label(root, text="Due Date (YYYY-MM-DD)")
        self.date_label.pack()
        self.date_entry = tk.Entry(root, width=20)
        self.date_entry.pack()

        # Buttons for adding, editing, and removing tasks
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.remind_button = tk.Button(root, text="Remind for Next 3 Days", command=self.remind_next_3_days)
        self.remind_button.pack()

        # Frame for the tasks box
        left_frame = tk.Frame(root)
        left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Title and task listbox on the left
        self.task_listbox_label = tk.Label(left_frame, text="List of Tasks", font=("arial", 15))
        self.task_listbox_label.pack(pady=10)

        self.task_listbox = tk.Listbox(left_frame, width=60, height=20)
        self.task_listbox.pack(padx=10, pady=10)

        # Frame for the reminders box
        right_frame = tk.Frame(root)
        right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # Title and reminders box on the right
        self.reminder_label = tk.Label(right_frame, text="Reminders", font=("arial", 15))
        self.reminder_label.pack(pady=10)

        self.reminder_text = tk.Text(right_frame, height=20, width=60)
        self.reminder_text.pack(padx=10, pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        priority = self.priority_var.get()
        due_date_str = self.date_entry.get()

        try:
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            due_date = None

        if task_text:
            task = Task(task_text, priority, due_date)
            self.tasks.append(task)
            self.update_task_listbox()
            self.clear_input_fields()

            # Checks if the due date is in the past, and creates a reminder immediately if it is
            if due_date and due_date < datetime.date.today():
                self.reminder_text.insert(tk.END, f"- {task.description} (Priority: {task.priority}, "
                                                  f"Due Date: {task.due_date})\n")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            edited_task_text = self.task_entry.get()
            priority = self.priority_var.get()
            due_date = self.date_entry.get()
            try:
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                due_date = None

            if edited_task_text:
                self.tasks[index] = Task(edited_task_text, priority, due_date)
                self.update_task_listbox()
                self.clear_input_fields()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            result = messagebox.askquestion("Confirmation", "Are you sure you want to remove this task?")
            if result == "yes":
                self.tasks.pop(index)
                self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END,
                                     f"{task.description} (Priority: {task.priority}, Due Date: {task.due_date})")

    def clear_input_fields(self):
        self.task_entry.delete(0, tk.END)
        self.priority_var.set("Low")
        self.date_entry.delete(0, tk.END)

    def check_reminders(self):
        today = datetime.date.today()
        self.reminder_text.delete(1.0, tk.END)  # Clear existing reminders
        for task in self.tasks:
            if task.due_date and task.due_date <= today:
                self.reminder_text.insert(tk.END, f"- {task.description} "
                                                  f"(Priority: {task.priority}, Due Date: {task.due_date})\n")

    def move_past_due_tasks_to_reminders(self):
        today = datetime.date.today()
        for task in self.tasks:
            if task.due_date and task.due_date <= today:
                self.reminder_text.insert(tk.END, f"- {task.description} "
                                                  f"(Priority: {task.priority}, Due Date: {task.due_date})\n")

    def remind_next_3_days(self):
        today = datetime.date.today()
        three_days_from_today = today + datetime.timedelta(days=3)

        self.reminder_text.delete(1.0, tk.END)  # Clears existing reminders
        for task in self.tasks:
            if task.due_date and today <= task.due_date <= three_days_from_today:
                self.reminder_text.insert(tk.END, f"- {task.description} "
                                                  f"(Priority: {task.priority}, Due Date: {task.due_date})\n")
