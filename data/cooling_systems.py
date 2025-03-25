import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class CoolingSystems(SqlAlchemyBase):
    __tablename__ = 'cooling_systems'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    socket_id = sqlalchemy.Column(sqlalchemy.Integer,
                               sqlalchemy.ForeignKey("sockets.id"))
    tdp = sqlalchemy.Column(sqlalchemy.Integer)
    type = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.REAL)
    currency = sqlalchemy.Column(sqlalchemy.String)

    socket = orm.relationship("Sockets")
