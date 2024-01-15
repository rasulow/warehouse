from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core import get_db, Response, admin_rbac, user_rbac, user_dependency
import models as _mod
import services as crud


router = APIRouter(
    prefix='/response',
    tags=['Response']
)


@router.get('/', status_code=status.HTTP_200_OK, summary='ADMIN and USER')
async def read_response(
    user: user_dependency,
    st: int = None,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.read(st, db)
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
async def create_response(
    user: user_dependency,
    req: _mod.ResponseSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.create(req, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.created(
        data=result
    )
    
    
@router.get('/{id}/', status_code=status.HTTP_200_OK, summary='ADMIN and USER')
async def get_response_by_id(
    id: int,
    user: user_dependency,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.read_by_id(id, db)
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
async def update_response(
    id: int,
    user: user_dependency,
    req: _mod.ResponseSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.update(id, req, db)
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
async def update_response_status(
    id: int,
    user: user_dependency,
    req: _mod.ResponseStatusSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.update_status(id, req, db)
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
async def delete_response(
    id: int,
    user: user_dependency,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.delete(id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.deleted(
        deleted_id=result
    )