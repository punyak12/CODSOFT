import tkinter as tk


class Task:
    def __init__(self, description, status="Active"):
        self.description = description
        self.status = status


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task.description} - {task.status}")

    def update_status(self, task_index, new_status):
        self.tasks[task_index - 1].status = new_status

    def save_to_text_file(self, filename="todo_list.txt"):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.description} - {task.status}\n")

    def load_from_text_file(self, filename="todo_list.txt"):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    description, status = line.strip().rsplit(' - ', 1)
                    task = Task(description, status)
                    self.tasks.append(task)
        except FileNotFoundError:
            pass


class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("400x300")  # Set the initial size of the window

        # Add a heading
        self.heading_label = tk.Label(self.master, text="To-do list using Python", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        self.todo_list = ToDoList()
        self.todo_list.load_from_text_file()  # Load tasks from file on startup

        self.task_entry = tk.Entry(self.master)
        self.task_entry.pack()

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.display_button = tk.Button(self.master, text="Display Tasks", command=self.display_tasks)
        self.display_button.pack()

        self.update_button = tk.Button(self.master, text="Update Task Status", command=self.update_status)
        self.update_button.pack()

        self.save_button = tk.Button(self.master, text="Save To-Do List", command=self.save_to_text_file)
        self.save_button.pack()

    def add_task(self):
        description = self.task_entry.get()
        task = Task(description)
        self.todo_list.add_task(task)
        self.task_entry.delete(0, tk.END)

    def display_tasks(self):
        task_display = tk.Toplevel(self.master)
        for index, task in enumerate(self.todo_list.tasks, start=1):
            tk.Label(task_display, text=f"{index}. {task.description} - {task.status}").pack()

    def update_status(self):
        update_window = tk.Toplevel(self.master)
        for index, task in enumerate(self.todo_list.tasks, start=1):
            tk.Label(update_window, text=f"{index}. {task.description} - {task.status}").pack()

        task_index = tk.Entry(update_window)
        task_index.pack()

        new_status = tk.Entry(update_window)
        new_status.pack()

        update_button = tk.Button(update_window, text="Update", command=lambda: self.update_task_status(task_index.get(), new_status.get()))
        update_button.pack()

    def update_task_status(self, task_index, new_status):
        task_index = int(task_index)
        self.todo_list.update_status(task_index, new_status)

    def save_to_text_file(self):
        self.todo_list.save_to_text_file()


def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
