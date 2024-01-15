from sqlalchemy.orm import Session, joinedload, load_only
from sqlalchemy import desc
import models as _mod
from fastapi.encoders import jsonable_encoder


async def read(status: int, db: Session):
    result = db.query(_mod.Response)\
        .options(
            load_only(
                _mod.Response.status,
                _mod.Response.description
            ),
            joinedload(
                _mod.Response.request
            )\
                .options(
                    load_only(
                        _mod.Request.req_date,
                        _mod.Request.req_quantity
                    ),
                    joinedload(
                        _mod.Request.user
                    )\
                        .options(
                            load_only(
                                _mod.User.username,
                                _mod.User.staff_id
                            )
                        )
                )
        )
    
    if status:
        result = result.filter(_mod.Response.status == status)
    
    result = result.order_by(desc(_mod.Response.id)).all()
    
    return jsonable_encoder(result)


async def create(req: _mod.ResponseSchema, db: Session):
    db.query(_mod.Request).filter(_mod.Request.id == req.request_id)\
    .update({
        _mod.Request.status: True
    }, synchronize_session=False)
    new_add = _mod.Response(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return jsonable_encoder(new_add)


async def read_by_id(id: int, db: Session):
    result = db.query(_mod.Response)\
        .options(
            load_only(
                _mod.Response.status,
                _mod.Response.description
            ),
            joinedload(
                _mod.Response.request
            )\
                .options(
                    load_only(
                        _mod.Request.req_date,
                        _mod.Request.req_quantity
                    ),
                    joinedload(
                        _mod.Request.user
                    )\
                        .options(
                            load_only(
                                _mod.User.username,
                                _mod.User.staff_id
                            )
                        )
                )
        )\
        .filter(_mod.Response.id == id)\
        .first()
    
    return jsonable_encoder(result)


async def update(id: int, req: _mod.ResponseSchema, db: Session):
    new_update = db.query(_mod.Response)\
        .filter(_mod.Response.id == id)\
        .update({
            _mod.Response.request_id: req.request_id,
            _mod.Response.status: req.status,
            _mod.Response.description: req.description
        }, synchronize_session=False)
    db.commit()
     
    return jsonable_encoder(new_update)


async def update_status(id: int, req: _mod.ResponseStatusSchema, db: Session):
    if req.status == 2:
        response = db.query(_mod.Response)\
            .options(
                joinedload(_mod.Response.request)  
            )\
            .filter(_mod.Response.id == id)\
            .first()
        item_id = response.request.item_id
        quantity = response.request.req_quantity
        
        db.query(_mod.Item)\
            .filter(_mod.Item.id == item_id)\
            .update({
                _mod.Item.quantity: _mod.Item.quantity - quantity
            }, synchronize_session=False)
        db.commit()   
    

        
    new_update = db.query(_mod.Response)\
        .filter(_mod.Response.id == id)\
        .update({
            _mod.Response.status: req.status,
        }, synchronize_session=False)
    db.commit()
    
    return jsonable_encoder(new_update)


async def delete(id: int, db: Session):
    new_delete = db.query(_mod.Response)\
        .filter(_mod.Response.id == id)\
        .delete(synchronize_session=False)
    db.commit()
    
    return jsonable_encoder(new_delete)