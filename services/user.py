from sqlalchemy.orm import Session, joinedload, load_only
from sqlalchemy import desc
import models as _mod
from fastapi.encoders import jsonable_encoder


async def read(is_deleted, db: Session):
    result = db.query(_mod.User) \
        .options(
        load_only(
            _mod.User.id,
            _mod.User.username,
            _mod.User.staff_id,
            _mod.User.role,
            _mod.User.is_deleted
        ),
        joinedload(_mod.User.department)
        .options(
            load_only(
                _mod.Department.id,
                _mod.Department.name
            )
        )
    ) \
        .options(
        joinedload(_mod.User.position)
        .options(
            load_only(
                _mod.Position.id,
                _mod.Position.name
            )
        )
    )

    if is_deleted is not None:
        result = result.filter(_mod.User.is_deleted == is_deleted)

    return jsonable_encoder(
        result.order_by(desc(_mod.User.id))
        .all()
    )


async def create(req: _mod.UserSchema, db: Session):
    new_add = _mod.User(
        username=req.username,
        hashed_password=req.password,
        role=req.role,
        staff_id=req.staff_id,
        department_id=req.department_id,
        position_id=req.position_id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return jsonable_encoder(new_add)


async def read_by_id(id: int, db: Session):
    return jsonable_encoder(
        db.query(_mod.User)
        .options(
            load_only(
                _mod.User.id,
                _mod.User.username,
                _mod.User.staff_id,
                _mod.User.role
            ),
            joinedload(_mod.User.department)
            .options(
                load_only(
                    _mod.Department.id,
                    _mod.Department.name
                )
            ),
            joinedload(_mod.User.position)
            .options(
                load_only(
                    _mod.Position.id,
                    _mod.Position.name
                )
            )
        )
        .filter(_mod.User.id == id)
        .first()
    )


async def update(id: int, req: _mod.UserSchema, db: Session):
    new_update = db.query(_mod.User) \
        .filter(_mod.User.id == id) \
        .update({
        _mod.User.name: req.name,
        _mod.User.staff_id: req.staff_id,
        _mod.User.role: req.role,
        _mod.User.department_id: req.department_id,
        _mod.User.position_id: req.position_id,
    }, synchronize_session=False)
    db.commit()
    return jsonable_encoder(new_update)


async def update_is_deleted(id: int, req: _mod.UserIsDeletedSchema, db: Session):
    new_update = db.query(_mod.User) \
        .filter(_mod.User.id == id) \
        .update({
        _mod.User.is_deleted: req.is_deleted
    }, synchronize_session=False)
    db.commit()
    return jsonable_encoder(new_update)


async def delete(id: int, db: Session):
    new_delete = db.query(_mod.User) \
        .filter(_mod.User.id == id) \
        .delete(synchronize_session=False)
    db.commit()
    return jsonable_encoder(new_delete)
