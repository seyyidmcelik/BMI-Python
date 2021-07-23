import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()
        
    def  init_ui(self):

        self.setFixedWidth(500)
        self.setFixedHeight(300)
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle("BMI Calculation")
        
        self.height = QtWidgets.QLineEdit(self)
        self.weight = QtWidgets.QLineEdit(self)
        self.weight.setValidator(QtGui.QIntValidator())
        self.height.setValidator(QtGui.QIntValidator())
        self.height.setPlaceholderText("Type your height like 170")
        self.weight.setPlaceholderText("Type your weight like 67")
        self.text1 = QtWidgets.QLabel()
        self.text2 = QtWidgets.QLabel()
        self.resultInt = QtWidgets.QLabel()
        self.resultText = QtWidgets.QLabel()
        self.text1.setText("Weight")
        self.text2.setText("Height")
        self.resultInt.setText("")
        self.resultText.setText("")
        self.picture = QtWidgets.QLabel()
        self.picture.setPixmap(QtGui.QPixmap("fit.png"))
        self.calculate = QtWidgets.QPushButton("Calculate")
        self.reset = QtWidgets.QPushButton("Clean")


        v_box = QtWidgets.QVBoxLayout()

        

        v_box2 = QtWidgets.QVBoxLayout()
        v_box2.addStretch()
        v_box2.addWidget(self.text2)
        v_box2.addWidget(self.height)
        v_box2.addWidget(self.text1)
        v_box2.addWidget(self.weight)
        v_box2.addWidget(self.resultInt)
        v_box2.addWidget(self.resultText)
        v_box2.addStretch()
        v_box2.addWidget(self.calculate)
        v_box2.addWidget(self.reset)
        v_box2.addStretch()
        v_box2.addLayout(v_box)


        h_box = QtWidgets.QHBoxLayout()

        h_box.addWidget(self.picture)
        h_box.addLayout(v_box2)


        self.setLayout(h_box)

        self.reset.clicked.connect(self.resetClick)
        self.calculate.clicked.connect(self.calculateClick)

        self.show()
        
    def resetClick(self):
        self.height.clear()
        self.weight.clear()
        self.resultInt.clear()
        self.resultText.clear()

    def calculateClick(self):
        
        
        try:
            hei = int(self.height.text()) #int
            wei = float(self.weight.text()) #float
            ibm = round(wei / ((hei/100)**2),2) #float
            ibm = str(ibm)
            if float(ibm) <= 18.5:
                self.resultInt.setText("Body mass index(BMI) "+ibm)
                self.resultText.setText("Weak\nYou should gain weight ")
            elif float(ibm) <= 24.9:
                self.resultInt.setText("Body mass index(BMI) "+ibm)
                self.resultText.setText("Normal\nKeep fit")
            elif float(ibm) <= 29.9:
                self.resultInt.setText("Body mass index(BMI) "+ibm)
                self.resultText.setText("Overweight\nYou should lose weight")
            elif float(ibm) <= 39.9:
                self.resultInt.setText("Body mass index(BMI) "+ibm)
                self.resultText.setText("Obese\nYou should lose weight")
            elif float(ibm) > 39.9:
                self.resultInt.setText("Body mass index(BMI) "+ibm)
                self.resultText.setText("Too obese\nYou should lose weight")
        except:
                self.resultInt.setText("Type the fields with integers")
        
        


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

