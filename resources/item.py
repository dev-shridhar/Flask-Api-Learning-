from flask_restful import Resource,reqparse
import sqlite3

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot left blank")
    
            
    def get(self,name):
        conn = sqlite3.connect("items.db")
        cursor = conn.cursor()
        
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        
        conn.close()
        if row:
            return {"item": {"name" : row[0], "price" : row[1]}}
        
        return {"message": "The item you are looking for is not found"}
    
    
    def post(self,name):
        
        data = Item.parser.parse_args()

        conn = sqlite3.connect("items.db")
        cursor = conn.cursor()
        
        query = "INSERT INTO items VALUES(NULL,?,?)"
        cursor.execute(query, (name, data["price"]))
        
        conn.commit()
        conn.close()
        
        return {"item": {"name": name, "price": data["price"]}}
    
    
    def put(self,name):
        data = Item.parser.parse_args()
        
        conn = sqlite3.connect("item.db")
        cursor = conn.cursor()
        
        search_query = "SELECT * FROM items WHERE name=?"
        result = (search_query, (name,))
        row = result.fetchone()
        
        if row: 
            query = "UPDATE items SET price=?"
            cursor.execute(query,(data["price"]))
        else:
            query = "INSERT INTO items VALUES(NULL,?,?)"
            cursor.execute(query, (name, data["price"]))
            
        conn.commit()
        conn.close()
        
        return {"item" : name, "price" : data["price"]}
    
    
    def delete(self,name):
        conn = sqlite3.connect("item.db")
        cursor = conn.cursor()
        
        delete_query = "DELETE FROM items WHERE name=?"
        cursor.execute(delete_query,(name,))
        
        conn.commit()
        conn.close()
        
        return {"message": "item is successfully deleted"}
    
    
class ItemRegister(Resource):
    def get(self):
        conn = sqlite3.connect("item.db")
        cursor = conn.cursor()
        
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        
        items = []
        
        for row in result:
            items.append({"name":row[0], "price": row[1]})
        
        conn.commit()
        conn.close()
        
        return  {"items": items}
        
    
    

    