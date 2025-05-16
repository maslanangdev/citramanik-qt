import importlib
import os
import inspect


class CitramanikPluginInterface:
    @classmethod
    def initialize(cls):
        pass
    
    @classmethod
    def execute(cls, *args, **kwargs):
        raise NotImplementedError