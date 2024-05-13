from db_connector import connect_db, Error
from db_fetch import fetch_all_users, fetch_all_books


def add_user():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            user_name = input("What is new user's name: ").title()
            email = input("What is new user's email: ")

            new_user = (user_name, email)

            query = "INSERT INTO users (name, email) VALUES (%s, %s);"

            cursor.execute(query, new_user)
            conn.commit()
            print(f"{user_name} added successfully to users!")
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def add_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            book_title = input("What is the  book title:  ").title()
            isbn_number = input("What is your the thirteen digit ISBN number: ") 
            pub_date = input('What is the publiction date of the book: ') 

            new_book = (book_title, isbn_number, pub_date)

            query = "INSERT INTO books (title, isbn, publication_date ) VALUES (%s, %s, %s)"

            cursor.execute(query, new_book)
            conn.commit()
            print(f"{book_title} added successfully to library!")
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
