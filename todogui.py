import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox
from todolist import ToDoList

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x400")  # Set window size to 800x400 pixels
        self.master.configure(bg="#05FBF0")  # Set background color 
        self.master.title("To-Do List Application")  # Change window title

        header_label = tk.Label(self.master, text="My To-Do List", font=("Arial", 20), bg="black", fg="#05FBF0", padx=10, pady=10)
        header_label.pack(fill=tk.X)

        self.todo_list = ToDoList()
        self.todo_list.load_tasks()  # Load tasks from file

        self.task_entry = tk.Entry(self.master, bg="#6A7070", width=50, font=("Helvetica", 14))
        self.task_entry.pack(padx=50, pady=10)

        button_frame = tk.Frame(self.master, bg="#05FBF0")
        button_frame.pack(pady=5)

        self.add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, width=20, bg="#145956", fg="white", font=("Arial", 12))
        self.add_button.grid(row=0, column=0, padx=10, pady=5)

        self.remove_button = tk.Button(button_frame, text="Remove Task", command=self.remove_task, width=20, bg="#145956", fg="white", font=("Arial", 12))
        self.remove_button.grid(row=0, column=1, padx=10, pady=5)

        self.update_button = tk.Button(button_frame, text="Update Task", command=self.update_task, width=20, bg="#145956", fg="white", font=("Arial", 12))
        self.update_button.grid(row=0, column=2, padx=10, pady=5)

        self.exit_button = tk.Button(button_frame, text="Exit", command=self.on_exit, width=20, bg="#145956", fg="white", font=("Arial", 12))
        self.exit_button.grid(row=0, column=3, padx=10, pady=5)

        self.listbox = Listbox(self.master, bg="#5AF3F3", fg="black", font=("Helvetica", 14), selectbackground="gray", selectforeground="black", activestyle="none", bd=2, relief="solid")
        scrollbar = tk.Scrollbar(self.master, orient="vertical", command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.listbox.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.list_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.list_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            task = self.listbox.get(index).lstrip('• ').strip()  # Remove bullet and any extra spaces

            if self.todo_list.remove_task(task):
                self.listbox.delete(index)
                print(f"Task '{task}' removed successfully.")
            else:
                messagebox.showwarning("Warning", "Task not found in the list!")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove!")

    def update_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            old_task = self.listbox.get(selected_task_index).lstrip('• ').strip()  # Normalize task

            new_task = simpledialog.askstring("Update Task", f"Update '{old_task}' to:")
            if new_task:
                self.todo_list.update_task(selected_task_index[0], new_task)
                self.list_tasks()
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")
        else:
            messagebox.showwarning("Warning", "Please select a task to update!")

    def list_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.listbox.insert(tk.END, f"• {task}")

    def on_exit(self):
        self.todo_list.save_tasks()  # Save tasks to file
        self.master.quit()

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
