import traceback


def catch_exception(func):
    def wrapper(*args, **kwargs):
        try:
            print(f">>> Start {func.__name__}.")
            func(*args, **kwargs)
            print(f">>> End {func.__name__} without any Exceptions.")

        except Exception as e:
            print(f">>> {func.__name__} raised error.")
            for t in traceback.format_exc().split("\n")[:-1]:
                print(f"... {t}")
    
    return wrapper

if __name__ == "__main__":
    @catch_exception
    def divide_by_zero():
        print(1 / 0)
    
    divide_by_zero()
