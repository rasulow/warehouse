from pydantic import BaseModel
from typing import List


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
    
    
class UserSchema(BaseSchema):
    role: str
    staff_id: int
    department_id: int
    position_id: int
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    'name': 'Kakageldiyew Myratgeldi',
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
    title : str 
    quantity : int 
    price : float 
    material_number : str 
    vendor : str 
    bin_location : str 
    note : str 
    is_retrieved : bool = False 
    category_id : int
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    'title': 'Standart list A4',
                    'quantity': 100, 
                    'price': 90.50, 
                    'material_number': 'f5d3s2a1',
                    'vendor': 'Снегурочка',
                    'bin_location': 'C5-G7',
                    'note': 'Her bir list korobkalayyn gelman, packalayyn geldi', 
                    'is_retrieved': False, 
                    'category_id': 1
                }
            ]
        }
    }