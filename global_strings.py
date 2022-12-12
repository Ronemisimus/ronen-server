import json

#strings
operation_str = "operation"
arguments_str = "arguments"
result_str="result"
error_str="error-message"
#errors
bad_json = "Error: body not in json format"
negative_fact = "Error while performing operation Factorial: not supported for the negative number"
bad_operation = "Error: unknown operation: "
bad_keys = "Error: missing json keys"
missing_args = "Error: Not enough arguments to perform the operation "
extra_args = "Error: Too many arguments to perform the operation "
not_list = "Error: prameter arguments is not a list"
bad_args_type = "Error: arguments is not a list of ints only"
div_by_0 = "Error while performing operation Divide: division by 0"
missing_query = "Error: missing query parameter"
missing_args_stack = lambda op,req_arg,cur_arg: f"Error: cannot implement operation {op}. It requires {req_arg} arguments and the stack has only {cur_arg} arguments"
not_int = "Error: argument is not an int"
too_many_remove = lambda remove, curr: f"Error: cannot remove {remove} from the stack. It has only {curr} arguments"

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

to_json = lambda res,error: json.dumps({
    a:b for (a,b) in [(result_str,res) if res!='' else (error_str,error)]
})

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