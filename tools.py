import time


def measure_execution_time(func):
    def inner(*args):
        t0 = time.time()
        func(*args)
        t1 = time.time()

        time_delta = t1 - t0
        print(f'Execution time: {time_delta}')
    
    return inner