import os

from sqlalchemy import Column, Engine, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker

# create engine with env

URL: str = str(os.getenv('DATABASE_URL'))


# define table classes
class Base(DeclarativeBase):
    pass


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    submenu = relationship(
        'SubMenu', cascade='all, delete', backref=('menu'), lazy='dynamic'
    )

    @hybrid_property
    def submenus_in(self):
        return len([s for s in self.submenu])

    @hybrid_property
    def dishes_in(self):
        return sum(s.dishes_in for s in self.submenu)


class SubMenu(Base):
    __tablename__ = 'submenu'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    to_menu = Column(Integer, ForeignKey('menu.id', ondelete='CASCADE'))
    dishes = relationship(
        'Dish', cascade='all, delete', backref=('submenu'), lazy='dynamic'
    )

    @hybrid_property
    def dishes_in(self):
        return len([d for d in self.dishes])


class Dish(Base):
    __tablename__ = 'dish'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    to_submenu = Column(Integer, ForeignKey('submenu.id', ondelete='CASCADE'))


engine: Engine = create_engine(URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
