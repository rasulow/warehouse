from sqlalchemy import *
from datetime import datetime
from sqlalchemy.orm import relationship
from core import Base


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    position = relationship('Position', back_populates='department')
    user = relationship('User', back_populates='department')
    request = relationship('Request', back_populates='department')


class Position(Base):
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id', ondelete='CASCADE'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    department = relationship('Department', back_populates='position')
    user = relationship('User', back_populates='position')
    request = relationship('Request', back_populates='position')


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    staff_id = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id', ondelete='CASCADE'))
    position_id = Column(Integer, ForeignKey('position.id', ondelete='CASCADE'))
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    department = relationship('Department', back_populates='user')
    position = relationship('Position', back_populates='user')
    request = relationship('Request', back_populates='user')


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    item = relationship('Item', back_populates='category')


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, default=None, nullable=True)
    material_number = Column(String, nullable=False)
    vendor = Column(String, nullable=False)
    bin_location = Column(String, nullable=False)
    note = Column(String, nullable=False)
    is_retrieved = Column(Boolean, nullable=False, default=False)
    category_id = Column(ForeignKey('category.id', ondelete='CASCADE'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    category = relationship('Category', back_populates='item')
    image = relationship('Image', back_populates='item')
    request = relationship('Request', back_populates='item')


class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True, index=True)
    src = Column(String, nullable=False)
    item_id = Column(Integer, ForeignKey('item.id', ondelete='CASCADE'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    item = relationship('Item', back_populates='image')


class Request(Base):
    __tablename__ = 'request'
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('item.id', ondelete='CASCADE'))
    department_id = Column(Integer, ForeignKey('department.id', ondelete='CASCADE'), default=3)
    position_id = Column(Integer, ForeignKey('position.id', ondelete='CASCADE'), default=7)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), default=1)
    req_quantity = Column(Integer, nullable=False)
    req_date = Column(Date, nullable=False)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    item = relationship('Item', back_populates='request')
    department = relationship('Department', back_populates='request')
    position = relationship('Position', back_populates='request')
    user = relationship('User', back_populates='request')
    response = relationship('Response', uselist=False, back_populates='request')


class Response(Base):
    __tablename__ = 'response'
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey('request.id', ondelete='CASCADE'), nullable=False)
    status = Column(Integer, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    request = relationship('Request', back_populates='response')
