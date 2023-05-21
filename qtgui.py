from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QPalette , QBrush

# from Controller import validate_login

def window_image(self):
    self.image = QPixmap("bg.png")
    self.palette = QPalette()
    self.palette.setBrush(QPalette.Window, QBrush(self.image))
    self.setPalette(self.palette)
    self.setFixedSize(1200, 675)

def switch_to_login():
    login_window.show()

def switch_to_signup():
    signup_window.show()

def switch_to_admin_home():
    home_window.show()


def switch_to_student_home():
    s_home_window.show()

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
      
        self.setup_ui()

    def setup_ui(self):
        window_image(self)
        self.setWindowTitle('Login')



        self.email_label = QtWidgets.QLabel('email:')
        self.email_input = QtWidgets.QLineEdit()
        self.email_input.setFixedSize(200, 30)

        self.password_label = QtWidgets.QLabel('Password:')
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setFixedSize(200, 30)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_button = QtWidgets.QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        self.login_button.setFixedSize(200, 30)

        self.switch_button = QtWidgets.QPushButton('Switch to Signup')
        self.switch_button.clicked.connect(self.switch_to_signup)
        self.switch_button.setFixedSize(200, 30)

        login_button_layout = QtWidgets.QHBoxLayout()
        login_button_layout.addStretch(1)  # Add a stretchable space to the left
        login_button_layout.addWidget(self.login_button)
        login_button_layout.addStretch(1)

        switch_button_layout = QtWidgets.QHBoxLayout()
        switch_button_layout.addStretch(1)  # Add a stretchable space to the left
        switch_button_layout.addWidget(self.switch_button)
        switch_button_layout.addStretch(1)
      

        layout = QtWidgets.QFormLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addRow(self.email_label, self.email_input)
        layout.addRow(self.password_label, self.password_input)
        layout.addRow(login_button_layout)
        layout.addRow(switch_button_layout)
       

        
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.addStretch(1)  # Add a stretchable space to the left
        horizontal_layout.addLayout(layout)  # Add the form layout
        horizontal_layout.addStretch(1)  # Add a stretchable space to the right

        vertical_layout = QtWidgets.QVBoxLayout(self)
        vertical_layout.addStretch(1)  # Add a stretchable space at the top
        vertical_layout.addLayout(horizontal_layout)  # Add the horizontal layout
        vertical_layout.addStretch(1)  # Add a stretchable space at the bottom

        self.center_window()

    def center_window(self):
        frame_geometry = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())


    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if email == "admin" and password == "123456":
            self.email_input.setText("")
            self.password_input.setText("")
            self.hide()
            switch_to_admin_home()

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

    def switch_to_signup(self):
        self.hide()
        switch_to_signup()





class SignupWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle('Signup')
        window_image(self)

        self.firstname_label = QtWidgets.QLabel('first name:')
        self.firstname_input = QtWidgets.QLineEdit()
        self.firstname_input.setFixedSize(200, 30)

        self.lastname_label = QtWidgets.QLabel('last name:')
        self.lastname_input = QtWidgets.QLineEdit()
        self.lastname_input.setFixedSize(200, 30)

        self.email_label = QtWidgets.QLabel('email:')
        self.email_input = QtWidgets.QLineEdit()
        self.email_input.setFixedSize(200, 30)

        self.password_label = QtWidgets.QLabel('Password:')
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setFixedSize(200, 30)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.confirm_password_label = QtWidgets.QLabel('Confirm Password:')
        self.confirm_password_input = QtWidgets.QLineEdit()
        self.confirm_password_input.setFixedSize(200, 30)
        self.confirm_password_input.setEchoMode(QtWidgets.QLineEdit.Password)


        self.role_label = QtWidgets.QLabel('Role:')
        self.student_radio = QtWidgets.QRadioButton('Student')
        self.admin_radio = QtWidgets.QRadioButton('Admin')
        self.student_radio.setChecked(True) 

        self.signup_button = QtWidgets.QPushButton('Signup')
        self.signup_button.clicked.connect(self.signup)
        self.signup_button.setFixedSize(200, 30)


        self.switch_button = QtWidgets.QPushButton('Switch to Login')
        self.switch_button.clicked.connect(self.switch_to_login)
        self.switch_button.setFixedSize(200, 30)


        signup_button_layout = QtWidgets.QHBoxLayout()
        signup_button_layout.addStretch(1)  # Add a stretchable space to the left
        signup_button_layout.addWidget(self.signup_button)
        signup_button_layout.addStretch(1)

        switch_button_layout = QtWidgets.QHBoxLayout()
        switch_button_layout.addStretch(1)  # Add a stretchable space to the left
        switch_button_layout.addWidget(self.switch_button)
        switch_button_layout.addStretch(1)
      

        layout = QtWidgets.QFormLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addRow(self.firstname_label, self.firstname_input)
        layout.addRow(self.lastname_label, self.lastname_input)
        layout.addRow(self.email_label, self.email_input)
        layout.addRow(self.password_label, self.password_input)
        layout.addRow(self.confirm_password_label, self.confirm_password_input)
        layout.addRow(self.role_label, self.student_radio)
        layout.addRow('', self.admin_radio)
        layout.addRow(signup_button_layout)
        layout.addRow(switch_button_layout)

        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.addStretch(1)  # Add a stretchable space to the left
        horizontal_layout.addLayout(layout)  # Add the form layout
        horizontal_layout.addStretch(1)  # Add a stretchable space to the right

        vertical_layout = QtWidgets.QVBoxLayout(self)
        vertical_layout.addStretch(1)  # Add a stretchable space at the top
        vertical_layout.addLayout(horizontal_layout)  # Add the horizontal layout
        vertical_layout.addStretch(1)  # Add a stretchable space at the bottom

        self.center_window()

    def center_window(self):
        frame_geometry = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def signup(self):
        if self.password_input.text() == self.confirm_password_input.text():
            # Successful signup
            print("Signup successful!")
            print(f"Name: {self.firstname_input.text()} {self.lastname_input.text()}")
            print(f"Email: {self.email_input.text()}")
            if self.student_radio.isChecked():
                print("Role: Student")
            else:
                print("Role: Admin")
            self.hide()
            switch_to_admin_home()

    def switch_to_login(self):
        self.hide()
        switch_to_login()



class AdminHomeWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        window_image(self)
        self.setWindowTitle('Home')

        self.welcome_label = QtWidgets.QLabel('Welcome to the home page!')
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)

        #add book button
        #add category
        #search and browsing
        #br#osingup> dpdate ar deletete profile data
        #view students

        
#        #logout
        #view all students        #ttoozzf enerate report
        

        self.logout_button = QtWidgets.QPushButton('Logout')
        self.logout_button.clicked.connect(self.logout)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.logout_button)

        self.center_window()

    def center_window(self):
        frame_geometry = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def logout(self):
        self.hide()
        switch_to_login()

class StudentHomeWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        window_image(self)
        self.setWindowTitle('Home')

        self.welcome_label = QtWidgets.QLabel('Welcome to the home page!')
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)

        #add book button
        #add category
        #search 
        #brwosing -> update or delete
        #update profile data
        #view students
        #generate report

        

        self.logout_button = QtWidgets.QPushButton('Logout')
        self.logout_button.clicked.connect(self.logout)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.logout_button)

        self.center_window()

    def center_window(self):
        frame_geometry = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def logout(self):
        self.hide()
        switch_to_login()        
import sys
app = QtWidgets.QApplication(sys.argv)

signup_window = SignupWindow()
login_window = LoginWindow()
home_window = AdminHomeWindow()
s_home_window = StudentHomeWindow()
login_window.show()

sys.exit(app.exec_())

