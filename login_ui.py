# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 636)
        MainWindow.setStyleSheet("#bg{\n"
"background-color: #4C4C4C;\n"
"}\n"
"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"    font: 9pt \"Arial\";\n"
"\n"
"}\n"
"\n"
"#loginFrame\n"
"{\n"
"background-color: #7A8A8A;\n"
"border-radius:15px;\n"
"}\n"
"QLineEdit\n"
"{\n"
"border-radius:8px;\n"
"padding:3px;\n"
"}\n"
"QPushButton {\n"
"padding:5px;\n"
"border-radius:7px;\n"
"color: rgb(255, 255, 255);\n"
"    font: bold 10pt \"Arial\";\n"
"\n"
"}")
        self.bg = QtWidgets.QWidget(MainWindow)
        self.bg.setObjectName("bg")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.bg)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topFrame = QtWidgets.QFrame(self.bg)
        self.topFrame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.topFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.topFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.topFrame)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setMaximumSize(QtCore.QSize(220, 80))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/images/logo2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.topFrame)
        self.mainFrame = QtWidgets.QFrame(self.bg)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.loginFrame = QtWidgets.QFrame(self.mainFrame)
        self.loginFrame.setMinimumSize(QtCore.QSize(520, 250))
        self.loginFrame.setMaximumSize(QtCore.QSize(16777215, 250))
        self.loginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginFrame.setObjectName("loginFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.loginFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.loginFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("font: bold 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.loginFrame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(30, -1, -1, -1)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMinimumSize(QtCore.QSize(133, 0))
        self.label_3.setMaximumSize(QtCore.QSize(133, 16777215))
        self.label_3.setStyleSheet("font: bold 11pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 28))
        self.lineEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_4.addWidget(self.frame_3, 0, QtCore.Qt.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(self.loginFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(30, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(133, 0))
        self.label_4.setMaximumSize(QtCore.QSize(133, 16777215))
        self.label_4.setStyleSheet("font: bold 11pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 28))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(220, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft)
        self.frame_4 = QtWidgets.QFrame(self.loginFrame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(110, 0))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: #121212;")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_4.addWidget(self.frame_4, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.loginFrame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.bg)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Connexion"))
        self.label_3.setText(_translate("MainWindow", "Adresse mail:"))
        self.label_4.setText(_translate("MainWindow", "Mot de passe:  "))
        self.pushButton.setText(_translate("MainWindow", "Créer un compte"))
        self.pushButton_2.setText(_translate("MainWindow", "OK"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
