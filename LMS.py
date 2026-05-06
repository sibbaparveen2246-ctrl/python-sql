# import 
import mysql.connector as myconn

# connection
mydb = myconn.connect(
    host = 'localhost',
    user = 'root',
    password = 'Your_Password',
    database = 'Library_db'
)

# cursor
db_cursor = mydb.cursor()

# database
db_cursor.execute('CREATE DATABASE IF NOT EXISTS Library_db')
db_cursor.execute('USE Library_db')

# Table
db_cursor.execute("""CREATE TABLE IF NOT EXISTS Library(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
author VARCHAR(100),
status VARCHAR(50))
""")

# Add_Book!
def add_book():
    name = input('Enter Name of Book:')
    author = input('Enter Name of Author:')

    query = "INSERT INTO Library (name,author,status) Values (%s,%s,%s)"
    db_cursor.execute(query,(name,author,'available'))
    mydb.commit()
    print('Book Added Successfully!')

# View_Book!
def view_book():
    db_cursor.execute("SELECT * FROM Library")
    all_book = db_cursor.fetchall()

    print('\n LIST OF BOOKS!')
    for i in all_book:
        print(f"id:{i[0]}, name:{i[1]}, author:{i[2]}, status:{i[3]}")

# Issue_Book!
def issue_book():
    book_id = input('Enter Book ID:')
    query = "UPDATE Library SET status=%s WHERE id=%s"
    db_cursor.execute(query,('issued',book_id))
    mydb.commit()
    print('Book Issued Successfully!')

# Return_Book!
def return_book():
    book_id = input('Enter Book Id:')
    query = "UPDATE Library SET status=%s WHERE id=%s"
    db_cursor.execute(query,('available',book_id))
    mydb.commit()
    print('Book Returned Successfully!')

# Delete_Book!
def delete_book():
    book_id = input('Book id:')
    query = "DELETE FROM Library WHERE id=%s"
    db_cursor.execute(query,(book_id,))
    mydb.commit()
    print('Book Deleted Successfully!')

# menu page
while True:
    print("\n LIBRARY MANAGEMENT SYSTEM WELCOME")
    print("1. ADD BOOK")
    print("2. VIEW BOOK")
    print("3. ISSUE BOOK")
    print("4. RETURN BOOK")
    print("5. DELETE BOOK")
    print("6. EXIT")

    choice = input('Enter Your Choice:')
    if choice == '1':
        add_book()
    elif choice == '2':
        view_book()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        delete_book()
    else:
        print('Exit.....Closing Program')    
    
# connection close
mydb.close()