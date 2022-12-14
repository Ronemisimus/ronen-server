import logging
from global_strings import reqNumStr
from time import perf_counter

# globals
extra_dict = {reqNumStr:0}

def log_request_at_start(resource, verb):
    extra_dict[reqNumStr]+=1
    reqLogger = logging.getLogger('request-logger')
    reqLogger.info('Incoming request | #%d | resource: %s | HTTP Verb %s',extra_dict[reqNumStr],resource,verb,extra=extra_dict)
    return perf_counter()

def log_request_at_end(pref_count):
    mstime = perf_counter()-pref_count
    reqLogger = logging.getLogger('request-logger')
    reqLogger.debug('request #%d duration: %dms',extra_dict[reqNumStr],int(mstime*1000),extra=extra_dict)

def log_stack_size(size,stack):
    stackLogger = logging.getLogger('stack-logger')
    stackLogger.info('Stack size is %d',size,extra=extra_dict)
    stackLogger.debug('Stack content (first == top): %s', list(stack)[::-1],extra=extra_dict)

def log_stack_add_args(size,added,arglist):
    stackLogger = logging.getLogger('stack-logger')
    stackLogger.info('Adding total of %d argument(s) to the stack | Stack size: %d',added,size,extra=extra_dict)
    stackLogger.debug('Adding arguments: %s | Stack size before %d | stack size after %d', ','.join([str(a) for a in arglist]), size-added, size, extra=extra_dict)


def log_stack_operate(op, res, size,args):
    stackLogger = logging.getLogger('stack-logger')
    stackLogger.info('Performing operation %s. Result is %s | stack size: %d',op,str(res),size,extra=extra_dict)
    stackLogger.debug('Performing operation: %s(%s) = %s', op, ','.join([str(a) for a in args]), str(res), extra=extra_dict)

def log_stack_delete(removed,size):
    stackLogger = logging.getLogger('stack-logger')
    stackLogger.info('Removing total %d argument(s) from the stack | Stack size: %d',removed,size,extra=extra_dict)

def log_error(error_message,is_stack):
    if error_message != '':
        if is_stack:
            Logger = logging.getLogger('stack-logger')
        else:
            Logger = logging.getLogger('independent-logger')
        Logger.error('Server encountered an error ! message: %s',error_message,extra=extra_dict)


def log_independent_operation(op,args,res):
    independentLogger = logging.getLogger('independent-logger')
    independentLogger.info('Performing operation %s. Result is %s',op,str(res),extra=extra_dict)
    independentLogger.debug('Performing operation: %s(%s) = %s', op, ','.join([str(a) for a in args]), str(res), extra=extra_dict)


