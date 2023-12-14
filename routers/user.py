from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core import get_db, Response, user_dependency, admin_rbac
import models as _mod
import services as crud

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.get('/', status_code=status.HTTP_200_OK, summary='ADMIN')
@admin_rbac
async def get_user(
        user: user_dependency,
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


@router.get('-details/', status_code=status.HTTP_200_OK, summary='ADMIN and USER')
async def get_current_user(
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.user.read_by_id(user['id'], db)
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
async def update_user(
        id: int,
        user: user_dependency,
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


@router.patch('/{id}/', status_code=status.HTTP_200_OK, summary='ADMIN')
@admin_rbac
async def update_user_is_deleted(
        id: int,
        user: user_dependency,
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


@router.delete('/{id}/', status_code=status.HTTP_200_OK, summary='ADMIN')
@admin_rbac
async def delete_user(
        id: int,
        user: user_dependency,
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
