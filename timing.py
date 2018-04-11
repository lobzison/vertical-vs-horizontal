"""Decorator / functional operator that takes a function as input, and returns a 
modified version of the function that times how long the function takes to run (in
minutes), and prints out how long the function took to run.
"""

from __future__ import print_function
import functools
import inspect
import time
 
    
def optional_args(decorator):
    @functools.wraps(decorator)
    def dispatcher(*args, **kwargs):
        one_arg = len(args) == 1 and not kwargs
        if one_arg and inspect.isfunction(args[0]):
            decor_obj = decorator()
            return decor_obj(args[0])
        else:
            return decorator(*args, **kwargs)
    return dispatcher


@optional_args
def time_function(what=None, digits=5, unit='minutes'):
    """Decorator that takes a function, and transforms it into a function that
    prints out how long it took to execute. This decorator may be easily 
    altered to output the time to a logging file instead of printing.
    
    Parameters
    ----------
    what : string (optional)
        An optional description of the function being executed.
        
    digits : int (optional)
        The number of digits to round the timing to
        
    unit : string (default is minutes)
        The unit to measure time in, choices are ['minutes', 'seconds']
    
    Returns
    -------
    master_function : function
        A modified version of the input function that prints out how long the 
        function took to execute
    """
    def master_function(func):
        def func_wrapper(*args, **kwargs):
            
            # The type of available units
            units = {
                'minutes' : 60,
                'seconds' : 1
            }
            assert unit in units.keys(), 'Your given unit is not valid'
            
            # Start timing, run the function, measure the time elapsed
            start = time.time()
            results = func(*args, **kwargs)
            elapsed = (time.time() - start) / units.get(unit)
            if digits:
                elapsed = round(elapsed, digits)
                
            # Print the amount of time everything took
            if what:
                print('{0} finished. Time elapsed ({1}): {2}'.format(
                what, unit, str(elapsed)), '\n')
            else:
                print('Time elapsed ({0}): {1}'.format(unit, str(elapsed)), '\n')
            return results
        return func_wrapper
    return master_function