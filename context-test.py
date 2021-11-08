class MyContext(object):
    def __init__(self, val=42):
        self.val = val
        print("Initializing context")

    def __enter__(self):
        print("Enter Context")
        return self.val

    def __exit__(self, exctype, value, tb):
        if exctype is not None:
            print(f"CM body raised{exctype.__name__}({value})")
            print(f"Inspect {tb}")

        print("Exiting Context")
        return True


with MyContext() as t:
    print("The answer is", t)

with MyContext(33) as t:
    x = t / 0
    print(x)

with MyContext() as t:
    x = t/7
    print(x)

with MyContext(21) as t:
    x = t/7
    print(x)
