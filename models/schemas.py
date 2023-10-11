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