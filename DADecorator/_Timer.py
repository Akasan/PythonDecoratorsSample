import time


def timer(iteration: int = 1, is_max: bool = False, is_min: bool = False):
    """
    Keyword Arguments:
    ------------------
        iteration {int} -- the number of iterations you want to execute the function
                           (default: 1)
        is_max {bool} -- if you want to print the maximum time, set this as True
                         (default: False)
        is_min {bool} -- if you want to print the minimum time, set this as True
                         (default: False)

    Examples:
    ---------
        >>> @timer()
        ... def hoge():
        ...     ...
    """

    def _timer(func):
        def wrapper(*args, **kwargs):
            t = 0
            _min = -1
            _max = -1
            
            for _ in range(iteration):
                st = time.time()
                func(*args, **kwargs)
                et = time.time()
                dt = et - st
                t += dt

                if is_min and (_min == -1 or _min < dt):
                    _min = dt
                if is_max and (_max == -1 or _max > dt):
                    _max = dt

            print(f"Execute {func.__name__} for {iteration} times.")
            print(f"It took {dt / iteration} second as average.")
            if is_min:
                print(f"Minimum time is {_min}")
            if is_max:
                print(f"Maximum time is {_max}")

        return wrapper

    return _timer
