from app.schemas.user import UserCreate
from app.services.user_service import UserService
from app.database.database import SessionLocal
from app.exceptions.user import (
    UserNotFoundError,
    UserAlreadyExistsError
)

user_service = UserService()
db = SessionLocal()

# user1 = UserCreate(
#     name= "Leonel Messi",
#     email= "leonmessi223@gmail.com",
#     password= "LeoMessiGoat"
# )

# result1 = user_service.create_user(db, user1)

# print(result1.id)
# print(result1.name)
# print(result1.email)
# try:
#     result2 = user_service.get_user(db,1)
#     print(result2)
# except UserNotFoundError as error:
#     print("\nCaught custom exception:")
#     print(error)

# try:
#     result3 = user_service.get_user(db,2)
#     print(result3)
# except UserNotFoundError as error:
#     print("\nCaught custom exception:")
#     print(error)

# try:
#     result4 = user_service.get_user(db,3)
#     print(result4)
# except UserNotFoundError as error:
#     print("\nCaught custom exception:")
#     print(error)

# user2 = UserCreate(
#     name= "Christiano Ronaldo",
#     email= "christrongoat",
#     password= "Christialdo223"
# )

# user3 = UserCreate(
#     name = "Andrew Garfield",
#     email = "christrongoat",
#     password= "andrew23garf"
# )

# try:
#     result3 = user_service.update_user(db,3,user3)
#     print("User Detail Update Successful...!!\n")
#     print(result3.id)
#     print(result3.name)
#     print(result3.email)
# except UserAlreadyExistsError as error:
#     print("\nCaught custom exception:")
#     print(error)

# user4 = UserCreate(
#     name = "King Li",
#     email = "christrongoat",
#     password= "kinglitch@13"
# )

# try:
#     result3 = user_service.update_user(db,4,user4)
#     print("User Detail Update Successful...!!\n")
#     print(result3.id)
#     print(result3.name)
#     print(result3.email)
# except UserAlreadyExistsError as error:
#     print("\nCaught custom exception:")
#     print(error)

result4 = user_service.get_all_user(db)
print(result4)