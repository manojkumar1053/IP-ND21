def add_four(func):
    def wrapper_func(*args, **kwargs):
        print("Adding 4")
        result = func((args, kwargs))
        return result + 4

    return wrapper_func


def double(func):
    def wrapper_func(*args, **kwargs):
        print("Double the result ")
        result = func((args, kwargs))
        return result * 2

    return wrapper_func()


@double
# add_four
def add(a, b):
    print(f"we are adding {a} and {b}")
    print(a + b)


add(9, 7)
