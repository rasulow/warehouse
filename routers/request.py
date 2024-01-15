from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core import get_db, Response, admin_rbac, user_rbac, user_dependency
import models as _mod
import services as crud

router = APIRouter(
    prefix='/request',
    tags=['Request']
)


@router.get('/', status_code=status.HTTP_200_OK, summary='ADMIN')
@admin_rbac
async def get_request(
        user: user_dependency,
        st: bool = None,
        db: Session = Depends(get_db)):
    try:
        result = await crud.request.read(st, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )


@router.get('/user/', status_code=status.HTTP_200_OK, summary='USER')
@user_rbac
async def get_request(
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.request.read_by_user_id(user['id'], db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )


@router.post('/', status_code=status.HTTP_201_CREATED, summary='USER')
@user_rbac
async def create_request(
        user: user_dependency,
        req: _mod.RequestSchema,
        db: Session = Depends(get_db)):
    try:
        result = await crud.request.create(req, user, db)
    except Exception as e:
        print(e)

    return Response.created(
        data=result
    )


@router.get('/{id}/', status_code=status.HTTP_200_OK, summary='ADMIN and USER')
async def read_request_by_id(
        id: int,
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.request.read_by_id(id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )


@router.put('/{id}/', status_code=status.HTTP_200_OK, summary='USER')
@user_rbac
async def update_request(
        id: int,
        user: user_dependency,
        req: _mod.RequestSchema,
        db: Session = Depends(get_db)):
    try:
        result = await crud.request.update(id, req, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.updated(
        updated_id=result
    )


@router.delete('/{id}/', status_code=status.HTTP_200_OK, summary='USER')
@user_rbac
async def delete_request(
        id: int,
        user: user_dependency,
        db: Session = Depends(get_db)):
    try:
        result = await crud.request.delete(id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.deleted(
        deleted_id=result
    )
