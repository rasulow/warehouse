from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc
import models as _mod
from fastapi.encoders import jsonable_encoder


async def read(db: Session):
    return jsonable_encoder(
        db.query(_mod.Category)
        .order_by(desc(_mod.Category.id))
        .all()
    )


async def read_by_item(db: Session):
    return jsonable_encoder(
        db.query(_mod.Category)\
            .options(
                joinedload(_mod.Category.item)\
                    .options(
                        joinedload(_mod.Item.image)
                    )
            )
        .order_by(desc(_mod.Category.id))
        .all()
    )
    
    
async def create(req: _mod.BaseSchema, db: Session):
    new_add = _mod.Category(**req.dict())
    db.add(new_add) 
    db.commit()
    db.refresh(new_add)
    return jsonable_encoder(new_add)


async def update(id: int, req: _mod.BaseSchema, db: Session):
    new_update = db.query(_mod.Category) \
    .filter(_mod.Category.id == id) \
    .update(
        {
            _mod.Category.name: req.name
        }, synchronize_session=False)
    db.commit()
    return jsonable_encoder(new_update)


async def delete(id: int, db: Session):
    new_delete = db.query(_mod.Category) \
    .filter(_mod.Category.id == id) \
    .delete(synchronize_session=False)
    db.commit()
    
    return jsonable_encoder(new_delete)