from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core import get_db, Response
import models as _mod
import services as crud

router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.get('/', status_code=status.HTTP_200_OK)
async def get_user(
    is_deleted: bool = None,
    db: Session = Depends(get_db)):
    try:
        result = await crud.user.read(is_deleted, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )
    
    
@router.post('/', status_code=status.HTTP_201_CREATED)
async def get_user(
    req: _mod.UserSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.user.create(req, db)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.created(
        data=result
    )
    
    

@router.get('/{id}/', status_code=status.HTTP_200_OK)
async def get_current_user(
    id: int, 
    db: Session = Depends(get_db)):
    try:
        result = await crud.user.read_by_id(id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )
    
    
@router.put('/{id}/', status_code=status.HTTP_200_OK)
async def update_user(
    id: int,
    req: _mod.UserSchema, 
    db: Session = Depends(get_db)):
    try:
        result = await crud.user.update(id, req, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.updated(
        updated_id=result
    )
    
    
@router.patch('/{id}/', status_code=status.HTTP_200_OK)
async def update_user_is_deleted(
    id: int,
    req: _mod.UserIsDeletedSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.user.update_is_deleted(id, req, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.updated(
        updated_id=result
    )
    
    
@router.delete('/{id}/', status_code=status.HTTP_200_OK)
async def delete_user(
    id: int,
    db: Session = Depends(get_db)):
    try:
        result = await crud.user.delete(id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.deleted(
        deleted_id=result
    )