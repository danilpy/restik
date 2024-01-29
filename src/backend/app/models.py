import uuid

from sqlalchemy import DECIMAL, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from backend.app.database import Base


class Menu(Base):
    '''Модель меню'''
    __tablename__ = 'menus'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(200), nullable=False, unique=True)
    description = Column(String(500), nullable=False)
    submenus = relationship('Submenu', back_populates='menu', cascade='all, delete')


class Submenu(Base):
    '''Модель подменю.'''
    __tablename__ = 'submenus'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(200), nullable=False, unique=True)
    description = Column(String(500), nullable=False)
    menu_id = Column(UUID(as_uuid=True), ForeignKey('menus.id'))
    menu = relationship('Menu', back_populates='submenus')
    dishes = relationship('Dish', back_populates='submenu', cascade='all, delete')


class Dish(Base):
    '''Модель блюда.'''
    __tablename__ = 'dishes'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(200), nullable=False)
    description = Column(String(500), nullable=False)
    price = Column(DECIMAL(scale=2), nullable=False)
    submenu_id = Column(UUID(as_uuid=True), ForeignKey('submenus.id'))
    submenu = relationship('Submenu', back_populates='dishes')
