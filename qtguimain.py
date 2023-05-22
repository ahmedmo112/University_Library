from PyQt5 import QtCore, QtGui, QtWidgets
from loginWindow import Ui_LoginWindow
from signupWindow import Ui_SignupWindow
from adminWindow import Ui_AdminHomeWindow
import Controller
import entities
import random

class LoginWindow(QtWidgets.QMainWindow):
    switch_to_signup = QtCore.pyqtSignal()
    switch_to_admin_window = QtCore.pyqtSignal()

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.signup_button.clicked.connect(self.switch_to_signup)
        self.ui.login_button.clicked.connect(self.login)

    def login(self):
        email = self.ui.email_input.text()
        password = self.ui.password_input.text()

        data = Controller.validate_login(email, password)
        if not data:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Wrong email or password')
            return
        if email == "admin" and password == "123456":
            self.ui.email_input.setText("")
            self.ui.password_input.setText("")
            self.switch_to_admin_window.emit()

        elif data.role=="ADMIN":
            self.ui.email_input.setText("")
            self.ui.password_input.setText("")
            self.switch_to_admin_window.emit()
            
        elif data.role=="STUDENT":
            self.ui.email_input.setText("")
            self.ui.password_input.setText("")
            self.switch_to_admin_window.emit()

        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Wrong email or password')
         
    
class SignupWindow(QtWidgets.QMainWindow):
    switch_to_login = QtCore.pyqtSignal()
    switch_to_admin_window = QtCore.pyqtSignal()

    def __init__(self):
        super(SignupWindow, self).__init__()
        self.ui = Ui_SignupWindow()
        self.ui.setupUi(self)
        self.ui.login_switch.clicked.connect(self.switch_to_login)
        self.ui.signup_apply.clicked.connect(self.signup)


    def signup(self):
        email = self.ui.signup_email.text()
        password = self.ui.signup_password.text()
        confirm_password = self.ui.confirm_signup_password.text()
        firstname = self.ui.first_name.text()
        lastname = self.ui.last_name.text()
        role = self.ui.admin_radio.isChecked()
        id= random.randint(1,1000)

        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Passwords do not match')
            return


        if role:
            user = entities.User(id,email, firstname, lastname,password,role)
            Controller.sign_up_admin(user)
            self.switch_to_login.emit()
            
        else:
            user = entities.Student(id,email, firstname, lastname,password,role,1)
            Controller.sign_up_student(user)
            self.switch_to_login.emit() # navigate to student window

       

class AdminWindow(QtWidgets.QMainWindow):
    # switch_to_admin_window = QtCore.pyqtSignal()

    def __init__(self):
        super(AdminWindow, self).__init__()
        self.ui = Ui_AdminHomeWindow()
        self.ui.setupUi(self)
        # self.ui.login_button.clicked.connect(self.switch_to_admin_window)

    

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.login_window = LoginWindow()
        self.signup_window = SignupWindow()
        self.admin_window = AdminWindow()

        self.login_window.switch_to_signup.connect(self.newSignupWindow)
        self.signup_window.switch_to_login.connect(self.show_login_window)
        self.login_window.switch_to_admin_window.connect(self.newAdminWindow)
        self.signup_window.switch_to_admin_window.connect(self.newAdminWindow)

        
        self.show_login_window()

    def show_login_window(self):
        if self.centralWidget() is not None:
            self.centralWidget().hide()
        self.setCentralWidget(self.login_window)
        self.login_window.show()

    def newLoginWindow(self):
        self.login_window = LoginWindow()
        self.login_window.switch_to_signup.connect(self.newSignupWindow)
        self.login_window.switch_to_admin_window.connect(self.newAdminWindow)
        self.show_login_window()
    
    def newAdminWindow(self):
        self.admin_window = AdminWindow()
        self.show_admin_window()

    def show_admin_window(self):
        if self.centralWidget() is not None:
            self.centralWidget().hide()
        self.setCentralWidget(self.admin_window)
        self.admin_window.show() 

    def newSignupWindow(self):
        self.signup_window = SignupWindow()
        self.signup_window.switch_to_login.connect(self.newLoginWindow)
        self.show_signup_window()

    def show_signup_window(self):
        if self.centralWidget() is not None:
            self.centralWidget().hide()
        self.setCentralWidget(self.signup_window)
        self.signup_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


