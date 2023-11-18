from sqlalchemy.orm import Session, joinedload, load_only
from sqlalchemy import desc, asc
import models as _mod
from fastapi.encoders import jsonable_encoder


async def read(status, db: Session):
    result = db.query(_mod.Request) \
        .options(
        load_only(
            _mod.Request.req_quantity,
            _mod.Request.req_date,
            _mod.Request.status
        ),
        joinedload(
            _mod.Request.item
        ) \
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
            ),
            joinedload(_mod.Item.image)
        )
    ) \
        .options(
        joinedload(
            _mod.Request.response
        ) \
            .options(
            load_only(
                _mod.Response.status,
                _mod.Response.description,
            )
        )
    )\
    .options(
        joinedload(
            _mod.Request.user
        ) \
        .options(
            load_only(
                _mod.User.username
            )
        )
    )

    if status is not None:
        result = result.filter(_mod.Request.status == status)
    result = result.order_by(desc(_mod.Request.id)).all()

    return jsonable_encoder(result)


async def read_by_user_id(user_id, db: Session):
    result = db.query(_mod.Request) \
        .options(
        load_only(
            _mod.Request.req_quantity,
            _mod.Request.req_date,
            _mod.Request.status
        ),
        joinedload(
            _mod.Request.item
        ) \
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
            ),
            joinedload(_mod.Item.image)
        )
    ) \
        .options(
        joinedload(
            _mod.Request.response
        ) \
            .options(
            load_only(
                _mod.Response.status,
                _mod.Response.description,
            )
        )
    )

    result = result.filter(_mod.Request.user_id == user_id)
    result = result.order_by(desc(_mod.Request.id)).all()

    return jsonable_encoder(result)


async def create(req: _mod.RequestSchema, user, db: Session):
    new_add = _mod.Request(
        item_id=req.item_id,
        req_quantity=req.req_quantity,
        req_date=req.req_date,
        user_id=user['id'],
        department_id=user['department_id'],
        position_id=user['position_id']
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return jsonable_encoder(new_add)


async def read_by_id(id: int, db: Session):
    result = db.query(_mod.Request) \
        .options(
        load_only(
            _mod.Request.req_quantity,
            _mod.Request.req_date,
            _mod.Request.status
        ),
        joinedload(
            _mod.Request.item
        ) \
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
    ) \
        .options(
        joinedload(
            _mod.Request.department
        ) \
            .options(
            load_only(
                _mod.Department.name
            )
        )
    ) \
        .options(
        joinedload(
            _mod.Request.position
        ) \
            .options(
            load_only(
                _mod.Position.name
            )
        )
    ) \
        .options(
        joinedload(
            _mod.Request.user
        ) \
            .options(
            load_only(
                _mod.User.username,
                _mod.User.staff_id,
                _mod.User.role
            )
        )
    ) \
        .filter(_mod.Request.id == id) \
        .first()

    return jsonable_encoder(result)


async def update(id: int, req: _mod.RequestSchema, db: Session):
    new_update = db.query(_mod.Request) \
        .filter(_mod.Request.id == id) \
        .update({
        _mod.Request.item_id: req.item_id,
        _mod.Request.req_date: req.req_date,
        _mod.Request.req_quantity: req.req_quantity
    }, synchronize_session=False)
    db.commit()
    return jsonable_encoder(new_update)


async def delete(id: int, db: Session):
    new_delete = db.query(_mod.Request) \
        .filter(_mod.Request.id == id) \
        .delete(synchronize_session=False)
    db.commit()
    return jsonable_encoder(new_delete)
