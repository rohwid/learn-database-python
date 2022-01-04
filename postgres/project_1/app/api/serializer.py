"""
this is module for serializer
"""

import re
from typing import KeysView

from sqlalchemy.orm import load_only

from marshmallow import fields
from marshmallow import ValidationError
from marshmallow import validates
from marshmallow import post_load, post_dump

from app.api.model import User
from app.api.model import Role
from app.api.model import Permission

from app.api import ma

from app.config.entity import VERTEX, EDGE, VERTEX_INVERSE

from pyorient.ogm.what import ( at_class)

def cannot_be_blank(string):
    """
        function to make user not enter empty string
        args :
            string -- user inputted data
    """
    if not string:
        raise ValidationError("Data cannot be blank")
#end def
def split_to_dict(list_):
    dict_ = {}
    for i in list_:
        i = i.split(" ")
        if len(i) > 1:
            # dict_.append({"key": i[0], "value" : i[1]})
            dict_[i[0]] = i[1]
        else:
            # dict_.append({"key": i[0], "value" : i[0]})
            dict_[i[0]] = i[0]
    return dict_

def extract_entities(entities, request_data,**kwargs):
    if entities is not None:
        entities = split_to_dict(entities)
        
        for key, value in entities.items():    
            request_data[value] = []
            
        for i in request_data['entities']:
            if i['class'] in [ key for key, value in entities.items() ]:
                v = {}
                v['id'] = i['id']
                v['label'] = i['label']

                try:
                    request_data[ entities[ i['class'] ] ].append(v)
                except(KeyError):
                    request_data[ entities[ i['class'] ] ] = []
                    request_data[ entities[ i['class'] ] ].append(v)

        del request_data['entities']
    return request_data

class UserSchema(ma.Schema):
    """ this is class schema for User"""
    id = fields.Int()
    name = fields.Str(required=True, validate=cannot_be_blank)
    email = fields.Email(required=True, validate=cannot_be_blank)
    username = fields.Str()
    role_id = fields.Int()
    password = fields.Str(required=True, load_only=True)
    is_active = fields.Bool(load_only=True)

    @validates('email')
    def validate_email(self, email):
        """
            function to validate email
            args:
                email -- email
        """
        if re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) != None:
            pass
        else:
            raise ValidationError('Invalid email')
    #end def

    @post_load
    def make_object(self, request_data,**kwargs):
        """ create user object """
        return User(**request_data)

class PermissionSchema(ma.Schema):
    """ this is class schema for Role"""
    id = fields.Int()
    name = fields.Str(required=True, validate=cannot_be_blank)
    is_active = fields.Bool(load_only=True)

    @post_load
    def make_object(self, request_data,**kwargs):
        """ create permission object """
        return Permission(**request_data)

class RoleSchema(ma.Schema):
    """ this is class schema for Role"""
    id = fields.Int()
    name = fields.Str(required=True, validate=cannot_be_blank)
    permission = fields.Nested(PermissionSchema, many=True)
    is_active = fields.Bool(load_only=True)

    @post_load
    def make_object(self, request_data,**kwargs):
        """ create role object """
        return Role(**request_data)
    

class PersonSchema(ma.Schema):
    """ this is class schema for Role"""
    id = fields.Str(required=True, validate=cannot_be_blank)
    label = fields.Str(required=True, validate=cannot_be_blank)

    @post_load
    def make_object(self, request_data,**kwargs):
        """ create person object """
        return Person(**request_data)

class OrganizationSchema(ma.Schema):
    """ this is class schema for Role"""
    id = fields.Str(required=True, validate=cannot_be_blank)
    label = fields.Str(required=True, validate=cannot_be_blank)

    @post_load
    def make_object(self, request_data,**kwargs):
        """ create organization object """
        return Organization(**request_data)

class EntitySchema(ma.Schema):
    """ this is class schema for Entity"""
    def __init__(self, *args, **kwargs):
        self._extract_entity = kwargs.pop('extract_entities', None)
        self._class_transformer = kwargs.pop('class_transform', True)
        super().__init__(*args, **kwargs)
        
    id = fields.Str(required=True, validate=cannot_be_blank)
    label = fields.Str(required=True, validate=cannot_be_blank)
    vertex_id = fields.Str(required=True, validate=cannot_be_blank, data_key="class")

    @post_dump
    def class_transformer(self, request_data,**kwargs):
        if self._class_transformer is True and request_data.get('class', None) is not None and VERTEX_INVERSE.get(request_data.get('class', None), None) is not None:
            request_data['class'] = VERTEX_INVERSE[ request_data['class'] ]
        return request_data

    @post_dump(pass_many=True)
    def group_by_class(self, request_data,**kwargs):
        if self._extract_entity is not None:
            data = {
                "entities" : request_data
            }
            return extract_entities(self._extract_entity, data,**kwargs)
        return request_data

