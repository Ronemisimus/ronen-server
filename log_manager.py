from flask import request,make_response
from logs import log_request_at_start, log_request_at_end
from global_strings import no_logger_name,logger_missing, no_logger_level, invalid_level
import logging

valid_levels = {
    'ERROR':logging.ERROR,
    'INFO':logging.INFO,
    'DEBUG':logging.DEBUG
}

def get_logger_name(params:dict):
    result =''
    error = ''
    response_code = 200
    name = ''

    valid_keys = 'logger-name' in params.keys()
    existing_logger = valid_keys and str(params['logger-name']) in logging.root.manager.loggerDict

    response_code = response_code if existing_logger else 409

    if not valid_keys:
        error = no_logger_name
    elif not existing_logger:
        error = logger_missing(str(params['logger-name']))
    else:
        name = str(params['logger-name'])
    return result,error,response_code,name

def get_logger_level(result, error, response_code, params):
    level = ''
    if response_code == 200:
        valid_keys = 'logger-level' in params.keys()
        valid_level = str(params['logger-level']) in valid_levels.keys()

        response_code = response_code if valid_level else 409

        if not valid_keys:
            error = no_logger_level
        elif not valid_level:
            error = invalid_level(str(params['logger-level']))
        else:
            level = str(params['logger-level'])
    return result, error,response_code, level



def logger_level_read_endpoint():
    mstime = log_request_at_start(request.path,request.method)
    params = request.args.to_dict()
    result, error, response_code, name = get_logger_name(params)
    result = logging.getLevelName(logging.getLogger(name).level) if response_code==200 else ''
    log_request_at_end(mstime)
    return make_response(str(result) if response_code==200 else error,response_code)



def logger_level_write_endpoint():
    mstime = log_request_at_start(request.path,request.method)
    params = request.args.to_dict()
    result, error, response_code, name = get_logger_name(params)
    result, error, response_code, level = get_logger_level(result, error, response_code, params)
    if response_code==200:
        logging.getLogger(name).setLevel(valid_levels[level])
    log_request_at_end(mstime)
    return make_response(str(level) if response_code==200 else error,response_code)

