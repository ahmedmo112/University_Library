
from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_LoginWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1200, 675)
        MainWindow.setFixedSize(1200, 675)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 675))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 675))
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-image: url(\"assets/bg.png\");\n"
"background-position: top left;\n"
"background-repeat: no-repeat;\n"
"background-size: cover;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(678, 400, 150, 45))
        self.login_button.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    background-color: #062b98;\n"
"    color: #f7f9fe;\n"
"    font-size: 16px;\n"
"    font-family: Arial, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #071d54;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #071d54;\n"
"}\n"
"")
        self.login_button.setObjectName("login_button")
        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setEnabled(True)
        self.email_input.setGeometry(QtCore.QRect(380, 240, 450, 60))
        self.email_input.setStyleSheet("QLineEdit {\n"
"    border: 1.5px solid #062b98;\n"
"    border-radius: 20;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #f7f9fe;\n"
"    font-size: 16px;\n"
"    font: 16px Arial, sans-serif;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #0743d8;\n"
"}\n"
"")
        self.email_input.setObjectName("email_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(380, 323, 450, 60))
        self.password_input.setStyleSheet("QLineEdit {\n"
"    border: 1.5px solid #062b98;\n"
"    border-radius: 20;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #f7f9fe;\n"
"    font-size: 16px;\n"
"    font: 16px Arial, sans-serif;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #0743d8;\n"
"}\n"
"")
        self.password_input.setObjectName("password_input")
        self.signup_button = QtWidgets.QPushButton(self.centralwidget)
        self.signup_button.setGeometry(QtCore.QRect(542, 400, 150, 45))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_button.setStyleSheet("QPushButton {\n"
"        background-color: transparent;\n"
"        border: none;\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"text-decoration: underline;\n"
"    }")
        self.signup_button.setObjectName("signup_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(386, 415, 211, 16))
        self.label.setStyleSheet("QLabel {\n"
"\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"\n"
"    }")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
      

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.email_input.setPlaceholderText(_translate("MainWindow", "Email"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "Password"))
        self.signup_button.setText(_translate("MainWindow", "Signup"))
        self.label.setText(_translate("MainWindow", "Don\'t have an account?"))

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if email == "admin" and password == "123456":
            self.email_input.setText("")
            self.password_input.setText("")
            return True
        else:
            return False
        #     self.hide()
        #     switch_to_admin_home()

        # Add your login logic here
        # data = validate_login(email,password)
        # print(data)
        # if data:
        #     # Successful login
        #     print("Login successful!")
        #     self.email_input.setText("")
        #     self.password_input.setText("")
        #     self.hide()
        #     switch_to_admin_home()
        # else:
        #     msgBox = QtWidgets.QMessageBox()
        #     msgBox.setText("Login Failed")
        #     msgBox.setInformativeText("User email or password is incorrect")
        #     msgBox.setWindowTitle("Login Failed")
        #     msgBox.exec_()

#     def switch_to_signup(self):
#         # self.hide()
#         qtgui.switch_to_signup()

      


