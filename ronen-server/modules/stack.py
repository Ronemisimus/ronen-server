from .global_strings import *
import json
#global objects
stack = []

def stack_size_endpoint():
    return to_json(res=str(len(stack)),error='')

