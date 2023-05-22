import pyodbc
import entities
import datetime
import random
def connect_database():
    cnxn_str = ("Driver={SQL Server};"
                "Server=LAPTOP-SC5IAURS;"
                "Database=University Library;"
                "Trusted_Connection=yes;")
    cnxn = pyodbc.connect(cnxn_str)

    cursor = cnxn.cursor()
    return cursor

cursor = connect_database()

def get_all_categories():
    cursor.execute('SELECT * FROM Category')
    category_List = []
    for row in cursor:
        row_to_list = [elem for elem in row]
        category = entities.Category(row_to_list[0],row_to_list[1])
        category_List.append(category)

    return category_List


def search_by_category(category_name):
    cursor.execute(f"SELECT isbn , c.name , title , publicationyear,author  FROM book , category as c WHERE c.categoryid = book.categoryid and c.name like '%{category_name}%'")
    book_List = []
    for row in cursor:
        row_to_list = [elem for elem in row]
        book = entities.BookWithCategory(row_to_list[0],row_to_list[1],row_to_list[2],row_to_list[3],row_to_list[4])
        book_List.append(book)
    return book_List


def add_book(book):
    #search if the category exists
    cursor.execute(f"SELECT * FROM category WHERE name = '{book.categoryName}'")
    row = cursor.fetchone()
    id = None

    if not row:
        #if not add it
        id = add_category(book.categoryName)
    else:   
        #if exists get the id
        row_to_list = [elem for elem in row]
        id = row_to_list[0]

    bookID = random.randint(1,10000)
    
    cursor.execute(f"INSERT INTO book (bookid,isbn,categoryid,title,publicationyear,author) VALUES ('{bookID}','{book.ISBN}','{id}','{book.title}','{book.year}','{book.author}')")
    cursor.commit()

def add_category(categoryName):
    id = random.randint(1,1000)
    cursor.execute(f"INSERT INTO category (categoryid,name) VALUES ('{id}','{categoryName}')")
    cursor.commit()
    return id

def update_book(book):
    cursor.execute(f"UPDATE book SET isbn = '{book.ISBN}', categoryid = '{book.categoryid}', title = '{book.title}', publicationyear = '{book.Publication_year}', author = '{book.author}' WHERE bookid = '{book.id}'")
    cursor.commit()

def update_user(user):
    cursor.execute(f"UPDATE \"USER\" SET firstname = '{user.firstname}', lastname = '{user.lastname}', email = '{user.email}', password = '{user.password}', role = {user.role} WHERE userid = '{user.id}'")
    if user.role == 'STUDENT':
        cursor.execute(f"UPDATE student SET year = '{user.year}' WHERE userid = '{user.id}'")
    cursor.commit()



def borrow_book(book_id, user_id,book_isbn):
    start_date = datetime.datetime.now()
    end = start_date + datetime.timedelta(days=30)
    current_date = start_date.strftime("%Y-%m-%d")
    end_date = end.strftime("%Y-%m-%d")
    cursor.execute(f"INSERT INTO borrow (bookid,isbn, userid,borrowdate,returndate) VALUES ('{book_id}','{book_isbn}','{user_id}', '{current_date}', '{end_date}')")
    cursor.commit()

def search_book_by_title(title):
    cursor.execute(f"SELECT isbn , c.name , title , publicationyear,author  FROM book , category as c WHERE c.categoryid = book.categoryid and title like '%{title}%'")
    book_List = []
    for row in cursor:
        row_to_list = [elem for elem in row]
        book = entities.BookWithCategory(row_to_list[0],row_to_list[1],row_to_list[2],row_to_list[3],row_to_list[4])
        book_List.append(book)

    return book_List

def search_book_by_author(author):
    cursor.execute(f"SELECT isbn , c.name , title , publicationyear,author  FROM book , category as c WHERE c.categoryid = book.categoryid and author like '%{author}%'")
    book_List = []
    for row in cursor:
        row_to_list = [elem for elem in row]
        book = entities.BookWithCategory(row_to_list[0],row_to_list[1],row_to_list[2],row_to_list[3],row_to_list[4])
        book_List.append(book)

    return book_List

def search_book_by_isbn(isbn):
    cursor.execute(f"SELECT isbn , c.name , title , publicationyear,author  FROM book , category as c WHERE c.categoryid = book.categoryid and isbn like '%{isbn}%'")
    book_List = []
    for row in cursor:
        row_to_list = [elem for elem in row]
        book = entities.BookWithCategory(row_to_list[0],row_to_list[1],row_to_list[2],row_to_list[3],row_to_list[4])
        book_List.append(book)
    return book_List

def search_book_by_publication_year(publication_year):
    cursor.execute(f"SELECT isbn , c.name , title , publicationyear,author  FROM book , category as c WHERE c.categoryid = book.categoryid and publicationyear like '%{publication_year}%'")
    book_List = []
    for row in cursor:
        row_to_list = [elem for elem in row]
        book = entities.BookWithCategory(row_to_list[0],row_to_list[1],row_to_list[2],row_to_list[3],row_to_list[4])
        book_List.append(book)

    return book_List



def validate_signup_email(email):
    cursor.execute(f"SELECT * FROM \"USER\" WHERE email = '{email}'")
    row = cursor.fetchone()
    
    if not row:
        return True
    else:
        return False



