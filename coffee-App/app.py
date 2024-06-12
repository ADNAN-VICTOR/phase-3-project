import Bean_model
import Coffee_shops_model

MENU_PROMPT="""
-- Coffee Bean App --

Please choose one of these options:

1) View coffee beans.
2) View Coffee shops
3) Exit.

Your selection: """

BEAN_MENU = """
-- Coffee Beans --

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Delete a bean.
6) Return to main menu.

Your selection: """

COFFEE_SHOPS = """
-- Coffee Shops --

What would you like to do?
Is it:

1) Add shop?
2) View all coffee shops?
3) View coffee shop by name?
4) View coffee shop by bean?
5) Delete a shop.
6) Return to main menu.

Your selection: """

         #MAIN MENU
def menu():
    con = Coffee_shops_model.connect()
    connection = Bean_model.connect()
    Coffee_shops_model.create_tables(con)
    Bean_model.create_tables(connection)
    while(user_input := input(MENU_PROMPT)) != "3":
        if user_input == "1":
            bean_menu()
        elif user_input == "2":
            coffee_shops_menu()
        else:
            print("Invalid input, please try again.")
 

            #COFFEEE SHOP MENU
def coffee_shops_menu():
    con = Coffee_shops_model.connect()
    Coffee_shops_model.create_tables(con)
    while(user_input := input(COFFEE_SHOPS)) != "6":
        if user_input == "1":
           add_shop(con)

        elif user_input == "2":
           get_all_shops(con)

        elif user_input == "3":
            find_shop(con)

        elif user_input == "4":
            find_shop_by_bean(con)
        elif user_input == "5":
            delete_shop(con)
        else:
            print("Invalid input, please try again.")


def add_shop(con):
    name = input("Enter shop name: ")
    location = input("Enter the location of the shop: ")
    specialized_bean = input("Enter the bean they specialize in: ")
    Coffee_shops_model.add_shop(con, name, location, specialized_bean)
    con.commit() 
    

def get_all_shops(con):
    shops = Coffee_shops_model.get_all_shops(con)
    for shop in shops:
        print(f"{shop[1]} ({shop[2]}) -specializes in {shop[3]}")

def find_shop(con):
    name = input("Enter shop name to find: ")
    shops = Coffee_shops_model.get_shops_by_name(con, name)

    for shop in shops:
        print (f"{shop[1]} located at {shop[2]} -specializes in {shop[3]}")

def find_shop_by_bean(con):
    specialized_bean = input("Enter the bean you want to find a shop for: ")
    shops = Coffee_shops_model.shop_for_specialized_bean(con, specialized_bean)
    if not shops:
        print(f"No shop specializes in {specialized_bean} coffee bean.")
    else:
        for shop in shops:
            print(f"The shop that specializes in {specialized_bean} coffee bean is {shop[1]}")

def delete_shop(con):
    name = input("Enter the name of the shop you want to delete: ")
    shops = Coffee_shops_model.get_shops_by_name(con, name)
    if not shops:
        print(f"No shop named '{name}' found.")
    else:
        for i, shop in enumerate(shops):
            print(f"{i + 1}: {shop[1]} at ({shop[2]}) ")
        selection = input("Enter the number of the shop you want to delete: ")
        try:
            index = int(selection) - 1
            if index < 0 or index >= len(shops):
                print("Invalid selection.")
            else:
                shop_id = shops[index][0]
                Coffee_shops_model.delete_shop(con, shop_id)
                print(f"Bean '{shops[index][1]}' deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a number.")

            # BEAN MENU
def bean_menu():
    connection = Bean_model.connect()
    Bean_model.create_tables(connection)
    while(user_input := input(BEAN_MENU)) != "6":
        if user_input == "1":
           add_bean(connection)

        elif user_input == "2":
           get_all_beans(connection)

        elif user_input == "3":
            find_bean(connection)

        elif user_input == "4":
            find_best_method(connection)
        elif user_input == "5":
            delete_bean(connection)
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


def delete_bean(connection):
    name = input("Enter the name of the bean you want to delete: ")
    beans = Bean_model.get_beans_by_name(connection, name)
    if not beans:
        print(f"No bean named '{name}' found.")
    else:
        for i, bean in enumerate(beans):
            print(f"{i + 1}: {bean[1]} ({bean[2]}) - {bean[3]}/100")
        selection = input("Enter the number of the bean you want to delete: ")
        try:
            index = int(selection) - 1
            if index < 0 or index >= len(beans):
                print("Invalid selection.")
            else:
                bean_id = beans[index][0]
                Bean_model.delete_bean(connection, bean_id)
                print(f"Bean '{beans[index][1]}' deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a number.")


menu()