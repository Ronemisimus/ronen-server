from flask import make_response, request
from global_strings import *
from logs import log_request_at_start, log_request_at_end

#functions

def test_params(error:str,response_code:int, params:dict):
    result = ''
    if response_code ==200:
        valid_keys = operation_str in params.keys() and arguments_str in params.keys()
        valid_operation = valid_keys and ( unary_op(op(params)) or binary_op(op(params)) )
        valid_arguments_len = valid_operation and type(params[arguments_str]) == list and \
            ( (len(params[arguments_str])==1 and unary_op(op(params)) ) or  
            (len(params[arguments_str])==2 and binary_op(op(params)) ))
        too_long_args = valid_operation and type(params[arguments_str]) == list and \
            ( (len(params[arguments_str])>1 and unary_op(op(params)) ) or  
            (len(params[arguments_str])>2 and binary_op(op(params)) ))
        too_short_args = valid_operation and type(params[arguments_str]) == list and \
            ( (len(params[arguments_str])<1 and unary_op(op(params)) ) or  
            (len(params[arguments_str])<2 and binary_op(op(params)) ))
        valid_arguments_type = valid_arguments_len and type(params[arguments_str][0])==int and \
            (len(params[arguments_str]) == 1 or type(params[arguments_str][1])==int)
        response_code = response_code if valid_arguments_type else 409
        if not valid_keys:
            error = bad_keys
        if not valid_operation and valid_keys:
            error = bad_operation + params[operation_str]
        if not valid_arguments_len and valid_operation:
            error = missing_args + params[operation_str] if too_short_args else error
            error = extra_args + params[operation_str] if too_long_args else error
            error = not_list if error=='' else error
        if not valid_arguments_type and valid_arguments_len:
            error = bad_args_type
    return result, error, response_code


def use_params(error:str,response_code:int, params:dict):
    result = ''
    if response_code == 200:
        operation = op(params)
        arguments = params[arguments_str]
        if unary_op(operation):
            if operation == "fact" and arguments[0]<0:
                error = negative_fact
                response_code = 409
            else:
                result = unary_operations[operation](arguments[0])
        if binary_op(operation):
            if operation == 'divide' and arguments[1]==0:
                error = div_by_0
                response_code = 409
            else:
                result = binary_operations[operation](arguments[0],arguments[1])
        return result, error, response_code
    else:
        return result, error, response_code


def calculate_endpoint():
    mstime = log_request_at_start(request.path,request.method)
    result, error, response_code, params = get_json(request.get_data())
    result, error, response_code = test_params(error,response_code,params)
    result, error, response_code = use_params(error,response_code,params)
    log_request_at_end(mstime)
    return make_response( to_json(result,error) , response_code)