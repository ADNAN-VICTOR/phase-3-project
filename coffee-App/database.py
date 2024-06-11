import sqlite3

CREATE_BEANS_TABLE = "CREATE TABLE IF NOT EXISTS beans(id INTEGER PRIMARY KEY, name TEXT,method TEXT,rating INTEGER);"

INSERT_BEAN = "INSERT INTO beans (name,method,rating) VALUES (?,?,?);"

GET_ALL_BEANS = "SELECT * FROM beans;"

GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"

GET_BEST_PREPARATION_FOR_BEAN = """
SELECT * FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""


