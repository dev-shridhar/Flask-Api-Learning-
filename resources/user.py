import sqlite3
from typing_extensions import Required
from flask_restful import Resource, reqparse
from models.user import User
   
class UserRegister(Resource):
    parser = reqparse.RequestPArser()
    parser.add_argument('username',
                        type = "str",
                        required=True,
                        help="This field cannot be left blank"
                    )
    
    parser.add_argument('password',
                        type = "str",
                        required=True,
                        help="This field cannot left blank"
                    )
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if User.find_by_username(data["username"]):
            return {"message" : "Auser by that name alredy exists"}, 400
        
        conn = sqlite3.connect("databse.db")
        cursor = conn.curosr()
        
        query = "INSERT INTO users VALUES (NULL,?,?)"
        cursor.execute(query, (data["username"], data["passowrd"]))
        
        conn.commit()
        conn.close()
        return {"message" : "User cerated succesfully"}, 201 