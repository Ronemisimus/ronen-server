from .global_strings import *
from flask import request, make_response
import json
#global objects
stack = []

def stack_size_endpoint():
    return make_response(to_json(res=str(len(stack)),error=''),200)


def get_arg_list(result:int, error:str, response_code:int, params:dict):
    arguments = []
    if response_code==200:
        valid_keys = arguments_str in params.keys()
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
    result, error, response_code, arguments = get_arg_list(result,error,response_code,params)
    stack.extend(arguments)
    if response_code == 200:
        result = str(len(stack))
    else:
        result = ''
    return make_response(to_json(result,error),response_code)


def get_operation(params:dict):
    result = ''
    error = ''
    response_code = 200
    operation = ''
    valid_keys = operation_str in params.keys()
    valid_operation = valid_keys and ( unary_op(op(params)) or binary_op(op(params)) )
    valid_amount  = valid_operation and ( ( unary_op(op(params)) and len(stack)>0 ) or
        ( binary_op(op(params)) and len(stack)>1 ) )
    required_args = 1 if unary_op(op(params)) else 2 if binary_op(op(params)) else 0
    current_args = len(stack)
    response_code = response_code if valid_keys and valid_operation and valid_amount else 409
    if not valid_keys:
        error = missing_query
    if not valid_operation and valid_keys:
        error = bad_operation + params[operation_str]
    if not valid_amount and valid_operation:
        error = missing_args_stack(params[operation_str],required_args,current_args)
    if valid_amount:
        operation = op(params)
    return result,error,response_code,operation


def do_operation(result,error:str,response_code:int,operation:str):
    if response_code==200:
        if unary_op(operation):
            if operation == 'fact' and stack[-1]<0:
                error = negative_fact
                response_code = 409
            else:
                result = unary_operations[operation](stack.pop())
        if binary_op(operation):
            if operation == 'divide' and stack[-2]==0:
                error = div_by_0
                response_code = 409
            else:
                x=stack.pop()
                y=stack.pop()
                result = binary_operations[operation](x,y)
    return result, error, response_code
            


def stack_operate_endpoint():
    params = request.args.to_dict()
    result, error, response_code, operation = get_operation(params)
    result, error, response_code = do_operation(result,error,response_code,operation)
    return make_response(to_json(result,error),response_code)

