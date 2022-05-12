from flask import Flask
from flask_rest import Api
from security import Authenticate, identity
from flask_jwt import JWT
from resources.item import Item, ItemRegister
from resources.user import UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "sid"
api = Api(app)

jwt = JWT(app, Authenticate, identity)



api.add_resource(Item, "/item/<str:name>")
api.add_Resource(ItemRegister,"/itemlist")
api.add_Resource(UserRegister, "/register")


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True) 