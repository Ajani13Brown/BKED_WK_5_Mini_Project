from db_connector import connect_db, Error

def fetch_all_users():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = 'SELECT * FROM users;'
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f'User: {row[0]} Name: {row[1]}')

        finally:
            cursor.close()
            conn.close()


def fetch_user():
    conn = connect_db()
    if conn is not None:
        try:
            user_id = int(input("What is the id of the user you're lookin for?: "))
            cursor = conn.cursor()

            query = 'SELECT * FROM users WHERE id = %s;'

            cursor.execute(query, (user_id,))

            row = cursor.fetchall()[0]
            print(f"User ID: {row[0]} Name: {row[1]} Email: {row[2]}")
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()




    


def fetch_all_books():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = 'SELECT * FROM books;'
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f'Book ID: {row[0]} Title: {row[1]}')

        finally:
            cursor.close()
            conn.close()

def fetch_book():
    conn = connect_db()
    if conn is not None:
        try:
            user_id = int(input("What is the id number of the book you're lookin for?: "))
            cursor = conn.cursor()

            query = 'SELECT * FROM books WHERE id = %s;'

            cursor.execute(query, (user_id,))

            row = cursor.fetchall()[0]
            print(f"Book ID: {row[0]} Title: {row[1]} ISBN: {row[2]} Publication Date: {row[3]}")
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

