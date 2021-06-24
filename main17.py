import time


def cached(size):
    def decorator(func):
        func.cached = {}

        def wrapper(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items()))
            if key not in func.cached:
                if len(func.cached) >= size:
                    print("clearing")
                    func.cached.clear()
                print("first time", key)
                func.cached[key] = func(*args, **kwargs), time.time()
            return func.cached[key][0]

        return wrapper
    return decorator


@cached(2)
def sum(a, b):
    return a + b


sum(1, 2)
sum(2, 3)
sum(3, 4)
sum(1, 2)
