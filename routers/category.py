from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core import get_db, Response
import models as _mod
import services as crud


router = APIRouter(
    prefix='/category',
    tags=['Category']
)


@router.get('/', status_code=status.HTTP_200_OK)
async def get_category(
    db: Session = Depends(get_db)):
    try:
        result = await crud.category.read(db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )
    
    
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_category(
    req: _mod.BaseSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.category.create(req, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.created(
        data=result
    )
    
    
@router.put('/', status_code=status.HTTP_200_OK)
async def update_category(
    id: int,
    req: _mod.BaseSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.category.update(id, req, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.updated(
        updated_id=result
    )
    
    
@router.delete('/', status_code=status.HTTP_200_OK)
async def delete_category(
    id: int,
    db: Session = Depends(get_db)):
    try:
        result = await crud.category.delete(id, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.deleted(
        deleted_id=result
    )