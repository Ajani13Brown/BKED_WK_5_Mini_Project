from db_connector import connect_db, Error

def view_borrowed_books():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = 'SELECT * FROM books WHERE availability = 0 ;'
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f'Book ID: {row[0]} Title: {row[1]}')

        finally:
            cursor.close()
            conn.close()



def book_available(return_book):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            available = 1

            new_availability = (available,return_book)

            query = 'UPDATE books SET availability = %s WHERE id = %s;'

            cursor.execute(query, new_availability)
            conn.commit()
            print("Book changed to available")

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()






def book_return():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            view_borrowed_books()
            return_book = int(input("What is the Book ID of the book you are returning: "))
            query = 'SELECT * FROM borrowed_books WHERE return_date IS NULL;'
            cursor.execute(query)
            for row in cursor.fetchall():
                if row[2] == return_book:
                    update = (row[0],)
                    query = 'UPDATE borrowed_books SET return_date = CURRENT_TIMESTAMP WHERE id = %s;'
                    cursor.execute(query, update)
                    conn.commit()
        finally:
            cursor.close()
            conn.close()
    book_available(return_book)

