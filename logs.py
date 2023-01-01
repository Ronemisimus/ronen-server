import logging
from global_strings import reqNumStr
from time import perf_counter

# globals
extra_dict = {reqNumStr:0}

def log_request_at_start(resource, verb):
    extra_dict[reqNumStr]+=1
    reqLogger = logging.getLogger('request')
    reqLogger.info('Incoming request | #%d | resource: %s | HTTP Verb %s',extra_dict[reqNumStr],resource,verb,extra=extra_dict)
    return perf_counter()

def log_request_at_end(pref_count):
    mstime = perf_counter()-pref_count
    reqLogger = logging.getLogger('request')
    reqLogger.debug('request #%d duration: %dms',extra_dict[reqNumStr],mstime,extra=extra_dict)