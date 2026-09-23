from app.schemas.category import CategoryCreate, CategoryResponse
from sqlalchemy.orm import Session
from app.models.category import Category
from app.exceptions.category import (
    CategoryAlreadyExistsError,
    CategoryNotFoundError
)

class CategoryService:

    def create_category(self, db: Session, data: CategoryCreate):

        existing_category = db.query(Category).filter(Category.name == data.name).first()

        if existing_category:
            raise CategoryAlreadyExistsError("Category Already Exists...!!\n")

        category = Category(
            name=data.name
        )

        db.add(category)
        db.commit()
        db.refresh(category)

        return category

    def get_category(self, db: Session, category_id: int):

        existing_category = db.query(Category).get(category_id)

        if existing_category is None:
            raise CategoryNotFoundError("Category not found...!!\n")

        return existing_category

    def update_category(self, db: Session, category_id: int, data: CategoryCreate):

        existing_category = self.get_category(db,category_id)

        existing_category.name = data.name

        db.commit()
        db.refresh(existing_category)

        return existing_category

    def delete_category(self, db: Session, category_id: int):
        
        existing_category = self.get_category(db, category_id)

        db.delete(existing_category)
        db.commit()

        return "Category Deleted Successfully!!\n"

    def get_all_categories(self, db: Session):

        categories = db.query(Category).all()

        if not categories:
            raise CategoryNotFoundError("No Categories Found in Records...!!\n")

        return categories