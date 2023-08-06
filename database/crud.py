# from sqlalchemy import func


from sqlalchemy.orm import Session

from . import database, schemas


class ModelRepository:
    db: Session
    table: type[database.Base]

    async def get_all(self, **kwargs) -> database.Base:
        return self.db.query(self.table).filter_by(**kwargs).all()

    async def get(self, **kwargs) -> database.Base | None:
        return self.db.query(self.table).filter_by(**kwargs).first()

    async def create(self, create_model: schemas.BaseModel) -> database.Base:
        item = self.table(**create_model.model_dump())
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    async def update(
        self, update_model: schemas.BaseModel, **kwargs
    ) -> database.Base | None:
        print(kwargs)
        item = self.db.query(self.table).filter_by(**kwargs).first()
        if item is None:
            return None
        for attr, value in update_model.model_dump().items():
            if value is not None:
                setattr(item, attr, value)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    async def delete(self, **kwargs) -> bool:
        query = self.db.query(self.table).filter_by(**kwargs)
        if query:
            query.delete()
            self.db.commit()
            return True
        return False


class MenuRepository(ModelRepository):
    def __init__(self) -> None:
        self.db: Session = database.get_db()
        self.table: type[database.Menu] = database.Menu


class SubMenuRepository(ModelRepository):
    def __init__(self) -> None:
        self.db: Session = database.get_db()
        self.table: type[database.SubMenu] = database.SubMenu


class DishRepository(ModelRepository):
    def __init__(self) -> None:
        self.db: Session = database.get_db()
        self.table: type[database.Dish] = database.Dish
