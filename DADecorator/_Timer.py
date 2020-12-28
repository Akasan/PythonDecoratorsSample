import time


def timer(*vargs, **vkwargs):
    iteration = vkwargs.get("iteration", 1)

    def _timer(func):
        def wrapper(*args, **kwargs):
            st = time.time()
            
            for _ in range(iteration):
                func(*args, **kwargs)

            end = time.time()

            print(f"Execute {func.__name__} for {iteration} times.")
            print(f"It took {(end - st) / iteration} second as average.")

        return wrapper

    return _timer
