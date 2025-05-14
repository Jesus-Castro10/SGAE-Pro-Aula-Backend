from datetime import date, datetime
from django.db.models import Model, QuerySet
import math

def serialize(obj, visited=None):
    if visited is None:
        visited = set()

    if id(obj) in visited:
        return f"<recursion detected: {type(obj).__name__}>"

    visited.add(id(obj))

    if isinstance(obj, (str, bool)) or obj is None:
        return obj
    elif isinstance(obj, (int, float)):
        if isinstance(obj, float) and (math.isnan(obj) or math.isinf(obj)):
            return None
        return obj
    elif isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, (list, tuple, QuerySet)):
        return [serialize(item, visited) for item in obj]
    elif isinstance(obj, dict):
        return {str(key): serialize(value, visited) for key, value in obj.items()}
    elif isinstance(obj, Model):
        data = {}
        for field in obj._meta.get_fields():
            if field.is_relation and field.auto_created and not field.concrete:
                continue
            try:
                value = getattr(obj, field.name)
                data[field.name] = serialize(value, visited)
            except Exception:
                data[field.name] = f"<unserializable: {type(field).__name__}>"
        return data
    elif hasattr(obj, '__dict__'):
        return {
            str(key): serialize(value, visited)
            for key, value in obj.__dict__.items()
            if not key.startswith('_') and not callable(value)
        }
    else:
        return str(obj)
