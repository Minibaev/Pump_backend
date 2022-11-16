from db.model_user import User, OST, PumpAggregate
from db.db import session
import api.schemas as schemas_api


def get_user_from_db(user_id):
    user = session.query(User).filter(User.id==user_id).first()
    res = schemas_api.UserSchema(id=user.id, name=user.name, surname=user.surname,
                                 nickname=user.nickname, email=user.email)
    return res


def get_osts_from_db():
    osts = session.query(OST).first()
    res = schemas_api.OSTSchemas(id=osts.id, neft_upr=osts.neft_upr, ost=osts.ost)
    return res


def add_user_in_db(name, surname, nickname, ost_id, email):
    user = User(name=name, surname=surname, nickname=nickname, ost_id=ost_id, email=email)
    session.add(user)
    session.commit()


def add_ost_in_db(neft_upr, ost):
    ost = OST(neft_upr=neft_upr, ost=ost)
    session.add(ost)
    session.commit()


def add_aggregate(ost_id, pump, electric_motor, kpd_pump, kpd_electric, station):
    aggregate = PumpAggregate(ost_id=ost_id, pump=pump, electric_motor=electric_motor, kpd_pump=kpd_pump,
                              kpd_electric=kpd_electric, station=station)
    session.add(aggregate)
    session.commit()
