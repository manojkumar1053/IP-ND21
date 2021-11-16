from contextlib import contextmanager


@contextmanager
def my_context(val=42):
    try:
        print("Initialing Context")
        yield val
    except BaseException as err:
        print(f"CM body raised {err.__class__.__name__}({err.args[0]})")
        print(f"Inspect {err.__traceback__}")
    finally:
        print("Exiting context")

# G
with my_context() as t:
    print("The answer is", t)

with my_context(33) as t:
    x = t / 0
    print(x)

with my_context(33) as t:
    x = t / 0.0
    print(x)
