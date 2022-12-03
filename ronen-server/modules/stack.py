from .global_strings import *
from flask import request
import json
#global objects
stack = []

def stack_size_endpoint():
    return to_json(res=str(len(stack)),error='')


def get_arg_list(result:int, error:str, response_code:int, params:dict):
    arguments = []
    if response_code==200:
        valid_keys = arguments_str in params
        valid_list = valid_keys and isinstance(params[arguments_str],list)
        valid_type = valid_list and all(isinstance(item,int) for item in params[arguments_str])

        response_code = response_code if valid_keys and valid_list and valid_type else 409
        if not valid_keys:
            error=bad_keys
        if not valid_list and valid_keys:
            error=not_list
        if not valid_type and valid_list:
            error=bad_args_type
        if valid_type:
            arguments = params[arguments_str]
    return result,error,response_code,arguments


def stack_add_argument():
    result, error, response_code, params = get_json(request.get_data())
    result, error, response_code, arguments = get_arg_list(params)
    stack.extend(arguments)
    if response_code == 200:
        result = str(len(stack))
    else:
        result = ''
    return to_json(result,error)


def get_operation(params:dict):
    pass

def stack_operate_endpoint():
    params = request.args.to_dict()
    result, error, response_code, operation = get_operation(params)
