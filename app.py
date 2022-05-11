from flask import Flask
from flask_rest import Api
from security import Authenticate, identity
from flask_jwt import JWT
from resources.item import Item, ItemRegister
from resources.user import UserRegister

app = Flask(__name__)
app.secret_key = "sid"
api = Api(app)

jwt = JWT(app, Authenticate, identity)



api.add_resource(Item, "/item/<str:name>")
api.add_Resource(ItemRegister,"/itemlist")
api.add_Resource(UserRegister, "/register")


if __name__ == "__main__":
    app.run(debug=True) 