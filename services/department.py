from sqlalchemy.orm import Session
from sqlalchemy import desc
import models as _mod
from fastapi.encoders import jsonable_encoder


async def read(db: Session):
    return jsonable_encoder(
        db.query(_mod.Department) \
            .order_by(desc(_mod.Department.id)) \
            .all()
    )


async def read_by_id(id: int, db: Session):
    return jsonable_encoder(
        db.query(_mod.Department) \
            .filter(_mod.Department.id == id) \
            .first()
    )


async def create(req: _mod.BaseSchema, db: Session):
    new_add = _mod.Department(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return jsonable_encoder(new_add)


async def update(id: int, req: _mod.BaseSchema, db: Session):
    new_update = db.query(_mod.Department) \
        .filter(_mod.Department.id == id) \
        .update(
            {
                _mod.Department.name: req.name
            }, synchronize_session=False)
    db.commit()
    return jsonable_encoder(new_update)


async def delete(id: int, db: Session):
    new_delete = db.query(_mod.Department)\
        .filter(_mod.Department.id == id)\
        .delete(synchronize_session=False)
    db.commit()
    return jsonable_encoder(new_delete)