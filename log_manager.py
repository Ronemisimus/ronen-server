from flask import request,make_response
from logs import log_request_at_start, log_request_at_end


def logger_level_read_endpoint():
    mstime = log_request_at_start(request.path,request.method)
    log_request_at_end(mstime)



def logger_level_write_endpoint():
    mstime = log_request_at_start(request.path,request.method)
    log_request_at_end(mstime)


