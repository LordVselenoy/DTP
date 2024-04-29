# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\TMProject\Forms\mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 645)
        MainWindow.setMinimumSize(QtCore.QSize(772, 645))
        MainWindow.setMaximumSize(QtCore.QSize(772, 645))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(6, 0, 361, 190))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(6, 197, 761, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.dateGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.dateGroupBox.setGeometry(QtCore.QRect(370, 0, 181, 191))
        self.dateGroupBox.setObjectName("dateGroupBox")
        self.dateEditIn = QtWidgets.QDateEdit(self.dateGroupBox)
        self.dateEditIn.setEnabled(True)
        self.dateEditIn.setGeometry(QtCore.QRect(58, 49, 110, 22))
        self.dateEditIn.setCalendarPopup(True)
        self.dateEditIn.setObjectName("dateEditIn")
        self.label = QtWidgets.QLabel(self.dateGroupBox)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(7, 54, 47, 13))
        self.label.setObjectName("label")
        self.dateEditOut = QtWidgets.QDateEdit(self.dateGroupBox)
        self.dateEditOut.setEnabled(True)
        self.dateEditOut.setGeometry(QtCore.QRect(58, 79, 110, 22))
        self.dateEditOut.setCalendarPopup(True)
        self.dateEditOut.setObjectName("dateEditOut")
        self.label_2 = QtWidgets.QLabel(self.dateGroupBox)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(9, 83, 47, 13))
        self.label_2.setObjectName("label_2")
        self.filterButton = QtWidgets.QPushButton(self.dateGroupBox)
        self.filterButton.setEnabled(True)
        self.filterButton.setGeometry(QtCore.QRect(10, 107, 161, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Z:\\TMProject\\Forms\\../icons/filter48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filterButton.setIcon(icon)
        self.filterButton.setFlat(False)
        self.filterButton.setObjectName("filterButton")
        self.dbGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.dbGroupBox.setGeometry(QtCore.QRect(158, 561, 451, 41))
        self.dbGroupBox.setTitle("")
        self.dbGroupBox.setObjectName("dbGroupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.dbGroupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(4, 5, 441, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Z:\\TMProject\\Forms\\../icons/add48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Z:\\TMProject\\Forms\\../icons/edit48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon2)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.delButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Z:\\TMProject\\Forms\\../icons/delete48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delButton.setIcon(icon3)
        self.delButton.setObjectName("delButton")
        self.horizontalLayout.addWidget(self.delButton)
        self.guideGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.guideGroupBox.setGeometry(QtCore.QRect(556, 0, 211, 191))
        self.guideGroupBox.setObjectName("guideGroupBox")
        self.customerButton = QtWidgets.QPushButton(self.guideGroupBox)
        self.customerButton.setGeometry(QtCore.QRect(30, 48, 161, 23))
        self.customerButton.setMinimumSize(QtCore.QSize(161, 0))
        self.customerButton.setObjectName("customerButton")
        self.executorButton = QtWidgets.QPushButton(self.guideGroupBox)
        self.executorButton.setGeometry(QtCore.QRect(30, 78, 161, 23))
        self.executorButton.setMinimumSize(QtCore.QSize(161, 0))
        self.executorButton.setObjectName("executorButton")
        self.statusButton = QtWidgets.QPushButton(self.guideGroupBox)
        self.statusButton.setGeometry(QtCore.QRect(30, 108, 161, 23))
        self.statusButton.setMinimumSize(QtCore.QSize(161, 0))
        self.statusButton.setObjectName("statusButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Журнал задач"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Клиент"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Задача"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата заказа"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Исполнитель"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Дата начала"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Срок исполнения"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Дата закрытия"))
        self.dateGroupBox.setTitle(_translate("MainWindow", "Фильтр по датам"))
        self.label.setText(_translate("MainWindow", "Старт"))
        self.label_2.setText(_translate("MainWindow", "Финиш"))
        self.filterButton.setText(_translate("MainWindow", "Применить фильтр"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.editButton.setText(_translate("MainWindow", "Изменить"))
        self.delButton.setText(_translate("MainWindow", "Удалить"))
        self.guideGroupBox.setTitle(_translate("MainWindow", "Справочники"))
        self.customerButton.setText(_translate("MainWindow", "Клиенты"))
        self.executorButton.setText(_translate("MainWindow", "Исполнители"))
        self.statusButton.setText(_translate("MainWindow", "Статусы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
