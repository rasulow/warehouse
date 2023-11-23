from fastapi import APIRouter, Depends, status, HTTPException, Request
from sqlalchemy.orm import Session
from core import get_db, Response, user_dependency, admin_rbac
import models as _mod
import services as crud

router = APIRouter(
    prefix='/category',
    tags=['Category']
)


@router.get('/', status_code=status.HTTP_200_OK, summary='ADMIN and USER')
async def get_category(
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.category.read(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )


@router.get('/item/', status_code=status.HTTP_200_OK, summary='ADMIN and USER')
async def get_category_by_item(
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.category.read_by_item(db)
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
async def create_category(
        req: _mod.BaseSchema,
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.category.create(req, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.created(
        data=result
    )


@router.put('/', status_code=status.HTTP_200_OK, summary='ADMIN')
@admin_rbac
async def update_category(
        id: int,
        user: user_dependency,
        req: _mod.BaseSchema,
        db: Session = Depends(get_db)):
    try:
        result = await crud.category.update(id, req, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.updated(
        updated_id=result
    )


@router.delete('/', status_code=status.HTTP_200_OK, summary='ADMIN')
@admin_rbac
async def delete_category(
        id: int,
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.category.delete(id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.deleted(
        deleted_id=result
    )
