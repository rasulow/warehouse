from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core import get_db, Response, admin_rbac, user_dependency
import models as _mod
import services as crud

router = APIRouter(
    prefix='/item',
    tags=['Item']
)


@router.get('/', status_code=status.HTTP_200_OK, summary='ADMIN and USER')
async def get_item(
        user: user_dependency,
        q: str = None,
        category_id: int = None,
        is_retrieved: bool = None,
        db: Session = Depends(get_db)):
    try:
        result = await crud.item.read(q, category_id, is_retrieved, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )


@router.post('/', status_code=status.HTTP_201_CREATED, summary='ADMIN')
@admin_rbac
async def create_item(
        req: _mod.ItemSchema,
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.item.create(req, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.created(
        data=result
    )


@router.get('/{id}/', status_code=status.HTTP_200_OK, summary='ADMIN and USER')
async def get_item_by_id(
        id: str,
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.item.read_by_id(id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )


@router.put('/{id}/', status_code=status.HTTP_200_OK, summary='ADMIN')
@admin_rbac
async def update_item(
        id: int,
        user: user_dependency,
        req: _mod.ItemSchema,
        db: Session = Depends(get_db)):
    try:
        result = await crud.item.update(id, req, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.updated(
        updated_id=result
    )


@router.delete('/{id}/', status_code=status.HTTP_200_OK, summary='ADMIN')
@admin_rbac
async def delete_item(
        id: int,
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.item.delete(id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.deleted(
        deleted_id=result
    )
