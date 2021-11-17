import logging

a, b = 5, 0

try:
    c = a / b

except Exception as e:
    logging.warning("Exception Occured", exc_info=True)

print("ons")
