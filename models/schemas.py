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


