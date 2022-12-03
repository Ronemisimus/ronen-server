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
bad_keys = "Error: no 'operation' or 'arguments' json keys"
missing_args = "Error: Not enough arguments to perform the operation "
extra_args = "Error: Too many arguments to perform the operation "
not_list = "Error: prameter arguments is not a list"
bad_args_type = "Error: arguments is not a list of ints only"
div_by_0 = "Error while performing operation Divide: division by 0"

to_json = lambda res,error: json.dumps({
    result_str:res,
    error_str:error
})