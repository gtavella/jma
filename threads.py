"""
NOTE: THE CODE IS NOT STABLE, NEEDS IMPROVEMENT.
I was JMAing (just messing around), it is not complete.
"""

from threading import Thread
from multiprocessing import Process
import time





def get_time_details_str(func, time_elapsed_sec): 
    time_elapsed_millisec = time_elapsed_sec * (10**3)
    time_elapsed_microsec = time_elapsed_sec * (10**6)
    atomic_op_fn_name = ctx['atomic_operation'].__name__ # type: ignore
    return (
        f"\nTo perform the atomic operation with function '{atomic_op_fn_name}', "+
        f"the function '{func.__name__}' took: \n" +
        f"---------------------------------\n" +
        f"| s   | {time_elapsed_sec}       \n" +
        f"| ms  | {time_elapsed_millisec}  \n" +
        f"| μs  | {time_elapsed_microsec}  \n" +
        f"---------------------------------\n\n"
    )



def measure_time(func):
    def inner(*args, **kwargs):
        t1 = time.perf_counter()
        func(*args, **kwargs)
        t2 = time.perf_counter()
        time_elapsed_sec = t2 - t1
        print(get_time_details_str(func, time_elapsed_sec))
    return inner



def inject_params(func):
    def inner(*args, **kwargs):
        # just combine tuples. order: first the standard parameters, 
        # then custom parameters
        all_args = _std_args + args 
        # shallow (or deep?) copy of dictionary
        all_kwargs = kwargs.copy()
        all_kwargs.update(_std_kwargs)
        func(*all_args, **all_kwargs)
    return inner



def multiply(*args, **kwargs):
    x = args[0]
    x * 10
    
    
def _sum(*args, **kwargs):
    pass
    

atomic_operations = {
    "multiply": multiply
}


def set_atomic_operation(ctx, atomic_op_name) -> None:
    ctx["atomic_operation"] = atomic_operations[atomic_op_name]
    

# ATOMIC OPERATIONS ********




"""
This is the simplest operation to be performed.
"Atomic" means that it is shared by ALL functions, 
does not depend on any other code, and is the most minimal
unit of code to be executed by all functions.
If it does depend on other code, then all functions should 
have such a dependency.
"""





# Calculate the mean from 1 to 10 milions.
# measure the seconds it takes, and the result



# SYNC
@inject_params
@measure_time
def do_computation_sync(*args, ctx, **kwargs):
    n = args[0]
    for x in range(n):
        ctx["atomic_operation"](x, *args, **kwargs)



# MULTITHREAD
@inject_params
@measure_time
def do_computation_multithread(*args, ctx, **kwargs):
    pass



# MULTIPROCESS
@inject_params
@measure_time
def do_computation_multiprocess(*args, ctx, **kwargs):
    # divide the work in 5 processes
    limit = args[0]
    # be careful with float values and rounding
    n_processes = 5 
    # current upper bound
    jump = limit // n_processes
    start = 0
    
    for pn in range(1, n_processes+1):
        # start a process
        p = Process(target=multiply, args=args, kwargs=kwargs)
        p.name = f"giuseppe's process n-{pn}"
        
        next_start = start+jump
        
        for i in range(start, next_start):
            print(f"current number {i}")        
        print()
        start = next_start
        




# standard positional and keyword arguments 
# this means pass these to all functions without
# hardcoding them manually 
# ORDER of positional arguments: first standard arguments
# (because they are guaranteed to be passed, then custom arguments)
_std_args = (100,)
_std_kwargs = {}
ctx = {
    "atomic_operation": None    
}



set_atomic_operation(ctx, "multiply")


# do_computation_sync(ctx=ctx)
# do_computation_multithread()
do_computation_multiprocess(ctx=ctx)

