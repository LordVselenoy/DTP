import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QInputDialog, QMessageBox, QListWidget, QListWidgetItem, QComboBox
from PyQt5.QtGui import QIcon
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
        self.completion_date = QDateTime.currentDateTime().toString(Qt.ISODate)

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
        if not self.is_valid_date(start_date) or not self.is_valid_date(deadline):
            return None

        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO tasks (description, assignee, start_date, deadline, status) VALUES (?, ?, ?, ?, ?)",
                       (description, assignee, start_date, deadline, "Передана в работу"))
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

    def delete_task(self, task):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task.task_id,))
        self.db_connection.commit()
        self.tasks.remove(task)

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

    def filter_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    def is_valid_date(self, date_str):
        try:
            QDateTime.fromString(date_str, Qt.ISODate)
            return True
        except:
            return False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.task_manager = TaskManager()
        self.task_manager.load_tasks()

        self.setWindowTitle("Управление задачами")
        self.setGeometry(300, 300, 300, 200)

        self.label = QLabel("Выберите действие:", self)
        
        self.theme_button = QPushButton("Стандартная тема", self)
        self.theme_button.clicked.connect(self.toggle_theme)
        self.theme_button.setStyleSheet("background-color: #F0F0F0; color: #000000;")

        self.register_button = QPushButton(QIcon("add48.png"), "Зарегистрировать задачу", self)
        self.register_button.clicked.connect(self.register_task)

        self.complete_button = QPushButton(QIcon("save48.png"), "Завершить задачу", self)
        self.complete_button.clicked.connect(self.complete_task)

        self.delete_button = QPushButton(QIcon("delete48.png"), "Удалить задачу", self)
        self.delete_button.clicked.connect(self.delete_task)

        self.view_button = QPushButton(QIcon("reset.png"), "Обновить список", self)
        self.view_button.clicked.connect(self.view_tasks)

        self.filter_combo = QComboBox(self)
        self.filter_combo.addItem(QIcon("filter48.png"), "Все")
        self.filter_combo.addItem(QIcon("edit48.png"), "Передано в работу")
        self.filter_combo.addItem(QIcon("goal.png"), "Исполнена")
        self.filter_combo.addItem(QIcon("trash.png"), "Удалена")
        self.filter_combo.currentIndexChanged.connect(self.filter_tasks)

        self.task_list_widget = QListWidget(self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.theme_button)
        self.layout.addWidget(self.register_button)
        self.layout.addWidget(self.complete_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.view_button)
        self.layout.addWidget(self.filter_combo)
        self.layout.addWidget(self.task_list_widget)

        self.widget = QWidget(self)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #333333;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
            QPushButton {
                background-color: #555555;
                color: #ffffff;
                border: none;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #777777;
            }
            QComboBox {
                background-color: #555555;
                color: #ffffff;
            }
            QComboBox::down-arrow {
                image: url(down_arrow.png);
            }
            QComboBox QAbstractItemView {
                background-color: #555555;
                color: #ffffff;
                selection-background-color: #777777;
            }
            QListWidget {
                background-color: #555555;
                color: #ffffff;
                border: none;
                padding: 8px;
            }
            QListWidget::item {
                padding: 4px;
            }
            QListWidget::item:selected {
                background-color: #777777;
            }
        """)

    def register_task(self):
        description, ok = QInputDialog.getText(self, "Регистрация задачи", "Введите описание задачи:")
        if ok and description:
            assignee, ok = QInputDialog.getText(self, "Регистрация задачи", "Введите ответственное лицо:")
            if ok and assignee:
                start_date, ok = QInputDialog.getText(self, "Регистрация задачи", "Введите дату начала (ГГГГ-ММ-ДД):")
                if ok and start_date:
                    deadline, ok = QInputDialog.getText(self, "Регистрация задачи", "Введите дату завершения (ГГГГ-ММ-ДД):")
                    if ok and deadline:
                        task = self.task_manager.register_task(description, assignee, start_date, deadline)
                        if task:
                            self.task_list_widget.addItem(f"{task.task_id}: {description}")
                            
    def toggle_theme(self):
        if self.theme_button.text() == "Стандартная тема":
            self.theme_button.setText("Темная тема")
            self.theme_button.setStyleSheet("background-color: #000000; color: #ffffff;")
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #222222;
                    color: #ffffff;
                }
                QLabel {
                    color: #ffffff;
                }
                QPushButton {
                    background-color: #444444;
                    color: #ffffff;
                    border: none;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background-color: #666666;
                }
                QComboBox {
                    background-color: #444444;
                    color: #ffffff;
                }
                QComboBox::down-arrow {
                    image: url(down_arrow_white.png);
                }
                QComboBox QAbstractItemView {
                    background-color: #444444;
                    color: #ffffff;
                    selection-background-color: #666666;
                }
                QListWidget {
                    background-color: #444444;
                    color: #ffffff;
                    border: none;
                    padding: 8px;
                }
                QListWidget::item {
                    padding: 4px;
                }
                QListWidget::item:selected {
                    background-color: #666666;
                }
            """)
        elif self.theme_button.text() == "Темная тема":
            self.theme_button.setText("Светлая тема")
            self.theme_button.setStyleSheet("background-color: #F0F0F0; color: #000000;")
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #F0F0F0;
                    color: #000000;
                }
                QLabel {
                    color: #000000;
                }
                QPushButton {
                    background-color: #DDDDDD;
                    color: #000000;
                    border: none;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background-color: #CCCCCC;
                }
                QComboBox {
                    background-color: #DDDDDD;
                    color: #000000;
                }
                QComboBox::down-arrow {
                    image: url(down_arrow_black.png);
                }
                QComboBox QAbstractItemView {
                    background-color: #DDDDDD;
                    color: #000000;
                    selection-background-color: #CCCCCC;
                }
                QListWidget {
                    background-color: #DDDDDD;
                    color: #000000;
                    border: none;
                    padding: 8px;
                }
                QListWidget::item {
                    padding: 4px;
                }
                QListWidget::item:selected {
                    background-color: #CCCCCC;
                }
            """)
        elif self.theme_button.text() == "Светлая тема":
            self.theme_button.setText("Стандартная тема")
            self.theme_button.setStyleSheet("background-color: #F0F0F0; color: #000000;")
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #333333;
                    color: #ffffff;
                }
                QLabel {
                    color: #ffffff;
                }
                QPushButton {
                    background-color: #555555;
                    color: #ffffff;
                    border: none;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background-color: #777777;
                }
                QComboBox {
                    background-color: #555555;
                    color: #ffffff;
                }
                QComboBox::down-arrow {
                    image: url(down_arrow.png);
                }
                QComboBox QAbstractItemView {
                    background-color: #555555;
                    color: #ffffff;
                    selection-background-color: #777777;
                }
                QListWidget {
                    background-color: #555555;
                    color: #ffffff;
                    border: none;
                    padding: 8px;
                }
                QListWidget::item {
                    padding: 4px;
                }
                QListWidget::item:selected {
                    background-color: #777777;
                }
            """)


    def complete_task(self):
        selected_item = self.task_list_widget.currentItem()
        if selected_item:
            task_id = int(selected_item.text().split(":")[0])
            task = next((task for task in self.task_manager.tasks if task.task_id == task_id), None)
            if task:
                self.task_manager.complete_task(task)
                selected_item.setText(f"{task.task_id}: {task.description} (Исполнена)")

    def delete_task(self):
        task_list = self.task_manager.tasks
        if not task_list:
            QMessageBox.information(self, "Нет задач", "Нет зарегистрированных задач.")
            return

        task_names = [f"{task.description} ({task.assignee})" for task in task_list]
        task_name, ok = QInputDialog.getItem(self, "Удалить задачу", "Выберите задачу:", task_names, editable=False)
        if ok and task_name:
            index = task_names.index(task_name)
            task = task_list[index]
            reply = QMessageBox.question(self, "Подтверждение удаления", "Вы уверены, что хотите удалить задачу?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.task_manager.delete_task(task)
                QMessageBox.information(self, "Задача удалена", "Задача успешно удалена.")

    def view_tasks(self):
        self.task_list_widget.clear()
        for task in self.task_manager.tasks:
            item_text = f"{task.task_id}: {task.description}"
            if task.status == "Исполнена":
                item_text += f" (Исполнена {task.completion_date})"
            self.task_list_widget.addItem(item_text)
            
    def show_task_details(self, item):
        index = self.task_list_widget.row(item)
        task = self.task_manager.tasks[index]
        QMessageBox.information(self, "Детали задачи",
                                f"Описание: {task.description}\n"
                                f"Исполнитель: {task.assignee}\n"
                                f"Дата начала: {task.start_date.toString(Qt.ISODate)}\n"
                                f"Крайний срок: {task.deadline.toString(Qt.ISODate)}\n"
                                f"Статус: {task.status}\n"
                                f"Дата завершения: {task.completion_date.toString(Qt.ISODate) if task.completion_date else ''}")

    def filter_tasks(self):
        selected_filter = self.filter_combo.currentText()
        if selected_filter == "Все":
            self.view_tasks()
        else:
            self.task_list_widget.clear()
            filtered_tasks = self.task_manager.filter_tasks_by_status(selected_filter)
            for task in filtered_tasks:
                item_text = f"{task.task_id}: {task.description}"
                if task.status == "Исполнена":
                    item_text += f" (Исполнена {task.completion_date})"
                self.task_list_widget.addItem(item_text)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()