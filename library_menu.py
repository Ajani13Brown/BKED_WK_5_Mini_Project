import os
import mysql.connector
from add_2_db import add_user , add_book
from db_fetch import fetch_user, fetch_all_users, fetch_book, fetch_all_books
from borrow_books import view_available_books, book_unavailable, checkout_book
from return_book import view_borrowed_books, book_available, book_return


def user_options():
    while True:
        try:
            option = int(input(''' 
                User Options:
            -----------------------
                1. Add a new user
                2. View user details
                3. Display all users
                4. Main Menu
                > '''))
        except ValueError:
            os.system('cls')
            print('Please respond only with numbers!')

        else:
            if option == 1:
                os.system('cls')
                add_user()

            elif option == 2:
                os.system('cls')
                fetch_all_users()
                fetch_user()

            elif option == 3:
                os.system('cls')
                fetch_all_users()

            elif option == 4:
                print('returning to main menu')
                break
            else:
                os.system('cls')
                print(f'Sorry {option} is not a valid option')
                print(f'Let try that again and please respond with only 1,2, 3 or 4')


def book_options():
    while True:
        try:
            option = int(input(''' 
                book Options:
            -----------------------
                1. Add a new book
                2. Borrow a book
                3. Return a book
                4. Search for a book
                5. Display all books
                6. Main Menu
                > '''))
        except ValueError:
            os.system('cls')
            print('Please respond only with numbers')
        
        else:
            if option == 1:
                os.system('cls')
                add_book()

            elif option == 2:
               os.system('cls')
               checkout_book()

            elif option == 3:
                os.system('cls')
                book_return()
            elif option == 4:
                os.system('cls')
                fetch_all_books()
                fetch_book()
            elif option == 5:
                os.system('cls')
                fetch_all_books()

            elif option == 6:
                os.system('cls')
                print('returning to main menu')
                break
            else:
                os.system('cls')
                print(f'Sorry {option} is not a valid option')
                print(f'Let try that again and please respond with only 1, 2, 3, 4, 5 or 6')




def library_menu():
    print( "Welcome to the Library Management System with Database Integration!")
    while True:
        try:
            option = int(input(''' 
                Main Menu:
            ------------------
            1. Book Options
            2. User Options
            3. Exit Library
            > '''))

        except ValueError:
            os.system('cls')
            print('Please respond only with numbers')

        else:
            if option == 1:
                os.system('cls')
                book_options()
            elif option == 2:
                os.system('cls')
                user_options()
            elif option == 3:
                os.system('cls')
                print('Exiting library')
                print('Thank you have a nice day')
                break
            else:
                os.system('cls')
                print(f'Sorry {option} is not a valid option')
                print(f'Let try that again and please respond with only 1,2 or 3')

library_menu()