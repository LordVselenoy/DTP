import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt, QDateTime

class Task:
    def __init__(self, task_id, description, assignee, start_date, deadline, status, completion_date):
        self.task_id = task_id
        self.description = description
        self.assignee = assignee
        self.start_date = start_date
        self.deadline = deadline
        self.status = status
        self.completion_date = completion_date

    def complete(self):
        self.status = "Исполнена"
        self.completion_date = QDateTime.currentDateTime()

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.db_connection = sqlite3.connect("tasks.db")
        self.create_table()

    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          description TEXT NOT NULL,
                          assignee TEXT NOT NULL,
                          start_date TEXT NOT NULL,
                          deadline TEXT NOT NULL,
                          status TEXT NOT NULL,
                          completion_date TEXT)''')
        self.db_connection.commit()

    def register_task(self, description, assignee, start_date, deadline):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO tasks (description, assignee, start_date, deadline, status) VALUES (?, ?, ?, ?, ?)",
                       (description, assignee, start_date.toString(Qt.ISODate), deadline.toString(Qt.ISODate), "Передана в работу"))
        self.db_connection.commit()
        task_id = cursor.lastrowid
        task = Task(task_id, description, assignee, start_date, deadline, "Передана в работу", None)
        self.tasks.append(task)
        return task

    def get_task_status(self, task):
        return task.status

    def complete_task(self, task):
        cursor = self.db_connection.cursor()
        cursor.execute("UPDATE tasks SET status = ?, completion_date = ? WHERE id = ?",
                       ("Исполнена", QDateTime.currentDateTime().toString(Qt.ISODate), task.task_id))
        self.db_connection.commit()
        task.complete()

    def load_tasks(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        for row in rows:
            task_id, description, assignee, start_date_str, deadline_str, status, completion_date_str = row
            start_date = QDateTime.fromString(start_date_str, Qt.ISODate)
            deadline = QDateTime.fromString(deadline_str, Qt.ISODate)
            completion_date = QDateTime.fromString(completion_date_str, Qt.ISODate) if completion_date_str else None
            task = Task(task_id, description, assignee, start_date, deadline, status, completion_date)
            self.tasks.append(task)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.task_manager = TaskManager()
        self.task_manager.load_tasks()

        self.setWindowTitle("Управление задачами")
        self.setGeometry(300, 300, 300, 200)

        self.label = QLabel("Выберите действие:", self)

        self.register_button = QPushButton("Зарегистрировать задачу", self)
        self.register_button.clicked.connect(self.register_task)

        self.complete_button = QPushButton("Завершить задачу", self)
        self.complete_button.clicked.connect(self.complete_task)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.register_button)
        layout.addWidget(self.complete_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def register_task(self):
        description, ok = QInputDialog.getText(self, "Регистрация задачи", "Введите описание задачи:")
        if ok and description:
            assignee, ok = QInputDialog.getText(self, "Регистрация задачи", "Введите исполнителя задачи:")
            if ok and assignee:
                start_date = QDateTime.currentDateTime()
                deadline, ok = QInputDialog.getText(self, "Регистрация задачи", "Введите дату выполнения задачи (в формате ГГГГ-ММ-ДД):")
                if ok and deadline:
                    try:
                        deadline = QDateTime.fromString(deadline, "yyyy-MM-dd")
                    except ValueError:
                        QMessageBox.warning(self, "Ошибка", "Некорректный формат даты. Задача не будет зарегистрирована.")
                        return

                    if deadline <= start_date:
                        QMessageBox.warning(self, "Ошибка", "Дата выполнения задачи должна быть позже текущей даты. Задача не будет зарегистрирована.")
                        return

                    task = self.task_manager.register_task(description, assignee, start_date, deadline)
                    QMessageBox.information(self, "Успех", "Задача зарегистрирована. ID задачи: {}".format(task.task_id))

    def complete_task(self):
        task_id, ok = QInputDialog.getInt(self, "Завершение задачи", "Введите ID задачи:")
        if ok and task_id >= 0 and task_id < len(self.task_manager.tasks):
            task = self.task_manager.tasks[task_id]
            self.task_manager.complete_task(task)
            QMessageBox.information(self, "Успех", "Задача завершена.")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())