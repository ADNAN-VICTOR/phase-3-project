import database

MENU_PROMPT="""
-- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection: """

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
           add_bean(connection)

        elif user_input == "2":
           get_all_beans(connection)

        elif user_input == "3":
            find_bean(connection)

        elif user_input == "4":
            find_best_method(connection)
        else:
            print("Invalid input, please try again.")




menu()