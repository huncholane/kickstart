import time


def timeit(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        dur = time.time() - start
        print(f.__name__, dur, "seconds")
        return result

    return wrapper
