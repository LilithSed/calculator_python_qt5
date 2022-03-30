from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QSizePolicy
from UI import Ui_Calculator

import sys

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    firstNum = None
    userIsTypingSecondNumber = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Connect buttons
        self.pushButton_0.clicked.connect(lambda: self.when_clicked(self.pushButton_0.text()))
        self.pushButton_1.clicked.connect(lambda: self.when_clicked(self.pushButton_1.text()))
        self.pushButton_2.clicked.connect(lambda: self.when_clicked(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.when_clicked(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.when_clicked(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.when_clicked(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.when_clicked(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.when_clicked(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.when_clicked(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.when_clicked(self.pushButton_9.text()))

        self.pushButton_dot.clicked.connect(self.decimal_clicked)

        self.pushButton_positiveNegative.clicked.connect(self.unary_operation_pressed)
        self.button_percentage.clicked.connect(self.unary_operation_pressed)

        self.pushButton_plus.clicked.connect(lambda: self.binary_operation_pressed(self.pushButton_plus.text()))
        self.pushButton_minus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_multiplication.clicked.connect(self.binary_operation_pressed)
        self.pushButton_divide.clicked.connect(self.binary_operation_pressed)

        self.pushButton_equal.clicked.connect(self.equals_clicked)

        self.pushButton_AC.clicked.connect(self.clear_pressed)
        self.pushButton_MR.clicked.connect(self.clear_pressed)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_multiplication.setCheckable(True)
        self.pushButton_divide.setCheckable(True)

        self.is_equal = False

    def when_clicked(self, number):
        button = self.sender()

        if((self.pushButton_plus.isChecked() or self.pushButton_minus.isChecked() or self.pushButton_multiplication.isChecked() 
                or self.pushButton_divide.isChecked()) and (not self.userIsTypingSecondNumber)):
            newLabel = format(float(button.text()), '.15g')
            self.userIsTypingSecondNumber = True
        else:
            if (('.' in self.screen.text()) and (button.text() == "0")):
                newLabel = format(self.screen.text() + button.text(), '.15')
            else:
                newLabel = format(float(self.screen.text() + button.text()), '.15g')

        self.screen.setText(newLabel)


    def decimal_clicked(self):
        self.screen.setText(self.screen.text() + '.')

    def unary_operation_pressed(self):
        button = self.sender()

        screenNumber = float(self.screen.text())

        if button.text() == '+/-':
            screenNumber = screenNumber * (-1)
        else:  # button text == '%'
            screenNumber = screenNumber * 0.01

        newLabel = format(screenNumber)
        self.screen.setText(newLabel)

    def binary_operation_pressed(self, op):
        button = self.sender()

        self.firstNum = int(self.screen.text())

        button.setChecked(True)

    def equals_clicked(self):

        secondNum = int(self.screen.text())

        if self.pushButton_plus.isChecked():
            screenNumber = self.firstNum + secondNum
            newLabel = format(screenNumber)
            self.screen.setText(newLabel)
            self.pushButton_plus.setChecked(False)
        elif self.pushButton_minus.isChecked():
            screenNumber = self.firstNum - secondNum
            newLabel = format(screenNumber)
            self.screen.setText(newLabel)
            self.pushButton_minus.setChecked(False)
        elif self.pushButton_multiplication.isChecked():
            screenNumber = self.firstNum * secondNum
            newLabel = format(screenNumber)
            self.screen.setText(newLabel)
            self.pushButton_multiplication.setChecked(False)
        elif self.pushButton_divide.isChecked():
            screenNumber = self.firstNum / secondNum
            newLabel = format(screenNumber)
            self.screen.setText(newLabel)
            self.pushButton_divide.setChecked(False)

        self.userIsTypingSecondNumber = False

    def clear_pressed(self):
        self.pushButton_plus.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_multiplication.setChecked(False)
        self.pushButton_divide.setChecked(False)

        self.userIsTypingSecondNumber = False

        self.screen.setText("0")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    calculator = CalculatorWindow()

    sys.exit(app.exec_())
