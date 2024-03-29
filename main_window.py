# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.canvas = GraphWidget(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(10, 10, 640, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setObjectName("canvas")
        self.results_box = QtWidgets.QGroupBox(self.centralwidget)
        self.results_box.setGeometry(QtCore.QRect(10, 500, 641, 191))
        self.results_box.setObjectName("results_box")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.results_box)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 19, 621, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.function_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.function_lbl.setObjectName("function_lbl")
        self.verticalLayout.addWidget(self.function_lbl)
        self.error_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.error_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.error_lbl.setObjectName("error_lbl")
        self.verticalLayout.addWidget(self.error_lbl)
        self.estimate_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.estimate_lbl.setObjectName("estimate_lbl")
        self.verticalLayout.addWidget(self.estimate_lbl)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(660, 10, 291, 681))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_1.sizePolicy().hasHeightForWidth())
        self.lbl_1.setSizePolicy(sizePolicy)
        self.lbl_1.setWordWrap(True)
        self.lbl_1.setObjectName("lbl_1")
        self.verticalLayout_2.addWidget(self.lbl_1)
        self.lbl_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_2.sizePolicy().hasHeightForWidth())
        self.lbl_2.setSizePolicy(sizePolicy)
        self.lbl_2.setWordWrap(True)
        self.lbl_2.setObjectName("lbl_2")
        self.verticalLayout_2.addWidget(self.lbl_2)
        self.points_table = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.points_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.points_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.points_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.points_table.setGridStyle(QtCore.Qt.SolidLine)
        self.points_table.setCornerButtonEnabled(True)
        self.points_table.setObjectName("points_table")
        self.points_table.setColumnCount(2)
        self.points_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.points_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.points_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.points_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(1, item)
        self.points_table.horizontalHeader().setCascadingSectionResizes(False)
        self.points_table.horizontalHeader().setDefaultSectionSize(137)
        self.points_table.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.points_table)
        self.calculate_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.calculate_btn.setFont(font)
        self.calculate_btn.setObjectName("calculate_btn")
        self.verticalLayout_2.addWidget(self.calculate_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.results_box.setTitle(_translate("MainWindow", "Результаты вычислений"))
        self.function_lbl.setText(_translate("MainWindow", "Функция"))
        self.error_lbl.setText(_translate("MainWindow", "Ошибка"))
        self.estimate_lbl.setText(_translate("MainWindow", "Качество приближения"))
        self.lbl_1.setText(_translate("MainWindow", "Введите координаты точек, для которых нужно найти линейную функцию."))
        self.lbl_2.setText(_translate("MainWindow", "Нажмите два раза на ячейку, чтобы отредактировать ее значение"))
        item = self.points_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.points_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.points_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.points_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x"))
        item = self.points_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y"))
        self.calculate_btn.setText(_translate("MainWindow", "Вычислить"))
from graph_widget import GraphWidget
