from functools import wraps
from fastapi import HTTPException, Depends
from core import get_current_user
from typing import Annotated


def user_rbac(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if kwargs['user']['role'] == 'admin':
            raise HTTPException(status_code=401, detail='This api gives access only user privileges')
        return await func(*args, **kwargs)

    return wrapper


def admin_rbac(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if kwargs['user']['role'] == 'user':
            raise HTTPException(status_code=401, detail='This api gives access only admin privileges')
        return await func(*args, **kwargs)

    return wrapper


user_dependency = Annotated[dict, Depends(get_current_user)]
