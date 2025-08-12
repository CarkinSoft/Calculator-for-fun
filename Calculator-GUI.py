from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog

#Main GUI Class:
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        calcVbox = QVBoxLayout()
        self.resize(300,200)

#Widgets:
        self.mainLabel = QLabel()
        self.subLabel = QLabel()

    #Number Buttom Objects
        self.num1 = QPushButton("1")
        self.num2 = QPushButton("2")
        self.num3 = QPushButton("3")
        self.num4 = QPushButton("4")
        self.num5 = QPushButton("5")
        self.num6 = QPushButton("6")
        self.num7 = QPushButton("7")
        self.num8 = QPushButton("8")
        self.num9 = QPushButton("9")
        self.num0 = QPushButton("0")
        self.sin = QPushButton("sin")
        self.cos = QPushButton("cos")
        self.tan = QPushButton("tan")

    #Operation Button Objects
        self.addButton = QPushButton("+")
        self.subButton = QPushButton("-")
        self.mulButton = QPushButton("*")
        self.divButton = QPushButton("/")
        self.powButton = QPushButton("^")
        self.sqrtButton = QPushButton("sqrt")
        self.parenthesis1Button = QPushButton("(")
        self.parentheses2Button = QPushButton(")")

    #Function Button Objects
        self.clearButton = QPushButton("CE")
        self.equalButton = QPushButton("=")

    #Adding Widgets to GUI Layout
        calcVbox.addWidget(self.mainLabel)
        calcVbox.addWidget(self.subLabel)
        calcVbox.addWidget(self.num1)
        calcVbox.addWidget(self.num2)
        calcVbox.addWidget(self.num3)
        calcVbox.addWidget(self.num4)
        calcVbox.addWidget(self.num5)
        calcVbox.addWidget(self.num6)
        calcVbox.addWidget(self.num7)
        calcVbox.addWidget(self.num8)
        calcVbox.addWidget(self.num9)
        calcVbox.addWidget(self.num0)
        calcVbox.addWidget(self.sin)
        calcVbox.addWidget(self.cos)
        calcVbox.addWidget(self.tan)
        calcVbox.addWidget(self.addButton)
        calcVbox.addWidget(self.subButton)
        calcVbox.addWidget(self.mulButton)
        calcVbox.addWidget(self.divButton)
        calcVbox.addWidget(self.powButton)
        calcVbox.addWidget(self.sqrtButton)
        calcVbox.addWidget(self.parenthesis1Button)
        calcVbox.addWidget(self.parentheses2Button)
        calcVbox.addWidget(self.equalButton)
        calcVbox.addWidget(self.clearButton)
        calcVbox.addWidget(self.equalButton)

        self.setWindowTitle("Calculator")
        self.setLayout(calcVbox)
        self.show()
