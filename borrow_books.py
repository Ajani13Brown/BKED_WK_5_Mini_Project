from db_connector import connect_db, Error
from db_fetch import fetch_all_users


def view_available_books():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = 'SELECT * FROM books WHERE availability = 1 ;'
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f'Book ID: {row[0]} Title: {row[1]}')

        finally:
            cursor.close()
            conn.close()

def book_unavailable(book):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            available = 0

            new_availability = (available,book)

            query = 'UPDATE books SET availability = %s WHERE id = %s;'

            cursor.execute(query, new_availability)
            conn.commit()
            print("Book changed to unavailable")

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()


def checkout_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            fetch_all_users()
            user = int(input('What is your User ID: '))
            
            view_available_books()
            book = int(input('What Book ID would you like to check out: '))

            book_checkout = (user,book)

            query = "INSERT INTO borrowed_books (user_id, book_id) VALUES (%s, %s);"

            cursor.execute(query, book_checkout)
            conn.commit()
            print('the title you have selected has been checked out, enjoy!')

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    book_unavailable(book)





