# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from keyboard import add_hotkey
from pyqtgraph import PlotWidget # PlotWidget nesnesini ekliyoruz
import pyqtgraph as pg
import numpy as np # Numpy modülünü ekliyoruz
import random # Random modülünü ekliyoruz

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(200, 200, 200);")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plotWidget = PlotWidget(self.centralwidget) # QGraphicsView yerine PlotWidget kullanıyoruz
        self.plotWidget.setGeometry(QtCore.QRect(440, 80, 1011, 531)) # PlotWidget nesnesinin konumunu ayarlıyoruz
        self.plotWidget.setObjectName("plotWidget")
        self.plotWidget.setRange(xRange=(-10, 10), yRange=(-10, 10), padding=0)
        self.plotWidget.showGrid(x=True, y=True, alpha=0.9)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(440, 630, 771, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 769, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setAlignment(QtCore.Qt.AlignTop)  # Frameleri üst tarafa hizala
        self.verticalLayout.setSpacing(3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.fonksiyonEkle_button = QtWidgets.QPushButton(self.centralwidget)
        self.fonksiyonEkle_button.setGeometry(QtCore.QRect(1220, 630, 231, 41))
        self.fonksiyonEkle_button.setStyleSheet("background-color: rgb(87, 65, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.fonksiyonEkle_button.setObjectName("fonksiyonEkle_button")
        self.fonksiyonEkle_button.clicked.connect(self.addLineEdit)
        self.hepsinisil_button = QtWidgets.QPushButton(self.centralwidget)
        self.hepsinisil_button.setGeometry(QtCore.QRect(1220, 680, 231, 41))
        self.hepsinisil_button.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.hepsinisil_button.setObjectName("hepsinisil_button")
        self.hepsinisil_button.clicked.connect(self.allDelete)
        self.cizbutton = QtWidgets.QPushButton(self.centralwidget)
        self.cizbutton.setGeometry(QtCore.QRect(1220, 990, 231, 71))
        self.cizbutton.setStyleSheet("background-color: rgb(0, 180, 6);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.cizbutton.setObjectName("cizbutton")
        self.addLineEdit()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fonksiyonEkle_button.setText(_translate("MainWindow", "Fonksiyon Ekle"))
        self.hepsinisil_button.setText(_translate("MainWindow", "Hepsini Sil"))
        self.cizbutton.setText(_translate("MainWindow", "Çiz"))
        self.cizbutton.clicked.connect(self.cizim)

    def addLineEdit(self):
        try:
            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            frame.setMaximumSize(QtCore.QSize(16777215, 50))
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame")
            horizontalLayout = QtWidgets.QHBoxLayout(frame)
            horizontalLayout.setObjectName("horizontalLayout")
            lineEdit = QtWidgets.QLineEdit(frame)
            lineEdit.setMinimumSize(QtCore.QSize(23, 34))
            lineEdit.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";")
            lineEdit.setObjectName("lineEdit")
            horizontalLayout.addWidget(lineEdit)
            pushButton = QtWidgets.QPushButton(frame)
            pushButton.setMinimumSize(QtCore.QSize(0, 33))
            pushButton.setMaximumSize(QtCore.QSize(35, 16777215))
            pushButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";")
            pushButton.setObjectName("pushButton")
            pushButton.setText("X")
            pushButton.clicked.connect(lambda x,idx=frame : self.deleteButton(idx))
            horizontalLayout.addWidget(pushButton)
            self.verticalLayout.addWidget(frame)
        except Exception as e:
            print(e)
    def cizim(self):
        try: 
            self.plotWidget.clear()
            for i in range(self.verticalLayout.count()):
                    frame = self.verticalLayout.itemAt(i).widget()
                    lineEdit = frame.findChild(QtWidgets.QLineEdit,"lineEdit")
                    text = lineEdit.text()
                    x = np.linspace(-10, 10, 100)
                    y1 = eval(text) # İlk fonksiyonu y değerleri olarak hesaplıyoruz

                    renk = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                    self.plotWidget.plot(x, y1, pen=pg.mkPen(color=renk,width=2.5,cosmetic = True)) # PlotWidget'e x ve y1 değerlerini çizdiriyoruz
                    lineEdit.setStyleSheet(f"border: 3px solid rgb{renk}")
        except Exception as e:
            print(e)
    def deleteButton(self,id):
        try:
            id.deleteLater()
            QtCore.QTimer.singleShot(100, self.cizim)    

        except Exception as e:
            print(e)
    def allDelete(self):
        try:
            # verticalLayout içindeki tüm widget'ları sil
            for i in reversed(range(self.verticalLayout.count())):
                widget_to_remove = self.verticalLayout.itemAt(i).widget()
                # Widget'ı layout'tan çıkar
                self.verticalLayout.removeWidget(widget_to_remove)
                # Widget'ı sil
                widget_to_remove.deleteLater()
            QtCore.QTimer.singleShot(100, self.cizim)          
        except Exception as e:
            print(e) 
    def close(self):
        MainWindow.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    add_hotkey('esc',ui.close)
    sys.exit(app.exec_())
