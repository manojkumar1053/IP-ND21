class CallTracker:
    def __init__(self, func):
        self.func = func
        self.time_called = 0
        self.call_args = []

    def track_call(self, *args, **kwargs):
        self.time_called += 1
        self.call_args.append((args, kwargs))

    def __call__(self, *args, **kwargs):
        self.track_call(args, kwargs)
        return self.func(*args, **kwargs)


@CallTracker
def add(a, b):
    return a + b


print(add(2, 1))

# -
print(add(3, b=4))
