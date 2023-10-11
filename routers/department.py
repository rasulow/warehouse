from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core import get_db, Response
import models as _mod
import services as crud

router = APIRouter(
    prefix='/department',
    tags=['Department']
)


@router.get('/', status_code=status.HTTP_200_OK)
async def get_department(
        db: Session = Depends(get_db)):
    try:
        result = await crud.department.read(db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )


@router.get('/{id}/', status_code=status.HTTP_200_OK)
async def get_current_department(
        id: int,
        db: Session = Depends(get_db)):
    try:
        result = await crud.department.read_by_id(id, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_department(
        req: _mod.BaseSchema,
        db: Session = Depends(get_db)):
    try:
        result = await crud.department.create(req=req, db=db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e
        )

    return Response.created(
        data=result
    )


@router.put('/{id}/', status_code=status.HTTP_200_OK)
async def update_department(
        id: int,
        req: _mod.BaseSchema,
        db: Session = Depends(get_db)):
    try:
        result = await crud.department.update(id, req, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e
        )

    return Response.updated(
        updated_id=result
    )


@router.delete('/{id}/', status_code=status.HTTP_200_OK)
async def delete_department(
        id: int,
        db: Session = Depends(get_db)):
    try:
        result = await crud.department.delete(id, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e
        )

    return Response.deleted(
        deleted_id=result
    )