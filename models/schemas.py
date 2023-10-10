from pydantic import BaseModel
from typing import List


class BaseSchema(BaseModel):
    name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": 'Human resources'
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