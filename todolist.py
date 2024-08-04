import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task.strip())  # Strip extra spaces
        print(f"Task added: {task}")

    def remove_task(self, task):
        task = task.strip()  # Remove any extra spaces
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task removed: {task}")
            return True
        else:
            print("Task not found.")
            return False
        
    def list_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task.strip()
            print(f"Task updated to: {new_task}")
        else:
            print("Invalid index.")

    def save_tasks(self, filename="tasks.json"):
        """Save tasks to a JSON file."""
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)
        print("Tasks saved.")

    def load_tasks(self, filename="tasks.json"):
        """Load tasks from a JSON file."""
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
            print("Tasks loaded.")
        except FileNotFoundError:
            print("No saved tasks found.")
        except json.JSONDecodeError:
            print("Error decoding the saved tasks.")
