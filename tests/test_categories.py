from app.schemas.category import CategoryCreate, CategoryResponse
from app.database.database import SessionLocal
from app.services.category_service import CategoryService

cat_service = CategoryService()
db = SessionLocal()

data = CategoryCreate(
    name ="Computers"
)

# result = cat_service.create_category(db, data)
# print(result)

result2 = cat_service.get_category(db,1)
print(result2)

# data2 = CategoryCreate(
#     name="Computer Electronics"
# )

# result3 = cat_service.update_category(db,1,data2)
# print(result3)

# result3 = cat_service.delete_category(db,2)
# print(result3)

result4 = cat_service.get_all_categories(db)
print(result4)