class RelationSchema(ma.Schema):
    from_ = fields.Str(required=True, validate=cannot_be_blank, data_key="from")
    id = fields.Str(required=True, validate=cannot_be_blank)
    label = fields.Str(required=True, validate=cannot_be_blank)
    to = fields.Str(required=True, validate=cannot_be_blank)

class RelexSchema(ma.Schema):
    relations = fields.Nested(RelationSchema, many=True)
    entities = fields.Nested(EntitySchema, many=True)

class CoordinateSchema(ma.Schema):
    latitude = fields.Float(required=True, validate=cannot_be_blank)
    longtitude = fields.Float(required=True, validate=cannot_be_blank)

class LocationSchema(ma.Schema):
    id = fields.Str(required=True, validate=cannot_be_blank)
    label = fields.Str(required=True, validate=cannot_be_blank)
    latitude = fields.Float(required=True, validate=cannot_be_blank)
    longtitude = fields.Float(required=True, validate=cannot_be_blank)

    @post_dump
    def coordinate(self, request_data,**kwargs):

        request_data["coordinate"] = {}

        if request_data.get('latitude', None) is not None:
            request_data["coordinate"]['latitude'] = request_data["latitude"]
            del request_data['latitude']

        if request_data.get('longtitude', None) is not None:
            request_data["coordinate"]['longtitude'] = request_data["longtitude"]
            del request_data['longtitude']

        return request_data

class IanSchema(ma.Schema):
    score = fields.Float(required=True, validate=cannot_be_blank)
    date = fields.Date(format='%Y-%m-%d')

class IanGatraSchema(ma.Schema):
    id = fields.Str(required=True, validate=cannot_be_blank)
    label = fields.Str(required=True, validate=cannot_be_blank)
    score = fields.Float(required=True, validate=cannot_be_blank)

class GatraProbaSchema(ma.Schema):
    # id = fields.Str(required=True, validate=cannot_be_blank)
    gatra_id = fields.Str(required=True, validate=cannot_be_blank, data_key='id')
    proba = fields.Float(required=True, validate=cannot_be_blank)

class EventDumpSchema(ma.Schema):
    """ this is class event for Entity"""
    def __init__(self, *args, **kwargs):
        self._extract_entity = kwargs.pop('extract_entities', None)
        super().__init__(*args, **kwargs)
        
    id = fields.Str()
    label = fields.Str()
    gatra = fields.Nested(GatraProbaSchema, many=True)
    entities = fields.Nested(EntitySchema(class_transform=False), many=True)
    # organisasi = fields.Nested(EntitySchema, many=True)
    ian = fields.Nested(IanSchema, allow_none= True, missing=True, many=True)
    location = fields.Nested(LocationSchema)
    
    @post_dump
    def extract_entity(self, request_data,**kwargs):
        return extract_entities(self._extract_entity, request_data,**kwargs)

class GraphSchema(ma.Schema):
    entities = fields.Nested(EntitySchema, many=True)
    relations = fields.Nested(RelationSchema, many=True)

class EventLoadSchema(ma.Schema):
    """ this is class event for Entity"""
        
    # id = fields.Str(allow_none= True, missing=True, many=True)
    label = fields.Str()
    gatra = fields.Nested(GatraProbaSchema, many=True)
    graph = fields.Nested(GraphSchema)
    main = fields.Dict()
    ian = fields.Float()
    location = fields.Nested(LocationSchema)

class RangeDateSchema(ma.Schema):
    start = fields.Date(format='%Y-%m-%d')
    end = fields.Date(format='%Y-%m-%d')

class GatraSchema(ma.Schema):
    gatra_id = fields.Int(required=True)

class SearchEventSchema(ma.Schema):
    gatra = fields.List(fields.String(), allow_none= True, missing=True)
    tokoh = fields.List(fields.String(), allow_none= True, missing=True)
    organisasi = fields.List(fields.String(), allow_none= True, missing=True)
    event = fields.List(fields.String(), allow_none= True, missing=True)
    date = fields.Nested(RangeDateSchema, allow_none= True, missing=True)

class Oauth2ClientSchema(ma.Schema):
    user_id = fields.Int(required=True)
    client_id = fields.Str(dump_only=True)
    client_secret = fields.Str(dump_only=True)
    client_name = fields.Str(required=True)
    client_uri = fields.Str(required=True)
    grant_type = fields.List(fields.String(), required=True)
    redirect_uri = fields.List(fields.String(), required=True)
    response_type = fields.List(fields.String(), required=True)
    scope = fields.Str(required=True)
    token_endpoint_auth_method = fields.Str(required=True)