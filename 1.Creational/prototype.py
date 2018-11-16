#prototype.py
import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register object"""
        self._object[name] = obj

    def unregister_object(self, name, obj):
        """Unregister object"""
        del self._object[name]

    def clone(salf, name, **attr):
        
