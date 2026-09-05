from app.schemas.auth import (
    RegisterRequest,
    RegisterResponse, 
    LoginRequest, 
    LoginResponse
)
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.password import hash_password, verify_password
from app.exceptions.auth import (
    EmailAlreadyExistsError,
    UserNotFoundError,
    InvalidCredentialsError
)

class AuthService:

    def register(self, db:Session, data:RegisterRequest):
        existing_user = db.query(User).filter(User.email == data.email).first()

        if existing_user:
            raise EmailAlreadyExistsError("User Already Exists...!!\n")

        hashed_password = hash_password(data.password)

        new_user = User(
            name = data.name,
            email = data.email,
            password = hashed_password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return RegisterResponse(
            user_id = new_user.id,
            status="registered successfully"
        )

    def login(self, db:Session, data:LoginRequest):
        existing_user = db.query(User).filter(User.email == data.email).first()

        if existing_user is None:
            raise UserNotFoundError("User does not Exist...!!\n")

        if not verify_password(data.password, existing_user.password):
            raise InvalidCredentialsError("Invalid Password...!!\n")
        
        return LoginResponse(
            user_id=existing_user.id,
            status="logged in successfully"
        )