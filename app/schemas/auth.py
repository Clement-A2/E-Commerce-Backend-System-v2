from pydantic import BaseModel

#_________REGISTRATION_________
class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

class RegisterResponse(BaseModel):
    user_id: int
    status: str

#__________LOGIN_________
class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    user_id: int
    status: str