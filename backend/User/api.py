import ast
from models import SessionLocal,User
from flask import request,jsonify
from blueprint import BLUEPRINT

def serialize(row):
    return {
        "id" : str(row.id),
        "username" : row.username,
        "email" : row.email,
        "admin":row.is_admin
    } 

api_method=BLUEPRINT('api', __name__)

@api_method.route("/",methods=["GET"])
def home():
    return {"hello":"Hello World"}

@api_method.route("/login",methods=["POST"])
def login_request():
    username=request.json['username']
    password=request.json['password']
    session=SessionLocal()
    try:
        user=session.query(User).filter_by(username=username).first()
        if user:
            if user.verify_password(password):
                return {"data":f"{user.email} is loggedinn successfully"}
            else:
                return {"Error":f"Password does not match"}
        else:
            return {"Error":f"User is not registered"}
    except Exception as e:
        return {"failed":f"Error: {e}"}
    finally:
        session.close()

@api_method.route("/register",methods=["POST"])
def register_request():
    username=request.json['username']
    password=request.json['password']
    email=request.json['email']
    admin=request.json['admin']
    admin=ast.literal_eval(admin)
    session=SessionLocal()
    try:
        new_user=User(email=email,hashed_password=password,is_active=True,is_admin=admin,username=username)
        session.add(new_user)
        session.commit()
        return {"data":f"{username} is created successfully"}
    except Exception as e:
        return {"failed":f"Error: {e}"}
    finally:
        session.close()
    
@api_method.route("/user/<int:id>",methods=["PUT"])
def user_request(id):
    session=SessionLocal()
    try:
        user=session.query(User).filter_by(id=id).first()
        if user:
            return {"data":f"Email: {user.email} Username:{user.username} Admin:{user.is_admin} ActiveUser:{user.is_active}"}
        else:
            return {"Error":f"No user with id {id}"}
    except Exception as e:
        return {"failed":f"Error: {e}"}
    finally:
        session.close()

@api_method.route("/deleteuser/<int:id>",methods=["DELETE"])
def delete_request(id):
    session=SessionLocal()
    try:
        user=session.query(User).filter_by(id=id).first()
        if user:
            session.delete(user)
            session.commit()
            return {"Success":f"User with id {id} deleted successfully"}
            
        else:
            return {"Error":f"No user with id {id}"}
    except Exception as e:
        return {"failed":f"Error: {e}"}
    finally:
        session.close()   

@api_method.route("/userslist",methods=["GET"])
def users_request():
    session=SessionLocal()
    # all_users=session.query(User).all()
    all_users=""
    if all_users:
        users = [serialize(x) for x in all_users]
        return jsonify({"data":users})
    else:
        return jsonify({"data":""})