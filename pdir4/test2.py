import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(400, 200, 320, 315)
        self.widgets()
        self.show()

    def click(self,num):
        expression = self.label.text()
        self.label.setText(expression+str(num))

    def equal(self):
        expression = self.label.text()
        try:
            ans = eval(expression)
            self.label.setText(str(ans))
        except:
            self.label.setText("Error")

    def clear(self):
        self.label.setText("")

    def back(self):
        expression = self.label.text()
        self.label.setText(expression[:-1])

    def widgets(self):
        self.label = QLabel(self)
        self.label.setGeometry(5, 5, 310, 55)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel" "{" "border : 2px solid black;"
                                 "Background : white;" "}")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 25))

        one = QPushButton("1", self)
        two = QPushButton("2", self)
        three = QPushButton("3", self)
        four = QPushButton("4", self)
        five = QPushButton("5", self)
        six = QPushButton("6", self)
        seven = QPushButton("7", self)
        eight = QPushButton("8", self)
        nine = QPushButton("9", self)
        zero = QPushButton("0", self)
        add = QPushButton("+", self)
        minus = QPushButton("-", self)
        product = QPushButton("*", self)
        div = QPushButton("/", self)
        point = QPushButton(".", self)
        clear = QPushButton("C", self)
        Back = QPushButton("⌫", self)
        equal = QPushButton("=", self)

        one.setFont(QFont('Arial', 15))
        two.setFont(QFont('Arial', 15))
        three.setFont(QFont('Arial', 15))
        four.setFont(QFont('Arial', 15))
        five.setFont(QFont('Arial', 15))
        six.setFont(QFont('Arial', 15))
        seven.setFont(QFont('Arial', 15))
        eight.setFont(QFont('Arial', 15))
        nine.setFont(QFont('Arial', 15))
        zero.setFont(QFont('Arial', 15))
        add.setFont(QFont('Arial', 15))
        minus.setFont(QFont('Arial', 15))
        product.setFont(QFont('Arial', 15))
        div.setFont(QFont('Arial', 15))
        point.setFont(QFont('Arial', 15))
        clear.setFont(QFont('Arial', 15))
        Back.setFont(QFont('Arial', 15))
        equal.setFont(QFont('Arial', 15))

        one.setGeometry(5, 120, 70, 40)
        two.setGeometry(85, 120, 70, 40)
        three.setGeometry(165, 120, 70, 40)
        four.setGeometry(5, 170, 70, 40)
        five.setGeometry(85, 170, 70, 40)
        six.setGeometry(165, 170, 70, 40)
        seven.setGeometry(5, 220, 70, 40)
        eight.setGeometry(85, 220, 70, 40)
        nine.setGeometry(165, 220, 70, 40)
        zero.setGeometry(5, 270, 70, 40)
        add.setGeometry(245, 70, 70, 40)
        minus.setGeometry(245, 120, 70, 40)
        product.setGeometry(245, 170, 70, 40)
        div.setGeometry(245, 220, 70, 40)
        point.setGeometry(85, 270, 70, 40)
        clear.setGeometry(5, 70, 110, 40)
        Back.setGeometry(125, 70, 110, 40)
        equal.setGeometry(165, 270, 150, 40)

        one.clicked.connect(lambda : self.click(1))
        two.clicked.connect(lambda : self.click(2))
        three.clicked.connect(lambda : self.click(3))
        four.clicked.connect(lambda : self.click(4))
        five.clicked.connect(lambda : self.click(5))
        six.clicked.connect(lambda : self.click(6))
        seven.clicked.connect(lambda : self.click(7))
        eight.clicked.connect(lambda : self.click(8))
        nine.clicked.connect(lambda : self.click(9))
        zero.clicked.connect(lambda : self.click(0))
        add.clicked.connect(lambda : self.click("+"))
        minus.clicked.connect(lambda : self.click("-"))
        product.clicked.connect(lambda : self.click("*"))
        div.clicked.connect(lambda : self.click("/"))
        point.clicked.connect(lambda : self.click("."))
        clear.clicked.connect(self.clear)
        Back.clicked.connect(self.back)
        equal.clicked.connect(self.equal)

CalculatorApp = QApplication(sys.argv)
window = Window()
sys.exit(CalculatorApp.exec())