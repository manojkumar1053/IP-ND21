from contextlib import contextmanager

settings = {
    'host': "old-test.com", 'port': 80,
    'user': "my-test",
    'password': "old_-wd"

}


@contextmanager
def configure(**kws):
    global settings
    try:
        old_settings = settings.copy()
        settings.update(kws)
        yield
    finally:
        settings = old_settings


with configure(host='localhost', port=70):
    print("connecting to hist: ", settings['host'])
    print("Connecting to port: ", settings['port'])

print("Initial settings: ", settings)
