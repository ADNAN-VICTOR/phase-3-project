import Bean_model

MENU_PROMPT="""
-- Coffee Bean App --

Please choose one of these options:

1) View coffee beans.
2) View Coffee shops
3) Exit.

Your selection: """

BEAN_MENU = """
-- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection: """

def menu():
    connection = Bean_model.connect()
    Bean_model.create_tables(connection)

    while(user_input := input(MENU_PROMPT)) != "3":
        if user_input == "1":
            bean_menu()
        elif user_input == "2":
            pass
        else:
            print("Invalid input, please try again.")

def bean_menu():
    connection = Bean_model.connect()
    Bean_model.create_tables(connection)
    while(user_input := input(BEAN_MENU)) != "5":
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


def add_bean(connection):
    name = input("Enter bean name: ")
    method = input("Enter how you've prepared it: ")
    rating = int(input("Enter your rating score (0-100): "))
    Bean_model.add_bean(connection,name, method, rating)

def get_all_beans(connection):
    beans = Bean_model.get_all_beans(connection)
    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")

def find_bean(connection):
    name = input("Enter bean name to find: ")
    beans = Bean_model.get_beans_by_name(connection, name)

    for bean in beans:
        print (f"{bean[1]} ({bean[2]}) - {bean[3]}/100")

def find_best_method(connection):
    name = input("Enter bean name to find: ")
    best_method = Bean_model.best_preparation_for_bean(connection,name)

    print(f"The best preparation method for {name} is {best_method[2]} ")


menu()