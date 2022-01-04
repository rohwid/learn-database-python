"""This module does blah blah."""
import time
from datetime import datetime
from datetime import timedelta
from enum import unique

import bcrypt
import jwt

from flask_sqlalchemy import SQLAlchemy


# from app.api import db
db = SQLAlchemy()

from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship, deferred

from app.config import config

from app.api.error.token import (EmptyPayloadError, SignatureExpiredError, InvalidTokenError)

from authlib.integrations.sqla_oauth2 import (
    OAuth2ClientMixin,
    OAuth2AuthorizationCodeMixin,
    OAuth2TokenMixin,
)

now = datetime.utcnow()

JWT_CONFIG = config.Config.JWT_CONFIG

class Base(db.Model):
    """
        this is base class used by all class model
    """
    __abstract__ = True
    created_at = Column(db.DateTime, default=db.func.now())
    updated_at = Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

"""This is association table between Role and Permission table -> Many to Many"""
role_permission_group = db.Table('role_permission_group', Base.metadata,
    db.Column('created_at', db.DateTime, default=db.func.now()),
    db.Column('updated_at',db.DateTime, default=db.func.now(), onupdate=db.func.now()),
    db.Column('id', db.Integer, primary_key=True),
    db.Column('role_id', db.ForeignKey('role.id')),
    db.Column('permission_id', db.ForeignKey('permission.id')),
    db.Column('is_active', db.Boolean(), default=True)
)

class Role(Base):
    """
        this is class that represent Role Table
    """
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    user = relationship("User", back_populates="role")
    permission = relationship("Permission",
                    secondary=role_permission_group, back_populates="role")
    is_active = Column(db.Boolean(), default=True)


class Permission(Base):
    """
        this is class that represent Permission Table
    """
    __tablename__ = 'permission'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    is_active = Column(db.Boolean(), default=True)
    role = relationship(
        "Role",
        secondary=role_permission_group,
        back_populates="permission")

