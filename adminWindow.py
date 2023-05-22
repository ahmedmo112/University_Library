from PyQt5 import QtCore, QtGui, QtWidgets
import Controller
import entities

class Ui_AdminHomeWindow(object):
    def setAddBookBG(self,MainWindow):
        
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-image: url(\"assets/add_book.png\");\n"
"background-position: top left;\n"
"background-repeat: no-repeat;\n"
"background-size: cover;\n"
"}")
        
    def setProfileBG(self, MainWindow):
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-image: url(\"assets/personal_details_1.png\");\n"
"background-position: top left;\n"
"background-repeat: no-repeat;\n"
"background-size: cover;\n"
"}")

    def setEditBookBG(self, MainWindow):
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-image: url(\"assets/edit_book.png\");\n"
"background-position: top left;\n"
"background-repeat: no-repeat;\n"
"background-size: cover;\n"
"}")
    def setBrowseBG(self, MainWindow):
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-image: url(\"assets/plain.png\");\n"
"background-position: top left;\n"
"background-repeat: no-repeat;\n"
"background-size: cover;\n"
"}")

    

    def setupUi(self, MainWindow):
     
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 675)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-image: url(\"assets/plain.png\");\n"
"background-position: top left;\n"
"background-repeat: no-repeat;\n"
"background-size: cover;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_book_widget = QtWidgets.QWidget(self.centralwidget)
        self.add_book_widget.setGeometry(QtCore.QRect(0, 120, 1201, 521))
        self.add_book_widget.setObjectName("add_book_widget")
        self.book_name_input = QtWidgets.QLineEdit(self.add_book_widget)
        self.book_name_input.setGeometry(QtCore.QRect(112, 43, 374, 53))
        self.book_name_input.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #062b98;\n"
"    border-radius: 20;\n"
"    padding: 15px;\n"
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
        self.book_name_input.setPlaceholderText("")
        self.book_name_input.setObjectName("book_name_input")
        self.author_name_input = QtWidgets.QLineEdit(self.add_book_widget)
        self.author_name_input.setGeometry(QtCore.QRect(112, 133, 374, 53))
        self.author_name_input.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #062b98;\n"
"    border-radius: 20;\n"
"    padding: 15px;\n"
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
        self.author_name_input.setPlaceholderText("")
        self.author_name_input.setObjectName("author_name_input")
        self.year_input = QtWidgets.QLineEdit(self.add_book_widget)
        self.year_input.setGeometry(QtCore.QRect(112, 221, 374, 53))
        self.year_input.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #062b98;\n"
"    border-radius: 20;\n"
"    padding: 15px;\n"
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
        self.year_input.setPlaceholderText("")
        self.year_input.setObjectName("year_input")
        self.isbn_input = QtWidgets.QLineEdit(self.add_book_widget)
        self.isbn_input.setGeometry(QtCore.QRect(112, 307, 374, 53))
        self.isbn_input.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #062b98;\n"
"    border-radius: 20;\n"
"    padding: 15px;\n"
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
        self.isbn_input.setPlaceholderText("")
        self.isbn_input.setObjectName("isbn_input")
        self.category_input = QtWidgets.QLineEdit(self.add_book_widget)
        self.category_input.setGeometry(QtCore.QRect(112, 398, 374, 53))
        self.category_input.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #062b98;\n"
"    border-radius: 20;\n"
"    padding: 15px;\n"
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
        self.category_input.setPlaceholderText("")
        self.category_input.setObjectName("category_input")
        self.add_apply_button = QtWidgets.QPushButton(self.add_book_widget)
        self.add_apply_button.setGeometry(QtCore.QRect(112, 470, 375, 50))
        self.add_apply_button.setStyleSheet("QPushButton{\n"
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
        self.add_apply_button.setObjectName("add_apply_button")
        self.add_book_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_book_button.setGeometry(QtCore.QRect(439, 68, 138, 39))
        self.add_book_button.setStyleSheet("QPushButton {\n"
"        background-color: transparent;\n"
"        border: none;\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"text-decoration: underline;\n"
"    }")
        self.add_book_button.setText("")
        self.add_book_button.setObjectName("add_book_button")
        self.edit_profile = QtWidgets.QPushButton(self.centralwidget)
        self.edit_profile.setGeometry(QtCore.QRect(604, 68, 138, 39))
        self.edit_profile.setStyleSheet("QPushButton {\n"
"        background-color: transparent;\n"
"        border: none;\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"text-decoration: underline;\n"
"    }")
        self.edit_profile.setText("")
        self.edit_profile.setObjectName("edit_profile")
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setGeometry(QtCore.QRect(751, 68, 138, 39))
        self.browse_button.setStyleSheet("QPushButton {\n"
"        background-color: transparent;\n"
"        border: none;\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"text-decoration: underline;\n"
"    }")
        self.browse_button.setText("")
        self.browse_button.setObjectName("browse_button")
        self.edit_book_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_book_button.setGeometry(QtCore.QRect(881, 68, 138, 39))
        self.edit_book_button.setStyleSheet("QPushButton {\n"
"        background-color: transparent;\n"
"        border: none;\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"text-decoration: underline;\n"
"    }")
        self.edit_book_button.setText("")
        self.edit_book_button.setObjectName("edit_book_button")
        self.browse_widget = QtWidgets.QWidget(self.centralwidget)
        self.browse_widget.setGeometry(QtCore.QRect(0, 120, 1201, 521))
        self.browse_widget.setObjectName("browse_widget")
        self.search_input = QtWidgets.QLineEdit(self.browse_widget)
        self.search_input.setEnabled(True)
        self.search_input.setGeometry(QtCore.QRect(333, 66, 530, 60))
        self.search_input.setStyleSheet("QLineEdit {\n"
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
        self.search_input.setPlaceholderText("")
        self.search_input.setObjectName("search_input")
        self.search_apply = QtWidgets.QPushButton(self.browse_widget)
        self.search_apply.setGeometry(QtCore.QRect(759, 66, 108, 60))
        self.search_apply.setStyleSheet("QPushButton{\n"
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
        self.search_apply.setObjectName("search_apply")
        self.radio_by_isbn = QtWidgets.QRadioButton(self.browse_widget)
        self.radio_by_isbn.setGeometry(QtCore.QRect(360, 140, 95, 20))
        self.radio_by_isbn.setStyleSheet("QRadioButton {\n"
"    color: #f7f9fe;\n"
"    color: #062b98;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"\n"
"}")
        self.radio_by_isbn.setObjectName("radio_by_isbn")
        self.radio_by_name = QtWidgets.QRadioButton(self.browse_widget)
        self.radio_by_name.setGeometry(QtCore.QRect(460, 140, 95, 20))
        self.radio_by_name.setStyleSheet("QRadioButton {\n"
"    color: #f7f9fe;\n"
"    color: #062b98;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"\n"
"}")
        self.radio_by_name.setObjectName("radio_by_name")
        self.radio_by_author = QtWidgets.QRadioButton(self.browse_widget)
        self.radio_by_author.setGeometry(QtCore.QRect(550, 140, 95, 20))
        self.radio_by_author.setStyleSheet("QRadioButton {\n"
"    color: #f7f9fe;\n"
"    color: #062b98;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"\n"
"}")
        self.radio_by_author.setObjectName("radio_by_author")
        self.radio_by_year = QtWidgets.QRadioButton(self.browse_widget)
        self.radio_by_year.setGeometry(QtCore.QRect(650, 140, 95, 20))
        self.radio_by_year.setStyleSheet("QRadioButton {\n"
"    color: #f7f9fe;\n"
"    color: #062b98;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"\n"
"}")
        self.radio_by_year.setObjectName("radio_by_year")
        self.radio_by_category = QtWidgets.QRadioButton(self.browse_widget)
        self.radio_by_category.setGeometry(QtCore.QRect(740, 140, 121, 20))
        self.radio_by_category.setStyleSheet("QRadioButton {\n"
"    color: #f7f9fe;\n"
"    color: #062b98;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"\n"
"}")
        self.radio_by_category.setObjectName("radio_by_category")
        self.treeWidget = QtWidgets.QTreeWidget(self.browse_widget)
        self.treeWidget.setGeometry(QtCore.QRect(90, 170, 1021, 331))
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setObjectName("treeWidget")
        self.edit_bookt_widget = QtWidgets.QWidget(self.centralwidget)
        self.edit_bookt_widget.setGeometry(QtCore.QRect(0, 120, 1201, 621))
        self.edit_bookt_widget.setObjectName("edit_bookt_widget")
        self.isbn_input_2 = QtWidgets.QLineEdit(self.edit_bookt_widget)
        self.isbn_input_2.setEnabled(True)
        self.isbn_input_2.setGeometry(QtCore.QRect(100, 60, 430, 60))
        self.isbn_input_2.setStyleSheet("QLineEdit {\n"
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
        self.isbn_input_2.setPlaceholderText("")
        self.isbn_input_2.setObjectName("isbn_input_2")
        self.find_book_apply = QtWidgets.QPushButton(self.edit_bookt_widget)
        self.find_book_apply.setGeometry(QtCore.QRect(550, 60, 171, 60))
        self.find_book_apply.setStyleSheet("QPushButton{\n"
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
        self.find_book_apply.setObjectName("find_book_apply")
        self.book_details_widget = QtWidgets.QWidget(self.edit_bookt_widget)
        self.book_details_widget.setGeometry(QtCore.QRect(0, 130, 1201, 451))
        self.book_details_widget.setObjectName("book_details_widget")
        self.book_name_label = QtWidgets.QLabel(self.book_details_widget)
        self.book_name_label.setGeometry(QtCore.QRect(334, 25, 311, 16))
        self.book_name_label.setStyleSheet("QLabel {\n"
"\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"\n"
"    }")
        self.book_name_label.setObjectName("book_name_label")
        self.author_label = QtWidgets.QLabel(self.book_details_widget)
        self.author_label.setGeometry(QtCore.QRect(334, 69, 291, 16))
        self.author_label.setStyleSheet("QLabel {\n"
"\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"\n"
"    }")
        self.author_label.setObjectName("author_label")
        self.year_label = QtWidgets.QLabel(self.book_details_widget)
        self.year_label.setGeometry(QtCore.QRect(334, 113, 361, 16))
        self.year_label.setStyleSheet("QLabel {\n"
"\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"\n"
"    }")
        self.year_label.setObjectName("year_label")
        self.isbn_label = QtWidgets.QLabel(self.book_details_widget)
        self.isbn_label.setGeometry(QtCore.QRect(334, 157, 231, 16))
        self.isbn_label.setStyleSheet("QLabel {\n"
"\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"\n"
"    }")
        self.isbn_label.setObjectName("isbn_label")
        self.category_label = QtWidgets.QLabel(self.book_details_widget)
        self.category_label.setGeometry(QtCore.QRect(334, 201, 531, 21))
        self.category_label.setStyleSheet("QLabel {\n"
"\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"\n"
"    }")
        self.category_label.setObjectName("category_label")
        self.copies_label = QtWidgets.QLabel(self.book_details_widget)
        self.copies_label.setGeometry(QtCore.QRect(380, 245, 55, 21))
        self.copies_label.setStyleSheet("QLabel {\n"
"\n"
"        color: #062b98;\n"
"            font-size: 18px;\n"
"            font-family: Arial, sans-serif;\n"
"\n"
"    }")
        self.copies_label.setObjectName("copies_label")
        self.add_copy_btn = QtWidgets.QPushButton(self.book_details_widget)
        self.add_copy_btn.setGeometry(QtCore.QRect(334, 240, 30, 30))
        self.add_copy_btn.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    background-color: #062b98;\n"
"    color: #f7f9fe;\n"
"    font-size: 20px;\n"
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
        self.add_copy_btn.setObjectName("add_copy")
        self.remove_copy_btn = QtWidgets.QPushButton(self.book_details_widget)
        self.remove_copy_btn.setGeometry(QtCore.QRect(440, 240, 30, 30))
        self.remove_copy_btn.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    background-color: #062b98;\n"
"    color: #f7f9fe;\n"
"    font-size: 20px;\n"
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
        self.remove_copy_btn.setObjectName("remove_copy")
        self.apply_edit_button = QtWidgets.QPushButton(self.book_details_widget)
        self.apply_edit_button.setGeometry(QtCore.QRect(100, 290, 171, 60))
        self.apply_edit_button.setStyleSheet("QPushButton{\n"
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
        self.apply_edit_button.setObjectName("apply_edit_button")
        self.delete_book_button = QtWidgets.QPushButton(self.book_details_widget)
        self.delete_book_button.setGeometry(QtCore.QRect(320, 290, 171, 60))
        self.delete_book_button.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    background-color: #b51818;\n"
"    color: #f7f9fe;\n"
"    font-size: 16px;\n"
"    font-family: Arial, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #770e0e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #071d54;\n"
"}\n"
"")
        self.delete_book_button.setObjectName("delete_book_button")
        self.edit_profile_widget = QtWidgets.QWidget(self.centralwidget)
        self.edit_profile_widget.setGeometry(QtCore.QRect(0, 120, 1201, 551))
        self.edit_profile_widget.setObjectName("edit_profile_widget")
        self.signup_email = QtWidgets.QLineEdit(self.edit_profile_widget)
        self.signup_email.setGeometry(QtCore.QRect(100, 164, 429, 60))
        self.signup_email.setStyleSheet("QLineEdit {\n"
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
        self.signup_email.setPlaceholderText("")
        self.signup_email.setObjectName("signup_email")
        self.first_name = QtWidgets.QLineEdit(self.edit_profile_widget)
        self.first_name.setEnabled(True)
        self.first_name.setGeometry(QtCore.QRect(100, 63, 195, 60))
        self.first_name.setStyleSheet("QLineEdit {\n"
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
        self.first_name.setPlaceholderText("")
        self.first_name.setObjectName("first_name")
        self.password_input_3 = QtWidgets.QLineEdit(self.edit_profile_widget)
        self.password_input_3.setGeometry(QtCore.QRect(100, 364, 429, 60))
        self.password_input_3.setStyleSheet("QLineEdit {\n"
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
        self.password_input_3.setPlaceholderText("")
        self.password_input_3.setObjectName("password_input_3")
        self.last_name = QtWidgets.QLineEdit(self.edit_profile_widget)
        self.last_name.setEnabled(True)
        self.last_name.setGeometry(QtCore.QRect(334, 63, 195, 60))
        self.last_name.setStyleSheet("QLineEdit {\n"
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
        self.last_name.setPlaceholderText("")
        self.last_name.setObjectName("last_name")
        self.signup_password = QtWidgets.QLineEdit(self.edit_profile_widget)
        self.signup_password.setGeometry(QtCore.QRect(100, 265, 429, 60))
        self.signup_password.setStyleSheet("QLineEdit {\n"
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
        self.signup_password.setPlaceholderText("")
        self.signup_password.setObjectName("signup_password")
        self.login_button = QtWidgets.QPushButton(self.edit_profile_widget)
        self.login_button.setGeometry(QtCore.QRect(100, 449, 430, 58))
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
        self.add_book_widget.raise_()
        self.add_book_button.raise_()
        self.edit_profile.raise_()
        self.browse_button.raise_()
        self.edit_book_button.raise_()
        self.edit_profile_widget.raise_()
        self.edit_bookt_widget.raise_()
        self.browse_widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.edit_bookt_widget.hide()
        self.add_book_widget.hide()
        self.edit_profile_widget.hide()



        self.retranslateUi(MainWindow)


        self.edit_profile.clicked.connect(lambda: self.setProfileBG(MainWindow)) # type: ignore
        self.add_book_button.clicked.connect(lambda: self.setAddBookBG(MainWindow)) # type: ignore
        self.edit_book_button.clicked.connect(lambda: self.setEditBookBG(MainWindow)) # type: ignore
        self.browse_button.clicked.connect(lambda: self.setBrowseBG(MainWindow)) # type: ignore
        self.add_book_button.clicked.connect(self.add_book_widget.show) # type: ignore


        self.add_book_button.clicked.connect(self.edit_bookt_widget.hide) # type: ignore
        self.add_book_button.clicked.connect(self.browse_widget.hide) # type: ignore
        self.edit_profile.clicked.connect(self.add_book_widget.hide) # type: ignore
  
        self.edit_profile.clicked.connect(self.edit_bookt_widget.hide) # type: ignore
        self.edit_profile.clicked.connect(self.browse_widget.hide) # type: ignore
        self.browse_button.clicked.connect(self.browse_widget.show) # type: ignore
        self.browse_button.clicked.connect(self.add_book_widget.hide) # type: ignore
        self.browse_button.clicked.connect(self.edit_bookt_widget.hide) # type: ignore
        self.edit_book_button.clicked.connect(self.edit_bookt_widget.show) # type: ignore
        self.edit_book_button.clicked.connect(self.add_book_widget.hide) # type: ignore
        self.edit_book_button.clicked.connect(self.browse_widget.hide) # type: ignore
        self.edit_profile.clicked.connect(self.edit_profile_widget.show) # type: ignore
        self.add_book_button.clicked.connect(self.edit_profile_widget.hide) # type: ignore
        self.browse_button.clicked.connect(self.edit_profile_widget.hide) # type: ignore
        self.edit_book_button.clicked.connect(self.edit_profile_widget.hide) # type: ignore
        self.find_book_apply.clicked.connect(self.book_details_widget.hide) # type: ignore # was showed
        self.edit_book_button.clicked.connect(self.book_details_widget.hide) # type: ignore
        self.browse_button.clicked.connect(self.book_details_widget.hide) # type: ignore
        self.edit_profile.clicked.connect(self.book_details_widget.hide) # type: ignore
        self.add_book_button.clicked.connect(self.book_details_widget.hide) # type: ignore
        self.apply_edit_button.clicked.connect(self.book_details_widget.hide) # type: ignore
        self.delete_book_button.clicked.connect(self.book_details_widget.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.search_apply.clicked.connect(self.search) # type: ignore
        self.add_apply_button.clicked.connect(self.add_book) # type: ignore
        self.find_book_apply.clicked.connect(self.get_edit_book) # type: ignore
        self.apply_edit_button.clicked.connect(self.update_copies) # type: ignore
        self.remove_copy_btn.clicked.connect(self.remove_copy) # type: ignore
        self.add_copy_btn.clicked.connect(self.add_copy) # type: ignore
        self.delete_book_button.clicked.connect(self.delete_book) # type: ignore

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_apply_button.setText(_translate("MainWindow", "Add New Book"))
        self.search_apply.setText(_translate("MainWindow", "Search"))
        self.radio_by_isbn.setText(_translate("MainWindow", "By isbn"))
        self.radio_by_name.setText(_translate("MainWindow", "By name"))
        self.radio_by_author.setText(_translate("MainWindow", "By author"))
        self.radio_by_year.setText(_translate("MainWindow", "By year"))
        self.radio_by_category.setText(_translate("MainWindow", "By category"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "ISBN"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Author"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Year"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Category"))
        self.find_book_apply.setText(_translate("MainWindow", "Find Book"))
        self.book_name_label.setText(_translate("MainWindow", "book"))
        self.author_label.setText(_translate("MainWindow", "author"))
        self.year_label.setText(_translate("MainWindow", "year"))
        self.isbn_label.setText(_translate("MainWindow", "isbn"))
        self.category_label.setText(_translate("MainWindow", "category"))
        self.copies_label.setText(_translate("MainWindow", "copies"))
        self.add_copy_btn.setText(_translate("MainWindow", "+"))
        self.remove_copy_btn.setText(_translate("MainWindow", "-"))
        self.apply_edit_button.setText(_translate("MainWindow", "Apply"))
        self.delete_book_button.setText(_translate("MainWindow", "Delete Book"))
        self.login_button.setText(_translate("MainWindow", "Update Personal Details"))
        self.get_all_books()
        self.radio_by_isbn.setChecked(True)


    def get_all_books(self):
        books = Controller.get_all_books()
        self.treeWidget.clear()
        for book in books:
                item = QtWidgets.QTreeWidgetItem(self.treeWidget)
                item.setText(0, book.title)
                item.setText(1, str(book.ISBN))
                item.setText(2, book.author)
                item.setText(3, str(book.year))
                item.setText(4, book.categoryName)

    def search(self):
        books = []
        if not self.search_input.text():
                return self.get_all_books()
        if self.radio_by_isbn.isChecked():
            books = Controller.search_book_by_isbn(self.search_input.text().lower())
        elif self.radio_by_name.isChecked():
            books = Controller.search_book_by_title(self.search_input.text().lower())
        elif self.radio_by_author.isChecked():
            books = Controller.search_book_by_author(self.search_input.text().lower())
        elif self.radio_by_year.isChecked():
            books = Controller.search_book_by_publication_year(self.search_input.text().lower())
        elif self.radio_by_category.isChecked():
            books = Controller.search_by_category(self.search_input.text().lower())
        else:
            return self.get_all_books()
        self.treeWidget.clear()
        for book in books:
            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item.setText(0, book.title)
            item.setText(1, str(book.ISBN))
            item.setText(2, book.author)
            item.setText(3, str(book.year))
            item.setText(4, book.categoryName)

    def add_book(self):
        title = self.book_name_input.text().lower()
        author = self.author_name_input.text().lower()
        year = self.year_input.text().lower()
        isbn = self.isbn_input.text().lower()
        category = self.category_input.text().lower()
        if not title or not author or not year or not isbn or not category :
            return

        book = entities.BookAdded(isbn, category, title, year, author)
        Controller.add_book(book)
        #show message box
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Book added successfully")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()
        self.book_name_input.setText("")
        self.author_name_input.setText("")
        self.year_input.setText("")
        self.isbn_input.setText("")
        self.category_input.setText("")

        self.get_all_books()

    book_id_edit = 0
    num_of_copies = 0

    def get_edit_book(self):
        isbn = self.isbn_input_2.text().lower()

        if not isbn:
            return
        book,self.book_id_edit = Controller.get_book_to_edit(isbn)
        self.num_of_copies = Controller.get_all_copies(self.book_id_edit)
        if not book:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error", "Book not found")
            return
        self.book_name_label.setText(book.title)
        self.author_label.setText(book.author)
        self.year_label.setText(str(book.year))
        self.isbn_label.setText(str(book.ISBN))
        self.category_label.setText(book.categoryName)
        self.copies_label.setText(str(self.num_of_copies))
        self.book_details_widget.show()

    def add_copy(self):
        
        isbn = self.isbn_input_2.text().lower()
        if not isbn:
            return
        self.copies_label.setText(str(int(self.copies_label.text())+1))

       

    def remove_copy(self):
        if int(self.copies_label.text()) == 0:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error", "No copies to remove")
            return
        isbn = self.isbn_input_2.text().lower()
        if not isbn:
            return
        self.copies_label.setText(str(int(self.copies_label.text())-1))
        
        
    def delete_book(self):
        isbn = self.isbn_input_2.text().lower()
        if not isbn:
            return
        Controller.delete_book(self.book_id_edit)
        
    def update_copies(self):
        isbn = self.isbn_input_2.text().lower()
        if not isbn:
            return
        Controller.update_copy(self.book_id_edit, int(self.copies_label.text()),self.num_of_copies, isbn)
        
        
    
        
        

     

