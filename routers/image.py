from fastapi import APIRouter, Depends, status, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from core import get_db, Response
import models as _mod
import services as crud
from typing import List


router = APIRouter(
    prefix='/image',
    tags=['Image']
)

@router.post('/{id}/')
async def create_image(
    id: int,
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db)):
    try:
        result = await crud.image.create(id, files, db)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.created(
        data=result
    )