class User(Base):
    """
        this is class that represent User Table
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(64), unique=True)
    username = Column(String(64))
    password = deferred(Column(String(255)))
    name = Column(String(64))
    role_id = db.Column(db.ForeignKey('role.id'))
    role = relationship("Role", back_populates="user")
    is_active = Column(db.Boolean(), default=True)

    def __str__(self):
        return self.username

    def get_user_id(self):
        return self.id

    def check_password(self, password):
        return password == 'valid'

    def set_password(self, password):
        """
            Function to set hashed password
            args :
                password -- password
        """
        password = str(password + password[::-1])
        password_encode = password.encode('utf8')
        self.password = bcrypt.hashpw(password_encode, bcrypt.gensalt()).decode()

    def check_password(self, password):
        """
            Function to check hashed password
            args :
                password -- str
        """
        password = str(password + password[::-1])
        return bcrypt.checkpw(password.encode('utf8'), self.password.encode('utf8'))

    @staticmethod
    def encode_token(token_type, user_id, scope):
        """
            Function to create JWT Token
            args :
                token_type -- Access / Refresh
                user_id -- User identity
                scope -- User scope
        """
        if token_type == "ACCESS":
            exp = datetime.utcnow() + timedelta(seconds=int(JWT_CONFIG["EXPIRE"]["ACCESS_TOKEN"]))
        elif token_type == "REFRESH":
            exp = datetime.utcnow() + timedelta(seconds=int(JWT_CONFIG["EXPIRE"]["REFRESH_TOKEN"]))

        payload = {
            "exp" : exp,
            "iat" : datetime.utcnow(),
            "sub" : str(user_id),
            "type": token_type,
            "aud" : scope
        }
        return jwt.encode(
            payload,
            JWT_CONFIG["SECRET"],
            JWT_CONFIG["ALGORITHM"]
        )

    @staticmethod
    def decode_token(token):
        """
            Function to decode JWT Token
            args :
                token -- Jwt token
        """
        try:
            payload = jwt.decode(token, JWT_CONFIG["SECRET"],
                                 algorithms=JWT_CONFIG["ALGORITHM"])

            if not payload:
                raise EmptyPayloadError
        except jwt.ExpiredSignatureError as error:
            raise SignatureExpiredError(error)
        except jwt.InvalidTokenError as error:
            raise InvalidTokenError(error)
        return payload

class OAuth2Client(db.Model, OAuth2ClientMixin):
    __tablename__ = 'oauth2_client'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

class OAuth2AuthorizationCode(db.Model, OAuth2AuthorizationCodeMixin):
    __tablename__ = 'oauth2_code'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

class OAuth2Token(db.Model, OAuth2TokenMixin):
    __tablename__ = 'oauth2_token'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

    def is_refresh_token_active(self):
        if self.revoked:
            return False
        expires_at = self.issued_at + self.expires_in * 2
        return expires_at >= time.time()

class Gatra(Base):
    """
        this is class that represent gatra Table
    """
    __tablename__ = 'gatra'
    id = db.Column(db.String(),primary_key=True, unique=True)
    name = db.Column(db.String(), unique=True)
    is_active = Column(db.Boolean(), default=True)


"""This is association table between EVent and Entities table -> Many to Many"""
event_entities_group = db.Table('event_entities_group', Base.metadata,
    db.Column('created_at', db.DateTime, default=db.func.now()),
    db.Column('updated_at',db.DateTime, default=db.func.now(), onupdate=db.func.now()),
    db.Column('id', db.Integer, primary_key=True),
    db.Column('event_id', db.ForeignKey('event.id')),
    db.Column('entities_id', db.ForeignKey('entities.id')),
    db.Column('is_active', db.Boolean(), default=True)
)

class Entities(Base):
    """
        this is class that represent entities Table
    """
    __tablename__ = 'entities'
    id = db.Column(db.String(),primary_key=True, unique=True)
    vertex_id = db.Column(db.ForeignKey('vertex.id'))
    label = db.Column(db.String())
    is_active = Column(db.Boolean(), default=True)
    event = relationship("Event",
                secondary=event_entities_group, back_populates="entities")

class Event(Base):
    """
        this is class that represent event Table
    """
    __tablename__ = 'event'
    id = db.Column(db.String(), primary_key=True,   server_default=db.Sequence('event_id_seq').next_value() )
    label = db.Column(db.String())
    main = db.Column(db.String())
    location_id = db.Column(db.ForeignKey('location.id'))
    location = relationship("Location")
    gatra = relationship("GatraProba")
    ian = relationship("Ian", back_populates="event")
    entities = relationship("Entities",
            secondary=event_entities_group, back_populates="event")
    is_active = Column(db.Boolean(), default=True)

class Location(Base):
    """
        this is class that represent location
    """
    __tablename__ = 'location'
    id = db.Column(db.String(), primary_key=True)
    label = db.Column(db.String())
    latitude = db.Column(db.Float())
    longtitude = db.Column(db.Float())
    is_active = Column(db.Boolean(), default=True)

class Ian(Base):
    """
        this is class that represent ian Table
    """
    __tablename__ = 'ian'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    # gatra_id = db.Column(db.ForeignKey('gatra.id'))
    # entities_id = db.Column(db.ForeignKey('entities.id'))
    event_id = db.Column(db.ForeignKey('event.id'))
    event = relationship("Event",back_populates="ian")
    score = db.Column(db.Float())
    date = db.Column(db.DateTime())
    is_active = Column(db.Boolean(), default=True)

class GatraProba(Base):
    """
        this is class blabla
    """
    __tablename__ = 'event_gatra_proba'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    gatra_id = db.Column(db.ForeignKey('gatra.id'))
    event_id = db.Column(db.ForeignKey('event.id'))
    gatra = relationship('Gatra')
    proba = db.Column(db.Float())

class Vertex(Base):
    """
        this is class that represent vertex Table
    """
    __tablename__ = 'vertex'
    id = db.Column(db.String(),primary_key=True, unique=True)
    name = db.Column(db.String(), unique=True)
    is_default =  Column(db.Boolean(), default=False)
    is_active = Column(db.Boolean(), default=True)

class Edge(Base):
    """
        this is class that represent edge Table
    """
    __tablename__ = 'edge'
    id = db.Column(db.String(),primary_key=True, unique=True)
    name = db.Column(db.String(), unique=True)
    is_default =  Column(db.Boolean(), default=False)
    is_active = Column(db.Boolean(), default=True)

class Relation(Base):
    """
        this is class that represent relation Table
    """
    __tablename__ = 'relation'
    id = db.Column(db.String(), primary_key=True)
    from_entity_id = db.Column(db.ForeignKey('entities.id'))
    edge_id = db.Column(db.ForeignKey('edge.id'))
    to_entity_id = db.Column(db.ForeignKey('entities.id'))
