import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from math import *


class Ui_Calc(object):
    def setupUi(self, Calc):
        Calc.setObjectName("Calc")
        Calc.setFixedSize(364, 590)

        self.centralwidget = QtWidgets.QWidget(Calc)
        self.centralwidget.setObjectName("centralwidget")

        self.root = QtWidgets.QPushButton(self.centralwidget)
        self.root.setGeometry(QtCore.QRect(290, 310, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.root.setFont(font)
        self.root.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(213, 213, 213);"
        )
        self.root.setObjectName("root")

        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(290, 520, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(213, 213, 213);"
        )
        self.clear.setObjectName("clear")

        self.delete = QtWidgets.QPushButton(self.centralwidget)
        self.delete.setGeometry(QtCore.QRect(290, 380, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.delete.setFont(font)
        self.delete.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(213, 213, 213);"
        )
        self.delete.setObjectName("delete")

        self.p_i = QtWidgets.QPushButton(self.centralwidget)
        self.p_i.setGeometry(QtCore.QRect(290, 450, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.p_i.setFont(font)
        self.p_i.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(213, 213, 213);"
        )
        self.p_i.setObjectName("p_i")

        self.input = QtWidgets.QLabel(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(90, 190, 261, 101))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        self.input.setFont(font)
        self.input.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(213, 213, 213);"
        )
        self.input.setObjectName("input")

        self.result = QtWidgets.QPushButton(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(220, 520, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(213, 213, 213);"
        )
        self.result.setObjectName("result")

        self.num_9 = QtWidgets.QPushButton(self.centralwidget)
        self.num_9.setGeometry(QtCore.QRect(220, 450, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.num_9.setFont(font)
        self.num_9.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(160, 160, 160);"
        )
        self.num_9.setObjectName("num_9")

        self.num_3 = QtWidgets.QPushButton(self.centralwidget)
        self.num_3.setGeometry(QtCore.QRect(220, 310, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.num_3.setFont(font)
        self.num_3.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(160, 160, 160);"
        )
        self.num_3.setObjectName("num_3")

        self.num_6 = QtWidgets.QPushButton(self.centralwidget)
        self.num_6.setGeometry(QtCore.QRect(220, 380, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.num_6.setFont(font)
        self.num_6.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(160, 160, 160);"
        )
        self.num_6.setObjectName("num_6")

        self.num_0 = QtWidgets.QPushButton(self.centralwidget)
        self.num_0.setGeometry(QtCore.QRect(150, 520, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.num_0.setFont(font)
        self.num_0.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(160, 160, 160);"
        )
        self.num_0.setObjectName("num_0")

        self.num_8 = QtWidgets.QPushButton(self.centralwidget)
        self.num_8.setGeometry(QtCore.QRect(150, 450, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.num_8.setFont(font)
        self.num_8.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(160, 160, 160);"
        )
        self.num_8.setObjectName("num_8")

        self.num_7 = QtWidgets.QPushButton(self.centralwidget)
        self.num_7.setGeometry(QtCore.QRect(80, 450, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.num_7.setFont(font)
        self.num_7.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(160, 160, 160);"
        )
        self.num_7.setObjectName("num_7")

        self.num_2 = QtWidgets.QPushButton(self.centralwidget)
        self.num_2.setGeometry(QtCore.QRect(150, 310, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.num_2.setFont(font)
        self.num_2.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(160, 160, 160);"
        )
        self.num_2.setObjectName("num_2")

        self.num_5 = QtWidgets.QPushButton(self.centralwidget)
        self.num_5.setGeometry(QtCore.QRect(150, 380, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.num_5.setFont(font)
        self.num_5.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(160, 160, 160);"
        )
        self.num_5.setObjectName("num_5")

        self.factorial = QtWidgets.QPushButton(self.centralwidget)
        self.factorial.setGeometry(QtCore.QRect(80, 520, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.factorial.setFont(font)
        self.factorial.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(213, 213, 213);"
        )
        self.factorial.setObjectName("factorial")

        self.num_1 = QtWidgets.QPushButton(self.centralwidget)
        self.num_1.setGeometry(QtCore.QRect(80, 310, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.num_1.setFont(font)
        self.num_1.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(160, 160, 160);"
        )
        self.num_1.setObjectName("num_1")

        self.num_4 = QtWidgets.QPushButton(self.centralwidget)
        self.num_4.setGeometry(QtCore.QRect(80, 380, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.num_4.setFont(font)
        self.num_4.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(160, 160, 160);"
        )
        self.num_4.setObjectName("num_4")

        self.division = QtWidgets.QPushButton(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(10, 520, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.division.setFont(font)
        self.division.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(213, 213, 213);"
        )
        self.division.setObjectName("division")

        self.multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.multiplication.setGeometry(QtCore.QRect(10, 450, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.multiplication.setFont(font)
        self.multiplication.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(213, 213, 213);"
        )
        self.multiplication.setObjectName("multiplication")

        self.subtraction = QtWidgets.QPushButton(self.centralwidget)
        self.subtraction.setGeometry(QtCore.QRect(10, 380, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.subtraction.setFont(font)
        self.subtraction.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(213, 213, 213);"
        )
        self.subtraction.setObjectName("subtraction")

        self.addition = QtWidgets.QPushButton(self.centralwidget)
        self.addition.setGeometry(QtCore.QRect(10, 310, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.addition.setFont(font)
        self.addition.setStyleSheet(
            "border-radius:10px;\n"
            "background-color: rgb(213, 213, 213);"
        )
        self.addition.setObjectName("addition")

        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(90, 80, 261, 101))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        self.output.setFont(font)
        self.output.setStyleSheet("color: rgb(200, 200, 200)")
        self.output.setObjectName("output")
        Calc.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calc)
        QtCore.QMetaObject.connectSlotsByName(Calc)

    def retranslateUi(self, Calc):
        translate = QtCore.QCoreApplication.translate
        Calc.setWindowTitle(translate("Calc", "Calculator"))
        self.root.setText(translate("Calc", "√"))
        self.clear.setText(translate("Calc", "c"))
        self.delete.setText(translate("Calc", "⌫"))
        self.p_i.setText(translate("Calc", "π"))
        self.input.setText(translate("Calc", ""))
        self.result.setText(translate("Calc", "="))
        self.num_9.setText(translate("Calc", "9"))
        self.num_3.setText(translate("Calc", "3"))
        self.num_6.setText(translate("Calc", "6"))
        self.num_0.setText(translate("Calc", "0"))
        self.num_8.setText(translate("Calc", "8"))
        self.num_7.setText(translate("Calc", "7"))
        self.num_2.setText(translate("Calc", "2"))
        self.num_5.setText(translate("Calc", "5"))
        self.factorial.setText(translate("Calc", "n!"))
        self.num_1.setText(translate("Calc", "1"))
        self.num_4.setText(translate("Calc", "4"))
        self.division.setText(translate("Calc", "÷"))
        self.multiplication.setText(translate("Calc", "×"))
        self.subtraction.setText(translate("Calc", "-"))
        self.addition.setText(translate("Calc", "+"))
        self.output.setText(translate("Calc", "Output"))



class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Calc()
        self.ui.setupUi(self)
        self.ui.num_1.clicked.connect(lambda: self.NumBut(1))
        self.ui.num_2.clicked.connect(lambda: self.NumBut(2))
        self.ui.num_3.clicked.connect(lambda: self.NumBut(3))
        self.ui.num_4.clicked.connect(lambda: self.NumBut(4))
        self.ui.num_5.clicked.connect(lambda: self.NumBut(5))
        self.ui.num_6.clicked.connect(lambda: self.NumBut(6))
        self.ui.num_7.clicked.connect(lambda: self.NumBut(7))
        self.ui.num_8.clicked.connect(lambda: self.NumBut(8))
        self.ui.num_9.clicked.connect(lambda: self.NumBut(9))
        self.ui.num_0.clicked.connect(lambda: self.NumBut(0))
        self.ui.p_i.clicked.connect(lambda: self.NumBut(3.14))
        self.ui.factorial.clicked.connect(self.Factor)
        self.ui.clear.clicked.connect(self.Clear)
        self.ui.result.clicked.connect(self.Operation)
        self.ui.root.clicked.connect(self.Root)
        self.ui.delete.clicked.connect(self.Delete)
        self.ui.subtraction.clicked.connect(lambda: self.NumBut("-"))
        self.ui.addition.clicked.connect(lambda: self.NumBut("+"))
        self.ui.multiplication.clicked.connect(lambda: self.NumBut("×"))
        self.ui.division.clicked.connect(lambda: self.NumBut("÷"))

    def Operation(self):
        minus = "-"
        plus = "+"
        spliT = "÷"
        multiplication = "×"
        Compare = self.ui.input.text()
        if minus in Compare:
            s = Compare.split("-")
            n = float(s[0])
            n1 = float(s[1])
            f = float(n - n1)
            self.ui.input.setText(str(floor(f)))

        elif plus in Compare:
            s = Compare.split("+")
            n = float(s[0])
            n1 = float(s[1])
            f = float(n + n1)
            self.ui.input.setText(str(floor(f)))

        elif spliT in Compare:
            s = Compare.split("÷")
            n = float(s[0])
            n1 = float(s[1])
            f = float(n / n1)
            self.ui.input.setText(str(floor(f)))

        elif multiplication in Compare:
            s = Compare.split("×")
            n = float(s[0])
            n1 = float(s[1])
            f = float(n * n1)
            self.ui.input.setText(str(floor(f)))
        self.ui.output.setText(self.ui.input.text())
        self.ui.input.clear()

    def Result(self):
        self.ui.output.setText(self.ui.input.text())
        self.ui.input.clear()

    def Clear(self):
        self.ui.input.clear()

    def Factor(self):
        N = factorial(int(self.ui.input.text()))
        print(N)
        self.ui.input.setText(str(N))

    def NumBut(self, num):
        v = str(num)
        self.ui.input.setText(self.ui.input.text() + v)

    def Root(self):
        N = sqrt(int(self.ui.input.text()))
        print(N)
        self.ui.input.setText(str(N))

    def Delete(self):
        a = self.ui.input.text()
        a = a[:-1]
        self.ui.input.setText(a)


app = QApplication(sys.argv)
wd = Window()
wd.show()
sys.exit(app.exec_())
