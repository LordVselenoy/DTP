from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QTableWidget, QTableWidgetItem, QCalendarWidget, QDateEdit, QLabel
from PyQt5.QtCore import Qt, QDate
from task_manager import TaskManager
from styles import Styles
from dialogs import TaskDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.task_manager = TaskManager()
        self.task_manager.load_tasks()

        self.init_ui()
