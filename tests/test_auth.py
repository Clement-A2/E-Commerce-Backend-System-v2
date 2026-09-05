from app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)
from app.services.auth_service import AuthService
from app.database.database import SessionLocal

data = RegisterRequest(
    name="Kevin Geovani",
    email="kevin2geovani@gmail.com",
    password="kevin223geo"
)

auth_service = AuthService()
db = SessionLocal()

# result = auth_service.register(db,data)

# print(result)

# data2 = RegisterRequest(
#     name= "Lamine Yamal",
#     email="kevin2geovani@gmail.com",
#     password="lamine234yam"
# )

# resul2 = auth_service.register(db,data2)

data3 = LoginRequest(
    email= "kevin2geovani@gmail.com",
    password= "kevin223geo"
)

result3 = auth_service.login(db,data3)
print(result3)

data4 = LoginRequest(
    email= "kevin2geovani@gmail.com",
    password= "lamine234yam"
)

# result4 = auth_service.login(db,data4)

data5 = LoginRequest(
    email="lamineyamal23@gmail.com",
    password="lamine234yam"
)

result5 = auth_service.login(db,data5)