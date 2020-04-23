# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ground_station.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 728)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 620, 75, 31))
        self.pushButton.setStyleSheet("color: rgb(198, 198, 198);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(34, 104, 179);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 620, 661, 31))
        self.textEdit.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"color: rgb(253, 253, 253);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Panel)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 290, 751, 311))
        self.textEdit_2.setStyleSheet("color: rgb(78, 255, 25);\n"
"background-color: rgb(31, 31, 31);")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_2.setLineWidth(1)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1230, 550, 101, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Descargas/icaro19_logo.png"))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 951, 251))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsTemperature = PlotWidget(self.horizontalLayoutWidget)
        self.graphicsTemperature.setObjectName("graphicsTemperature")
        self.horizontalLayout.addWidget(self.graphicsTemperature)
        self.graphicsPresure = PlotWidget(self.horizontalLayoutWidget)
        self.graphicsPresure.setObjectName("graphicsPresure")
        self.horizontalLayout.addWidget(self.graphicsPresure)
        self.lcdTemperature = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdTemperature.setGeometry(QtCore.QRect(1240, 20, 64, 23))
        self.lcdTemperature.setProperty("value", 0.0)
        self.lcdTemperature.setObjectName("lcdTemperature")
        self.lcdPresure = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdPresure.setGeometry(QtCore.QRect(1220, 70, 81, 23))
        self.lcdPresure.setDigitCount(7)
        self.lcdPresure.setObjectName("lcdPresure")
        self.lcdAltitude = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdAltitude.setGeometry(QtCore.QRect(1240, 120, 64, 23))
        self.lcdAltitude.setObjectName("lcdAltitude")
        self.lcdArqppm = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdArqppm.setGeometry(QtCore.QRect(1110, 170, 70, 23))
        self.lcdArqppm.setObjectName("lcdArqppm")
        self.lcdUV = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdUV.setGeometry(QtCore.QRect(1240, 220, 64, 23))
        self.lcdUV.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdUV.setObjectName("lcdUV")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1000, 30, 131, 16))
        self.label_2.setStyleSheet("color: rgb(140, 255, 78);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1000, 80, 131, 16))
        self.label_3.setStyleSheet("color: rgb(140, 255, 78);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1000, 130, 131, 16))
        self.label_4.setStyleSheet("color: rgb(140, 255, 78);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1000, 180, 131, 16))
        self.label_5.setStyleSheet("color: rgb(140, 255, 78);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1000, 230, 171, 16))
        self.label_6.setStyleSheet("color: rgb(140, 255, 78);")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1310, 80, 61, 16))
        self.label_9.setStyleSheet("color: rgb(140, 255, 78);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1310, 30, 61, 16))
        self.label_10.setStyleSheet("color: rgb(140, 255, 78);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1310, 130, 61, 16))
        self.label_11.setStyleSheet("color: rgb(140, 255, 78);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1180, 180, 41, 16))
        self.label_12.setStyleSheet("color: rgb(140, 255, 78);")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1310, 180, 61, 16))
        self.label_14.setStyleSheet("color: rgb(140, 255, 78);")
        self.label_14.setObjectName("label_14")
        self.lcdArqppb = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdArqppb.setGeometry(QtCore.QRect(1240, 170, 64, 23))
        self.lcdArqppb.setObjectName("lcdArqppb")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(1000, 250, 301, 31))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background-color: rgb(24, 24, 24);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.nivel4 = QtWidgets.QWidget(self.frame)
        self.nivel4.setGeometry(QtCore.QRect(84, -2, 22, 31))
        self.nivel4.setMinimumSize(QtCore.QSize(22, 19))
        self.nivel4.setStyleSheet("background-color: rgb(244, 223, 0);")
        self.nivel4.setObjectName("nivel4")
        self.nivel9 = QtWidgets.QWidget(self.frame)
        self.nivel9.setGeometry(QtCore.QRect(224, -2, 22, 31))
        self.nivel9.setMinimumSize(QtCore.QSize(22, 19))
        self.nivel9.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.nivel9.setObjectName("nivel9")
        self.nivel3 = QtWidgets.QWidget(self.frame)
        self.nivel3.setGeometry(QtCore.QRect(56, -2, 22, 31))
        self.nivel3.setMinimumSize(QtCore.QSize(22, 19))
        self.nivel3.setStyleSheet("background-color: rgb(225, 254, 0);")
        self.nivel3.setObjectName("nivel3")
        self.nivel5 = QtWidgets.QWidget(self.frame)
        self.nivel5.setGeometry(QtCore.QRect(112, -2, 22, 31))
        self.nivel5.setMinimumSize(QtCore.QSize(22, 19))
        self.nivel5.setStyleSheet("background-color: rgb(250, 178, 0);")
        self.nivel5.setObjectName("nivel5")
        self.nivel1 = QtWidgets.QWidget(self.frame)
        self.nivel1.setGeometry(QtCore.QRect(0, -2, 22, 31))
        self.nivel1.setMinimumSize(QtCore.QSize(22, 19))
        self.nivel1.setStyleSheet("background-color: rgb(98, 167, 52);")
        self.nivel1.setObjectName("nivel1")
        self.nivel6 = QtWidgets.QWidget(self.frame)
        self.nivel6.setGeometry(QtCore.QRect(140, -2, 22, 31))
        self.nivel6.setMinimumSize(QtCore.QSize(22, 19))
        self.nivel6.setStyleSheet("background-color: rgb(254, 127, 0);")
        self.nivel6.setObjectName("nivel6")
        self.nivel2 = QtWidgets.QWidget(self.frame)
        self.nivel2.setGeometry(QtCore.QRect(28, -2, 22, 31))
        self.nivel2.setMinimumSize(QtCore.QSize(22, 19))
        self.nivel2.setStyleSheet("background-color: rgb(134, 223, 37);")
        self.nivel2.setObjectName("nivel2")
        self.nivel7 = QtWidgets.QWidget(self.frame)
        self.nivel7.setGeometry(QtCore.QRect(168, -2, 22, 31))
        self.nivel7.setMinimumSize(QtCore.QSize(22, 19))
        self.nivel7.setStyleSheet("background-color: rgb(245, 100, 0);")
        self.nivel7.setObjectName("nivel7")
        self.nivel10 = QtWidgets.QWidget(self.frame)
        self.nivel10.setGeometry(QtCore.QRect(252, -2, 22, 31))
        self.nivel10.setMinimumSize(QtCore.QSize(22, 19))
        self.nivel10.setStyleSheet("background-color: rgb(255, 0, 110);")
        self.nivel10.setObjectName("nivel10")
        self.nivel11 = QtWidgets.QWidget(self.frame)
        self.nivel11.setGeometry(QtCore.QRect(280, -2, 22, 31))
        self.nivel11.setMinimumSize(QtCore.QSize(22, 19))
        self.nivel11.setStyleSheet("background-color: rgb(221, 0, 180);")
        self.nivel11.setObjectName("nivel11")
        self.nivel8 = QtWidgets.QWidget(self.frame)
        self.nivel8.setGeometry(QtCore.QRect(196, -2, 22, 31))
        self.nivel8.setMinimumSize(QtCore.QSize(22, 19))
        self.nivel8.setStyleSheet("background-color: rgb(242, 0, 0);")
        self.nivel8.setObjectName("nivel8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 25))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Icaro´19 Ground Station"))
        self.pushButton.setText(_translate("MainWindow", "Enviar"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Temperatura:"))
        self.label_3.setText(_translate("MainWindow", "Presión:"))
        self.label_4.setText(_translate("MainWindow", "Altitud:"))
        self.label_5.setText(_translate("MainWindow", "Calidad del aire:"))
        self.label_6.setText(_translate("MainWindow", "Índice ultravioleta:"))
        self.label_9.setText(_translate("MainWindow", "hPa"))
        self.label_10.setText(_translate("MainWindow", "ºC"))
        self.label_11.setText(_translate("MainWindow", "m"))
        self.label_12.setText(_translate("MainWindow", "ppm"))
        self.label_14.setText(_translate("MainWindow", "ppb"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
from pyqtgraph import PlotWidget