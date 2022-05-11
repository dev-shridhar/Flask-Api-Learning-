import sqlite3

conn = sqlite3.connect("databse.db")
cursor = conn.cursor()

create_query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username VARCHAR, password VARCHAR)"
cursor.execute(create_query)

create_table = "CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT, price TEXT)"
cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES (?,?,?)"
users = [
    (1,"sid","asdf"),
    (2,"sis","1234"),
    (3,"bro","7890")
]
cursor.executemany(insert_query, users)

conn.commit()
conn.close()


