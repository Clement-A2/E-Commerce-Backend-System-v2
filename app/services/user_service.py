from app.schemas.user import UserCreate,UserResponse
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.user import User
from app.utils.password import hash_password
from app.exceptions.user import (
    UserAlreadyExistsError,
    InvalidUserError,
    UserNotFoundError
)

class UserService:

    def create_user(self, db: Session, data: UserCreate):

        existing_user = db.query(User).filter(User.email == data.email).first()

        if existing_user:
            raise UserAlreadyExistsError("User Already Exists...!!")

        hashed_password = hash_password(data.password)

        user = User(
            name= data.name,
            email= data.email,
            password= hashed_password
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    def get_user(self, db: Session, user_id: int):

        found_user = db.query(User).get(user_id)

        if found_user is None:
            raise UserNotFoundError("User Not Found/Does Not Exist...!!")

        return found_user

    def update_user(self, db: Session, user_id: int, data: UserCreate):

        found_user = self.get_user(db,user_id)

        email_availability = db.query(User).filter(and_(User.email == data.email, User.id != user_id)).first()

        if email_availability:
            raise UserAlreadyExistsError("Email Already Exists/Belongs to another User...!!")

        found_user.name = data.name
        found_user.email = data.email

        hashed_password = hash_password(data.password)
        found_user.password = hashed_password

        db.commit()
        db.refresh(found_user)

        return found_user

    def delete_user(self, db: Session, user_id: int):

        found_user = self.get_user(db, user_id)

        db.delete(found_user)
        db.commit()

        return "User Deleted From Records Successfully...!!\n"

    def get_all_user(self, db:Session):

        users = db.query(User).all()

        if not users:
            raise UserNotFoundError("No User(s) Not Found Records...!!")

        return users