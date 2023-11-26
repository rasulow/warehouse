from pydantic import BaseModel
from typing import List
from datetime import date
from typing import Optional


class BaseSchema(BaseModel):
    name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": 'default'
                }
            ]
        }
    }


class PositionSchema(BaseSchema):
    department_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": 'IT',
                    'department_id': 1
                }
            ]
        }
    }


class UserSchema(BaseModel):
    username: str
    password: str
    role: str
    staff_id: int
    department_id: int
    position_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    'username': 'Kakageldiyew Myratgeldi',
                    'password': 'demo',
                    'department_id': 1,
                    'position_id': 1,
                    'role': 'user',
                    'staff_id': '11223344',
                }
            ]
        }
    }


class UserIsDeletedSchema(BaseModel):
    is_deleted: bool


class ItemSchema(BaseModel):
    title: str
    quantity: int
    material_number: str
    vendor: str
    bin_location: str
    note: str
    price: float = None
    is_retrieved: bool = False
    category_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    'title': 'Standart list A4',
                    'quantity': 100,
                    'material_number': 'f5d3s2a1',
                    'vendor': 'Снегурочка',
                    'bin_location': 'C5-G7',
                    'price': 1.5,
                    'note': 'Her bir list korobkalayyn gelman, packalayyn geldi',
                    'is_retrieved': False,
                    'category_id': 1
                }
            ]
        }
    }


class RequestSchema(BaseModel):
    item_id: int
    req_quantity: int
    req_date: date

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    'item_id': 12,
                    # 'department_id': 3, 
                    # 'position_id': 7, 
                    # 'user_id': 1,
                    'req_quantity': 45,
                    'req_date': '2023-10-12',
                }
            ]
        }
    }


class ResponseSchema(BaseModel):
    request_id: int
    status: int
    description: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    'request_id': 1,
                    'status': 1,
                    'description': 'Some description here!!!'
                }
            ]
        }
    }


class ResponseStatusSchema(BaseModel):
    status: int
