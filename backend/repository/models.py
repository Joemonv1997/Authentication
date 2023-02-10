from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash,check_password_hash
from database import database_config
Base,SessionLocal,engine=database_config()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username=Column(String,nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=True)
    def __init__(self,email,hashed_password,is_active,is_admin,username):
        self.username=username
        self.email=email
        self.hashed_password=generate_password_hash(hashed_password)
        self.is_active=is_active
        self.is_admin=is_admin
    def verify_password(self, password):
        return check_password_hash(self.hashed_password, password)
    def __repr__(self):
        return f"User: {self.username}"