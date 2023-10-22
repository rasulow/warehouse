from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from core import get_db, Response
import models as _mod
import services as crud
from operator import attrgetter



router = APIRouter(
    prefix='/request',
    tags=['Request']
)


@router.get('/', status_code=status.HTTP_200_OK)
async def get_request(
    st: bool = None,
    db: Session = Depends(get_db)):
    try:
        result = await crud.request.read(st, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_request(
    req: _mod.RequestSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.request.create(req, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.created(
        data=result
    )
    
    
@router.get('/{id}/', status_code=status.HTTP_200_OK)
async def read_request_by_id(
    id: int,
    db: Session = Depends(get_db)):
    try:
        result = await crud.request.read_by_id(id, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.read(
        data=result
    )
    
    
@router.put('/{id}/', status_code=status.HTTP_200_OK)
async def update_request(
    id: int,
    req: _mod.RequestSchema,
    db: Session = Depends(get_db)):
    try:
        result = await crud.request.update(id, req, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.updated(
        updated_id=result
    )
    
    
@router.delete('/{id}/', status_code=status.HTTP_200_OK)
async def delete_request(
    id: int, 
    db: Session = Depends(get_db)):
    try:
        result = await crud.request.delete(id, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.deleted(
        deleted_id=result
    )