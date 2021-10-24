def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are awesome!"


def greet_bob(greeter_func):
    return greeter_func("bob")


print(greet_bob(say_hello))
