import sqlite3


CREATE_COFFEE_SHOPS_TABLE = """
CREATE TABLE IF NOT EXISTS coffee_shops
(id INTEGER PRIMARY KEY, name TEXT,location TEXT, 
specialized_bean TEXT ,FOREIGN KEY(specialized_bean) REFERENCES beans(name));
"""

FOREIGN_KEY = "PRAGMA foreign_keys = ON"

INSERT_SHOP = "INSERT INTO coffee_shops (name,location,specialized_bean) VALUES (?,?,?);"

GET_ALL_SHOPS = "SELECT * FROM coffee_shops;"

GET_SHOPS_BY_NAME = "SELECT * FROM coffee_shops WHERE name = ?;"

DELETE_SHOP = "DELETE FROM coffee_shops WHERE id = ?;"

GET_SHOP_BY_SPECIALIZED_BEAN = """
SELECT * FROM coffee_shops
WHERE specialized_bean = ?
;"""

def connect():
    return sqlite3.connect("database.db")

def foreign_key(connection):
    with connection:
        connection.execute(FOREIGN_KEY)


def create_tables(connection):
    with connection:
        connection.execute(CREATE_COFFEE_SHOPS_TABLE)
    
def add_shop(connection,name,location,specialized_bean):
    with connection:
        connection.execute(INSERT_SHOP,(name,location,specialized_bean))

def get_all_shops(connection):
    with connection:
        return connection.execute(GET_ALL_SHOPS).fetchall()

def get_shops_by_name(connection, name):
    with connection:
        return connection.execute(GET_SHOPS_BY_NAME, (name,)).fetchall()

def shop_for_specialized_bean(connection, specialized_bean):
    with connection:
        return connection.execute(GET_SHOP_BY_SPECIALIZED_BEAN,(specialized_bean,)).fetchall()

def delete_shop(connection, shop_id):
    with connection:
        connection.execute(DELETE_SHOP, (shop_id,))