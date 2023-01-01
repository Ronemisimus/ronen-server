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
    reqLogger.debug('request #%d duration: %dms',extra_dict[reqNumStr],int(mstime*1000),extra=extra_dict)

def log_stack_size(size,stack):
    stackLogger = logging.getLogger('stack')
    stackLogger.info('Stack size is %d',size,extra=extra_dict)
    stackLogger.debug('Stack content (first == top): %s', list(stack),extra=extra_dict)

def log_stack_add_args(size,added,arglist):
    stackLogger = logging.getLogger('stack')
    stackLogger.info('Adding total of %d argument(s) to the stack | Stack size: %d',added,size,extra=extra_dict)
    stackLogger.debug('Adding arguments: %s | Stack size before %d | stack size after %d', arglist, size-added, size, extra=extra_dict)


