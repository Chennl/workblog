
from sqlalchemy.ext.declarative import DeclarativeMeta
import json
from datetime import datetime

def new_alchemy_encoder(revisit_self = False, fields_to_expand = []):
    _visited_objs = []
    class AlchemyEncoder(json.JSONEncoder):

        def default(self, obj):
            
            if isinstance(obj.__class__, DeclarativeMeta):
                if revisit_self:
                    if obj in _visited_objs:
                        return None
                    _visited_objs.append(obj)
                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and hasattr(obj.__getattribute__(x),'__call__') ==False and x != 'metadata']:
                    data = obj.__getattribute__(field)
                    if field not in fields_to_expand:
                        fields[field] = None
                        continue
                    try:
                        if isinstance(data.__class__, DeclarativeMeta) or (isinstance(data, list) and len(data) > 0 and isinstance(data[0].__class__, DeclarativeMeta)):
                            fields[field] = data
                        elif isinstance(data,datetime):
                            data=data.strftime('%Y-%m-%d %H:%M:%S')
                            fields[field] = data
                        else: 
                            fields[field] = data
                    except TypeError:
                        fields[field] = None
                # a json-encodable dict
                return fields
            return json.JSONEncoder.default(self, obj)
    return  AlchemyEncoder