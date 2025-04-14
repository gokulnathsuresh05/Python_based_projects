from tkinter import *
import os

TASKS_FILE = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x450")

        self.tasks = []

        # Entry for new task
        self.task_entry = Entry(root, width=30, font=('Arial', 14))
        self.task_entry.pack(pady=10)

        # Add button
        Button(root, text="Add Task", width=20, command=self.add_task).pack()

        # Listbox to show tasks
        self.task_listbox = Listbox(root, width=40, height=15, font=('Arial', 12), selectbackground="gray")
        self.task_listbox.pack(pady=10)

        # Buttons
        Button(root, text="Delete Task", width=20, command=self.delete_task).pack(pady=5)
        Button(root, text="Mark as Done", width=20, command=self.mark_done).pack(pady=5)
        Button(root, text="Save Tasks", width=20, command=self.save_tasks).pack(pady=5)

        # Load previous tasks
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, END)

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except:
            pass

    def mark_done(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index] = "✔️ " + self.tasks[index]
            self.update_listbox()
        except:
            pass

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                self.tasks = [line.strip() for line in f]
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            self.task_listbox.insert(END, task)

if __name__ == "__main__":
    root = Tk()
    app = ToDoApp(root)
    root.mainloop()
