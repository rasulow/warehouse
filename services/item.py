from sqlalchemy.orm import Session, joinedload, load_only
from sqlalchemy import desc
import models as _mod
from fastapi.encoders import jsonable_encoder



async def read(is_retrieved: bool, db: Session):
    result = db.query(_mod.Item)\
        .options(
            joinedload(_mod.Item.category)\
            .options(
                load_only(
                    _mod.Category.id,
                    _mod.Category.name
                )
            )
        )
    if is_retrieved is not None:
        result = result.filter(_mod.Item.is_retrieved == is_retrieved)
    result = result.order_by(desc(_mod.Item.id)).all()
    
    return jsonable_encoder(
        result
    )
    
    
async def create(req: _mod.ItemSchema, db: Session):
    new_add = _mod.Item(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return jsonable_encoder(new_add)


async def update(id: int, req: _mod.ItemSchema, db: Session):
    new_update = db.query(_mod.Item)\
        .filter(_mod.Item.id == id)\
        .update({
            _mod.Item.title: req.title,
            _mod.Item.quantity: req.quantity, 
            _mod.Item.price: req.price, 
            _mod.Item.material_number: req.material_number,  
            _mod.Item.vendor: req.vendor,
            _mod.Item.bin_location: req.bin_location,
            _mod.Item.note: req.note,
            _mod.Item.is_retrieved: req.is_retrieved,
            _mod.Item.category_id: req.category_id
        }, synchronize_session=False)
    db.commit()
    return jsonable_encoder(new_update)


async def delete(id: int, db: Session):
    new_delete = db.query(_mod.Item)\
        .filter(_mod.Item.id == id)\
        .delete(synchronize_session=False)
    
    db.commit()
    
    return jsonable_encoder(new_delete)
        