from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from core import get_db, Response
import models as _mod
import services as crud


router = APIRouter(
    prefix='/response',
    tags=['Response']
)


@router.get('/', status_code=status.HTTP_200_OK)
async def read_response(
    st: int = None,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.read(st, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_response(
    req: _mod.ResponseSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.create(req, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.created(
        data=result
    )
    
    
@router.get('/{id}/', status_code=status.HTTP_200_OK)
async def get_response_by_id(
    id: int,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.read_by_id(id, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )


@router.put('/{id}/', status_code=status.HTTP_200_OK)
async def update_response(
    id: int,
    req: _mod.ResponseSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.update(id, req, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.updated(
        updated_id=result
    )


@router.patch('/{id}/', status_code=status.HTTP_200_OK)
async def update_response_status(
    id: int,
    req: _mod.ResponseStatusSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.update_status(id, req, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.updated(
        updated_id=result
    )

@router.delete('/{id}/', status_code=status.HTTP_200_OK)
async def delete_response(
    id: int,
    db: Session = Depends(get_db)):
    try:
        result = await crud.response.delete(id, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.deleted(
        deleted_id=result
    )