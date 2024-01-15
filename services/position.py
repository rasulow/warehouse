from sqlalchemy.orm import Session, joinedload, load_only
from sqlalchemy import desc
import models as _mod
from fastapi.encoders import jsonable_encoder


async def read(db: Session):
    return jsonable_encoder(
        db.query(_mod.Position)\
        .options(
            load_only(_mod.Position.name),
            joinedload(_mod.Position.department)\
            .options(
                load_only(
                    _mod.Department.id, _mod.Department.name
                )
            )
        )\
        .order_by(desc(_mod.Position.id))\
        .all()
    )


async def read_by_id(id: int, db: Session):
    return jsonable_encoder(
        db.query(_mod.Position)\
        .options(
            load_only(_mod.Position.name),
            joinedload(_mod.Position.department)\
            .options(
                load_only(
                    _mod.Department.id, _mod.Department.name
                )
            )
        )\
        .filter(_mod.Position.id == id)\
        .first()
    )


async def create(req: _mod.PositionSchema, db: Session):
    new_add = _mod.Position(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return jsonable_encoder(new_add)


async def update(id: int, req: _mod.PositionSchema, db: Session):
    new_update = db.query(_mod.Position)\
    .filter(_mod.Position.id == id)\
    .update({
        _mod.Position.name: req.name,
        _mod.Position.department_id: req.department_id
    }, synchronize_session=False)
    db.commit()
    return jsonable_encoder(new_update)


async def delete(id: int, db: Session):
    new_delete = db.query(_mod.Position)\
    .filter(_mod.Position.id == id)\
    .delete(synchronize_session=False)
    db.commit()
    return  jsonable_encoder(new_delete)