import pyodbc
from entities import Category


cnxn_str = ("Driver={SQL Server};"
            "Server=LAPTOP-SC5IAURS;"
            "Database=University Library;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()

def get_all_categories():
    cursor.execute('SELECT * FROM Category')
    category_List = []
    for row in cursor:
        row_to_list = [elem for elem in row]
        category = Category(row_to_list[0],row_to_list[1])
        category_List.append(category)

    return category_List

clist =  get_all_categories()

print(clist[0].name)

#kda el comment
#msh sam3enk
#ma ana 3rfaaaaaaaaaaa
#mashii 😂
#wow 👌