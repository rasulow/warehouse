from sqlalchemy.orm import Session, joinedload, load_only
from sqlalchemy import desc
import models as _mod
from fastapi.encoders import jsonable_encoder


async def read(status, db: Session):
    result = db.query(_mod.Request)\
        .options(
            load_only(
                _mod.Request.req_quantity,
                _mod.Request.req_date,
                _mod.Request.status
            ),
            joinedload(
                _mod.Request.item
            )\
                .options(
                    load_only(
                        _mod.Item.title,
                        _mod.Item.quantity,
                        _mod.Item.price,
                        _mod.Item.material_number,
                        _mod.Item.vendor,
                        _mod.Item.bin_location,
                        _mod.Item.note,
                        _mod.Item.is_retrieved,
                    )
                )
        )\
        .options(
            joinedload(
                _mod.Request.department
            )\
                .options(
                    load_only(
                        _mod.Department.name
                    )
                )
        )\
        .options(
            joinedload(
                _mod.Request.position
            )\
                .options(
                    load_only(
                        _mod.Position.name
                    )
                )
        )\
        .options(
            joinedload(
                _mod.Request.user
            )\
                .options(
                    load_only(
                        _mod.User.name,
                        _mod.User.staff_id,
                        _mod.User.role
                    )
                )
        )
    
    if status is not None:
        result = result.filter(_mod.Request.status == status)
    result = result.order_by(desc(_mod.Request.id)).all()
    
    return jsonable_encoder(result)


async def create(req: _mod.RequestSchema, db: Session):
    new_add = _mod.Request(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return jsonable_encoder(new_add)