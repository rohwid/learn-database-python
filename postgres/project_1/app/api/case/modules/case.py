from sqlalchemy import or_

from app.api.model import Entities

from app.api.serializer import EntitySchema

from app.api.http_response import HttpResponse

def extract_id(id):
    id_ = id.split('|')
    return id_[0], id_[1]

def degree_helper(degree_):
    return degree_ * 2


class EntityServices():

    def __init__(self) -> None:
        pass
    
    def show_all(self, key=None):
        filter = []
        if key is not None:
            filter = [or_(Entities.label.ilike('%' + key + '%') , Entities.id.ilike('%' + key + '%'))]
        entity = Entities.query.filter(*filter).limit(10)

        entity_list = EntitySchema(many=True).dump(entity)
        return HttpResponse(entity_list).ok()

