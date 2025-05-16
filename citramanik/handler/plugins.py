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
    
    def call_inkscape():
        raise NotImplementedError

    def call_parser():
        raise NotImplementedError

    def call_cmd():
        raise NotImplementedError
    
    def get_input_data():
        raise NotImplementedError