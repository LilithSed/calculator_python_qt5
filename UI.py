# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt5_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setFixedWidth(409)
        Calculator.setFixedHeight(390)
        Calculator.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.screen = QtWidgets.QLabel(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(5, 5, 400, 78))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.screen.setFont(font)
        self.screen.setAcceptDrops(False)
        self.screen.setAutoFillBackground(False)
        self.screen.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.screen.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.screen.setIndent(-1)
        self.screen.setObjectName("screen")
        self.button_percentage = QPushButton(self.centralwidget)
        self.button_percentage.setGeometry(QtCore.QRect(210, 90, 91, 53))
        self.button_percentage.setStyleSheet("QPushButton{\n"
                                             "    font: 16pt \"MS Sans Serif\";\n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             "    border-style: outset;\n"
                                             "    border-width: 0px;\n"
                                             "    border-radius: 6px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: rgb(244, 244, 244);\n"
                                             "}\n"
                                             "")
        self.button_percentage.setObjectName("button_percentage")
        self.pushButton_AC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AC.setGeometry(QtCore.QRect(10, 90, 91, 53))
        self.pushButton_AC.setStyleSheet("QPushButton{\n"
                                         "    font: 16pt \"MS Sans Serif\";\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    border-style: outset;\n"
                                         "    border-width: 0px;\n"
                                         "    border-radius: 6px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: rgb(244, 244, 244);\n"
                                         "}")
        self.pushButton_AC.setObjectName("pushButton_AC")
        self.pushButton_MR = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_MR.setGeometry(QtCore.QRect(110, 90, 91, 53))
        self.pushButton_MR.setStyleSheet("QPushButton{\n"
                                         "    font: 16pt \"MS Sans Serif\";\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    border-style: outset;\n"
                                         "    border-width: 0px;\n"
                                         "    border-radius: 6px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: rgb(244, 244, 244);\n"
                                         "}")
        self.pushButton_MR.setObjectName("pushButton_MR")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(310, 90, 91, 53))
        self.pushButton_divide.setStyleSheet("QPushButton{\n"
                                             "    font: 16pt \"MS Sans Serif\";\n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             "    border-style: outset;\n"
                                             "    border-width: 0px;\n"
                                             "    border-radius: 6px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: rgb(244, 244, 244);\n"
                                             "}")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 150, 91, 53))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "    font: 16pt \"MS Sans Serif\";\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0px;\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(244, 244, 244);\n"
                                        "}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 150, 91, 53))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "    font: 16pt \"MS Sans Serif\";\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0px;\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(244, 244, 244);\n"
                                        "}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 150, 91, 53))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
                                        "    font: 16pt \"MS Sans Serif\";\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0px;\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(244, 244, 244);\n"
                                        "}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_multiplication = QtWidgets.QPushButton(
            self.centralwidget)
        self.pushButton_multiplication.setGeometry(
            QtCore.QRect(310, 150, 91, 53))
        self.pushButton_multiplication.setStyleSheet("QPushButton{\n"
                                                     "    font: 16pt \"MS Sans Serif\";\n"
                                                     "    background-color: rgb(255, 255, 255);\n"
                                                     "    border-style: outset;\n"
                                                     "    border-width: 0px;\n"
                                                     "    border-radius: 6px;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover{\n"
                                                     "    background-color: rgb(244, 244, 244);\n"
                                                     "}")
        self.pushButton_multiplication.setObjectName(
            "pushButton_multiplication")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 210, 91, 53))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    font: 16pt \"MS Sans Serif\";\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0px;\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(244, 244, 244);\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 210, 91, 53))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "    font: 16pt \"MS Sans Serif\";\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0px;\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(244, 244, 244);\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 210, 91, 53))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "    font: 16pt \"MS Sans Serif\";\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0px;\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(244, 244, 244);\n"
                                        "}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(310, 210, 91, 53))
        self.pushButton_minus.setStyleSheet("QPushButton{\n"
                                            "    font: 16pt \"MS Sans Serif\";\n"
                                            "    background-color: rgb(255, 255, 255);\n"
                                            "    border-style: outset;\n"
                                            "    border-width: 0px;\n"
                                            "    border-radius: 6px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: rgb(244, 244, 244);\n"
                                            "}")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 270, 91, 53))
        self.pushButton_1.setStyleSheet("QPushButton{\n"
                                        "    font: 16pt \"MS Sans Serif\";\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0px;\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(244, 244, 244);\n"
                                        "}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 270, 91, 53))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    font: 16pt \"MS Sans Serif\";\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0px;\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(244, 244, 244);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 270, 91, 53))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    font: 16pt \"MS Sans Serif\";\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0px;\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(244, 244, 244);\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(310, 270, 91, 53))
        self.pushButton_plus.setStyleSheet("QPushButton{\n"
                                           "    font: 16pt \"MS Sans Serif\";\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    border-style: outset;\n"
                                           "    border-width: 0px;\n"
                                           "    border-radius: 6px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "    background-color: rgb(244, 244, 244);\n"
                                           "}")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_positiveNegative = QtWidgets.QPushButton(
            self.centralwidget)
        self.pushButton_positiveNegative.setGeometry(
            QtCore.QRect(10, 330, 91, 53))
        self.pushButton_positiveNegative.setStyleSheet("QPushButton{\n"
                                                       "    font: 16pt \"MS Sans Serif\";\n"
                                                       "    background-color: rgb(255, 255, 255);\n"
                                                       "    border-style: outset;\n"
                                                       "    border-width: 0px;\n"
                                                       "    border-radius: 6px;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:hover{\n"
                                                       "    background-color: rgb(244, 244, 244);\n"
                                                       "}")
        self.pushButton_positiveNegative.setObjectName(
            "pushButton_positiveNegative")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(110, 330, 91, 53))
        self.pushButton_0.setStyleSheet("QPushButton{\n"
                                        "    font: 16pt \"MS Sans Serif\";\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 0px;\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(244, 244, 244);\n"
                                        "}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(210, 330, 91, 53))
        self.pushButton_dot.setStyleSheet("QPushButton{\n"
                                          "    font: 16pt \"MS Sans Serif\";\n"
                                          "    background-color: rgb(255, 255, 255);\n"
                                          "    border-style: outset;\n"
                                          "    border-width: 0px;\n"
                                          "    border-radius: 6px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: rgb(244, 244, 244);\n"
                                          "}")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(310, 330, 91, 53))
        self.pushButton_equal.setStyleSheet("QPushButton{\n"
                                            "    font: 16pt \"MS Sans Serif\";\n"
                                            "    background-color: rgb(129, 114, 78);\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    border-style: outset;\n"
                                            "    border-width: 0px;\n"
                                            "    border-radius: 6px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: rgb(147, 130, 89);\n"
                                            "}")
        self.pushButton_equal.setObjectName("pushButton_equal")
        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.screen.setText(_translate("Calculator", "0"))
        self.button_percentage.setText(_translate("Calculator", "%"))
        self.pushButton_AC.setText(_translate("Calculator", "AC"))
        self.pushButton_MR.setText(_translate("Calculator", "MR"))
        self.pushButton_divide.setText(_translate("Calculator", "÷"))
        self.pushButton_7.setText(_translate("Calculator", "7"))
        self.pushButton_8.setText(_translate("Calculator", "8"))
        self.pushButton_9.setText(_translate("Calculator", "9"))
        self.pushButton_multiplication.setText(_translate("Calculator", "x"))
        self.pushButton_4.setText(_translate("Calculator", "4"))
        self.pushButton_5.setText(_translate("Calculator", "5"))
        self.pushButton_6.setText(_translate("Calculator", "6"))
        self.pushButton_minus.setText(_translate("Calculator", "-"))
        self.pushButton_1.setText(_translate("Calculator", "1"))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_plus.setText(_translate("Calculator", "+"))
        self.pushButton_positiveNegative.setText(
            _translate("Calculator", "+/-"))
        self.pushButton_0.setText(_translate("Calculator", "0"))
        self.pushButton_dot.setText(_translate("Calculator", "."))
        self.pushButton_equal.setText(_translate("Calculator", "="))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
