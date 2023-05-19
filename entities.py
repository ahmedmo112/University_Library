


class Category:
    def __init__(self,id,name):
        self.id = id
        self.name = name


class User:
    def __init__(self,id,email,first_name,last_name,password,role):
        self.id = id
        self.email = email
        self.fisrt_name =  first_name
        self.last_name =  last_name
        self.password = password
        self.role = role

class Student(User):
     def __init__(self,id,email,first_name,last_name,password,role,year):
        super().__init__(self,id,email,first_name,last_name,password,role)
        self.year =year


class Book:
    def __init__(self,id,ISBN,title,year,author,quantity,catid):
        self.id=id
        self.ISBN=ISBN
        self.title=title
        self.year=year
        self.author=author
        self.quantity=quantity
        self.catid=catid
        
class Copy:
    def __init__(self,id,userid,bookid,status):
        self.id=id
        self.status=status      

class PhoneNumber:
    def __init__(self,id,number):
        self.id=id
        self.number=number
       