def sign_up_admin(user):
    if validate_signup_email(user.email):
        print(user.id)
        cursor.execute(f"INSERT INTO \"USER\" (userid,firstname,lastname,email,password,role) VALUES ('{user.id}','{user.firstname}','{user.lastname}','{user.email}','{user.password}','ADMIN')")
        cursor.commit()
    else:
        print("Email already exists")


def sign_up_student(user):
    if validate_signup_email(user.email):
        cursor.execute(f"INSERT INTO \"USER\" (userid,firstname,lastname,email,password,role) VALUES ({user.id},'{user.firstname}','{user.lastname}','{user.email}','{user.password}','STUDENT')")
        cursor.execute(f"INSERT INTO student (userid,year) VALUES ({user.id},'{user.year}')")
        cursor.commit()
    else:
        print("Email already exists")

def validate_login(email, password):
    cursor.execute(f"SELECT * FROM \"USER\" WHERE email = '{email}' AND password = '{password}'")
    row = cursor.fetchone()
    
    if not row:
        return False
    else:
        row_to_list = [elem for elem in row]
        user = None
        if row_to_list[5] == 'ADMIN':
            user = entities.User(row_to_list[0], row_to_list[1], row_to_list[2], row_to_list[3], row_to_list[4], row_to_list[5])
        else:
            cursor.execute(f"SELECT * FROM student WHERE userid = '{row_to_list[0]}'")
            row = cursor.fetchone()
            student_to_list = [elem for elem in row]
            user = entities.Student(row_to_list[0], row_to_list[1], row_to_list[2], row_to_list[3], row_to_list[4], row_to_list[5], student_to_list[1])
        return user
        

def numbers_of_books_borrowed(user_id):
    cursor.execute(f"SELECT COUNT(*) FROM borrow WHERE userid = '{user_id}'")
    for row in cursor:
        return row[0]

def add_copy(book_id,book_isbn):
    copy_id = random.randint(1,10000)
    cursor.execute(f"INSERT INTO copy (bookid,isbn,copyid) VALUES ('{book_id}','{book_isbn}','{copy_id}')")
    cursor.commit()

def delete_book(book_id):
    cursor.execute(f"DELETE FROM copy WHERE bookid = '{book_id}'")
    cursor.commit()
    cursor.execute(f"DELETE FROM book WHERE bookid = '{book_id}'")
    cursor.commit()

def delete_copy(book_id):
    cursor.execute(f"select copyid from copy where bookid = '{book_id}'")
    row = cursor.fetchone()
    copy_id = None
    for row in cursor:
        row_to_list = [elem for elem in row]
        copy_id = row_to_list[0]
        break
    cursor.execute(f"DELETE FROM copy WHERE copyid = '{copy_id}'")
    cursor.commit()

def update_copy(book_id,new_number_of_copies,number_of_copies,book_isbn):
    if new_number_of_copies > number_of_copies:
        for i in range(number_of_copies,new_number_of_copies):
            add_copy(book_id,book_isbn)
    elif new_number_of_copies < number_of_copies:
        for i in range(new_number_of_copies,number_of_copies):
            delete_copy(book_id)
    


def get_all_copies(book_id):
    total_copies = 0
    cursor.execute(f"SELECT COUNT(*) FROM copy as c WHERE c.bookid = '{book_id}'")
    for row in cursor:
        total_copies = row[0]

    return total_copies

def get_all_borrowed_copies(book_id):
    total_borrowed_copies = 0
    cursor.execute(f"SELECT COUNT(*) FROM borrow as b WHERE b.bookid = '{book_id}' And b.returndate > GETDATE()")
    for row in cursor:
        total_borrowed_copies = row[0]

    return total_borrowed_copies

def count_available_copies(book_id):
    total_copies = 0
    total_copies=get_all_copies(book_id)
    total_borrowed_copies = 0
    total_borrowed_copies=get_all_borrowed_copies(book_id)  
    return total_copies - total_borrowed_copies

def get_all_books():
    cursor.execute('SELECT isbn , c.name , title , publicationyear,author  FROM book , category as c WHERE c.categoryid = book.categoryid')
    book_List = []
    for row in cursor:
        row_to_list = [elem for elem in row]
        book = entities.BookWithCategory(row_to_list[0],row_to_list[1],row_to_list[2],row_to_list[3],row_to_list[4])
        book_List.append(book)
    print(book_List)
    return book_List


def get_book_to_edit(isbn):
    cursor.execute(f"SELECT bookid, isbn , c.name , title , publicationyear,author  FROM book , category as c WHERE c.categoryid = book.categoryid and isbn = '{isbn}'")
    book_List = []
    id = 0
    book = None
    for row in cursor:
        row_to_list = [elem for elem in row]
        id = row_to_list[0]
        book = entities.BookWithCategory(row_to_list[1],row_to_list[2],row_to_list[3],row_to_list[4],row_to_list[5])
    
    return book, id


#software id->6

# c = entities.Category(3,"Horror")
# add_category(c)

# c = entities.Category(10,"Math")
# add_category(c)

# book = entities.Book(20,3456,6,"modern c++",2020,"robet")
# add_book(book)
# book = entities.Book(44,3564,3,"Dracula",2019,"michel")
# add_book(book)

# book = entities.Book(100,45664,10,"Math 2",2020,"michel")
# add_book(book)

# li = get_all_category_books(6)
# for i in li:    
#     print(i.title)




# borrow_book(6,22,1223)
# borrow_book(6,10,1223)

# print(count_available_copies(6))




# (userid,firstname,lastname,email,password,role) VALUES ('10','shahd','salah','unicorn@gmail.com','123456','ADMIN')