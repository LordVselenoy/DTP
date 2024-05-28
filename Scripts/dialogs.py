from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDateEdit, QHBoxLayout, QPushButton
from PyQt5.QtCore import QDate

class TaskDialog(QDialog):
    def __init__(self, parent=None, task=None):
        super().__init__(parent)
        self.setWindowTitle("Задача")

        self.task = task or {
            "client": "",
            "description": "",
            "order_date": QDate.currentDate(),
            "executor": "",
            "start_date": QDate.currentDate(),
            "due_date": QDate.currentDate(),
            "close_date": None
        }

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Клиент:"))
        self.client_edit = QLineEdit(self.task["client"])
        layout.addWidget(self.client_edit)

        layout.addWidget(QLabel("Задача:"))
        self.description_edit = QLineEdit(self.task["description"])
        layout.addWidget(self.description_edit)

        layout.addWidget(QLabel("Дата заказа:"))
        self.order_date_edit = QDateEdit(calendarPopup=True)
        self.order_date_edit.setDate(self.task["order_date"])
        layout.addWidget(self.order_date_edit)

        layout.addWidget(QLabel("Исполнитель:"))
        self.executor_edit = QLineEdit(self.task["executor"])
        layout.addWidget(self.executor_edit)

        layout.addWidget(QLabel("Дата начала:"))
        self.start_date_edit = QDateEdit(calendarPopup=True)
        self.start_date_edit.setDate(self.task["start_date"])
        layout.addWidget(self.start_date_edit)

        layout.addWidget(QLabel("Срок исполнения:"))
        self.due_date_edit = QDateEdit(calendarPopup=True)
        self.due_date_edit.setDate(self.task["due_date"])
        layout.addWidget(self.due_date_edit)

        layout.addWidget(QLabel("Дата закрытия:"))
        self.close_date_edit = QDateEdit(calendarPopup=True)
        self.close_date_edit.setDate(self.task["close_date"] or QDate.currentDate())
        self.close_date_edit.setEnabled(self.task["close_date"] is not None)
        layout.addWidget(self.close_date_edit)

        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.accept)
        button_layout.addWidget(self.save_button)

        self.cancel_button = QPushButton("Отмена")
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

    def accept(self):
        self.task["client"] = self.client_edit.text()
        self.task["description"] = self.description_edit.text()
        self.task["order_date"] = self.order_date_edit.date()
        self.task["executor"] = self.executor_edit.text()
        self.task["start_date"] = self.start_date_edit.date()
        self.task["due_date"] = self.due_date_edit.date()
        self.task["close_date"] = self.close_date_edit.date() if self.close_date_edit.isEnabled() else None
        super().accept()
