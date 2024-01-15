from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core import get_db, Response, admin_rbac, user_dependency
import models as _mod
import services as crud

router = APIRouter(
    prefix='/position',
    tags=['Position']
)


@router.get('/', status_code=status.HTTP_200_OK, summary='ADMIN')
@admin_rbac
async def get_position(
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.position.read(db)
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
async def create_position(
        user: user_dependency,
        req: _mod.PositionSchema,
        db: Session = Depends(get_db)):
    try:
        result = await crud.position.create(req, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.created(
        data=result
    )


@router.get('/{id}/', status_code=status.HTTP_200_OK, summary='ADMIN')
@admin_rbac
async def get_current_position(
        id: int,
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.position.read_by_id(id, db)
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
async def update_position(
        id: int,
        user: user_dependency,
        req: _mod.PositionSchema,
        db: Session = Depends(get_db)):
    try:
        result = await crud.position.update(id, req, db)
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
async def delete_position(
        id: int,
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.position.delete(id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.deleted(
        deleted_id=result
    )
