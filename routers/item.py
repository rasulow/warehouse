from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core import get_db, Response
import models as _mod
import services as crud

router = APIRouter(
    prefix='/item',
    tags=['Item']
)

@router.get('/', status_code=status.HTTP_200_OK)
async def get_item(
    is_retrieved: bool = None,
    db: Session = Depends(get_db)):
    try:
        result = await crud.item.read(is_retrieved, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )
    
    
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_item(
    req: _mod.ItemSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.item.create(req, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.created(
        data=result
    )
    
    
@router.put('/{id}/', status_code=status.HTTP_200_OK)
async def update_item(
    id: int, 
    req: _mod.ItemSchema, 
    db: Session = Depends(get_db)):
    try:
        result = await crud.item.update(id, req, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.updated(
        updated_id=result
    )
    
    
@router.delete('/{id}/', status_code=status.HTTP_200_OK)
async def delete_item(
    id: int,
    db: Session = Depends(get_db)):
    try:
        result = await crud.item.delete(id, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.deleted(
        deleted_id=result
    )