from PyQt5.QtCore import QDate

class TaskManager:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        pass

    def save_tasks(self):
        pass

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, index, task):
        self.tasks[index] = task
        self.save_tasks()

    def delete_task(self, index):
        del self.tasks[index]
        self.save_tasks()
