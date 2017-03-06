class InsensitiveDict(dict):
    def __init__(self, obj):
        obj_dict = obj.__dict__
        for key in dir(obj):
            if not key.startswith('_'):
                self[key.lower()] = getattr(obj, key)
