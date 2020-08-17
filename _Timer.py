import time
from numba import jit


# ループでprintを使ったりすると瞬時に表示されないなどの問題があるため
_print = print
def print(text):
    _print(text, flush=True)


class Timer:
    def __init__(self):
        self.times = []
        self.sum = 0.0
        self.cnt = 0

    def timer(self, iteration=1):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for i in range(iteration):
                    st = time.time()
                    func(*args, **kwargs)
                    diff = time.time() - st
                    self.times.append(diff)
                    self.cnt += 1
                    self.sum += diff

                print(f"Average time : {self.sum / self.cnt}")
                print(f"Maximum time : {max(self.times)}")
                print(f"Minimum time : {min(self.times)}")

            return wrapper
        
        return decorator

timer = Timer()

@timer.timer(100)
def hoge():
    print("hoge")
    time.sleep(0.01)

hoge()
