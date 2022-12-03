import json
from flask import make_response, request

#strings
operation_str = "operation"
arguments_str = "arguments"

#errors
bad_json = "Error: body not in json format"
negative_fact = "Error while performing operation Factorial: not supported for the negative number"
bad_operation = "Error: unknown operation: "
bad_keys = "Error: no 'operation' or 'arguments' json keys"
missing_args = "Error: Not enough arguments to perform the operation "
extra_args = "Error: Too many arguments to perform the operation "
not_list = "Error: prameter arguments is not a list"
bad_args_type = "Error: arguments is not a list of ints only"
div_by_0 = "Error while performing operation Divide: division by 0"

#global_objects
plus = lambda a,b: a+b
minus = lambda a,b: a-b
times = lambda a,b: a*b
divide = lambda a,b: a//b
pow = lambda a,b: a**b
from math import factorial

binary_operations = {
    'plus':plus,
    'minus':minus,
    'times':times,
    'divide':divide,
    'pow':pow
}
binary_op = lambda s: s in binary_operations.keys()

unary_operations = {
    'abs':abs,
    'fact':factorial
}
unary_op = lambda s: s in unary_operations.keys()

op = lambda params: params[operation_str].lower()

#functions
def get_json(body:str):
    result = ''
    error = ''
    params = []
    response_code = 200
    try:
        params = json.loads(body)
    except json.JSONDecodeError:
        error=bad_json
        response_code = 418
    return result, error, response_code, params

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
    result, error, response_code, params = get_json(request.get_data())
    result, error, response_code = test_params(error,response_code,params)
    result, error, response_code = use_params(error,response_code,params)
    return make_response(json.dumps({
        "result":result,
        "error-message":error
    }), response_code)