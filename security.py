from user import User

def Authenticate(username, password):
    user = User.find_by_username(username)
    if user and user.password == password:
        return user
    
def identity(payload):
    user_id = payload["identity"]
    return User.find_by_userid(user_id)
    