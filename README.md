This is my Coding Temple Back-end week 5 SQL intergrated library managment system Mini Project.

I have my main library user-friendly command-line-intherface (CLI) in my library_menu.py file this holds my library main menu and all of my seperate menu for each option.
The rest of my files hold the functions to execute the various functionalities of my program.

Add_2_db.py file holds my function to add users and books to my sql database taking in input from the user and constucting columnsin my database.

db_connector.py holds my function that connect to the SQL database and creates my connection object conn.

fetch_db.py holds all my functions to view specific  and display all users and books these functions ask the users for the user id that they with to view with and input function then
pulls that data from the SQL database then display it

borrow_books and return_books.py files hold the functions to borrow/checkout books and return them. for these functions i altered the borrowed_books table to take in a timestamp for the borrow_date and return_date
values and have set the default for borrowed_date to CURRENT TIMESTAMP and return_date to default as Null this was to elimitate the need to pass these values when running the function.
i fave a functions inside the checkout_book and return_book functions to display all eligibility options and to update the avalibility of the book.
