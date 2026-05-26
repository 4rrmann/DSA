#TIMING FUNCTION EXECUTION
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer #now, below the func is always go through the `timer` func
def eg_func(n):
    time.sleep(n)

eg_func(2)