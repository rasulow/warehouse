from fastapi import APIRouter, Depends, status, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from core import get_db, Response, admin_rbac, user_dependency
import services as crud
from typing import List

router = APIRouter(
    prefix='/image',
    tags=['Image']
)


@router.post('/{id}/', summary='ADMIN')
@admin_rbac
async def create_image(
        id: int,
        user: user_dependency,
        files: List[UploadFile] = File(...),
        db: Session = Depends(get_db)):
    try:
        result = await crud.image.create(id, files, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=e
        )

    return Response.created(
        data=result
    )
