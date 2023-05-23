# Description: This file contains the classes that represent the entities of the database.
class Category:
    def __init__(self,id,name):
        self.id = id
        self.name = name


class User:
    def __init__(self,id,email,first_name,last_name,password,role):
        self.id = id
        self.email = email
        self.firstname =  first_name
        self.lastname =  last_name
        self.password = password
        self.role = role

class Student(User):
     def __init__(self,id,email,firstname,lastname,password,role,year):
        super().__init__(id,email,firstname,lastname,password,role)
        self.year =year


class Book:
    def __init__(self,id,ISBN,categoryid,title,Publication_year,author):
        self.id=id
        self.ISBN=ISBN
        self.categoryid=categoryid
        self.title=title
        self.Publication_year=Publication_year
        self.author=author

class BookAdded:
    def __init__(self,ISBN,categoryName,title,year,author):
       
        self.ISBN=ISBN
        self.categoryName=categoryName
        self.title=title
        self.year=year
        self.author=author

class BookWithCategory:
    id = None
    def __init__(self,ISBN,categoryName,title,year,author):
        self.ISBN=ISBN
        self.categoryName=categoryName
        self.title=title
        self.year=year
        self.author=author
        
        
class Copy:
    def __init__(self,id,bookid,ISBN,status):
        self.id=id
        self.status=status 
        self.bookid=bookid
        self.ISBN=ISBN     

class PhoneNumber:
    def __init__(self,id,number):
        self.id=id
        self.number=number

class Borrow:
    def __init__(self,userid,bookid,borrowdate,returndate):
        self.userid=userid
        self.borrowdate=borrowdate    
        self.returndate=returndate
        self.bookid=bookid

class BorrowedBook:
    def __init__(self,bookid,ISBN,bookName,categoryName,startDate,endDate):
        self.bookid=bookid
        self.ISBN=ISBN
        self.bookName=bookName
        self.categoryName=categoryName
        self.startDate=startDate
        self.endDate=endDate
       