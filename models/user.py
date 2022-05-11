import sqlite3

class User:
    def __init__(self,_id, username, password):
        self.id = _id
        self.useranme = username
        self.password = password 
        
    def find_by_username(self,username):
        connection = sqlite3.connect("databse.db")
        cursor = connection.cursor()
        
        search_query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(search_query, (username,))
        row = result.fetchone()
        if row:
            user = User(row[0], row[1], row[2])
        else:
            user = None
        
        connection.close()
        return user

    def find_by_userid(self, id):
        connection = sqlite3.connect("databse.db")
        cursor = connection.cursor()
        
        search_query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(search_query, (id,))
        row = result.fetchone()
        if row:
            user = User(row[0], row[1], row[2])
        else:
            user = None
        connection.close()
        return user
 