from User.models import SessionLocal,User
from User.blueprint import BLUEPRINT
api_method=BLUEPRINT('api', __name__)

@api_method.route("/",methods=["GET"])
def home():
    return {"hello":"Hello World"}

@api_method.route("/login",methods=["POST"])
def login_request():
    return {"hello":"Hello World"}

@api_method.route("/register",methods=["POST"])
def register_request():
    new_user=User("joe@test.com", "hashed_password", True, True, 'joetest')
    session=SessionLocal()
    session.add(new_user)
    session.commit()
    session.close()
    return {"hello":"Hello World"}


@api_method.route("/userslist",methods=["GET"])
def users_request():
    session=SessionLocal()
    all_users=session.query(User).all()
    if all_users:
        return {"hello":f"Hello World {all_users}"}
    else:
        return {"Failed":"No Users Found"}