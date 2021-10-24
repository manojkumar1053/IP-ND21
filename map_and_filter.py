# Practice with map
# Fill out the rest of the map functions.
# You can define additional functions if you need to.
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)

def str_reverse(s):
    return s[::-1]


def index_2(s):
    return s[:2]


l = ["apple", "orange", "pear"]

a = list(map(len, l))
# print(a)
b = list(map(str.upper, l))

c = list(map(str_reverse, l))

d = list(map(index_2, l))

# Practice with filter
# Fill out the rest of the filter functions.
# You can define additional functions if you need to.
# (a) range(100) => (0, 3, 6, 9, ...)  (div by 3)
# (b) range(100) => (0, 5, 10, 15, ...)  (div by 5)
# (c) range(100) => (0, 15, 30, 45, ...)  (div by 15)
# (d) range(100) => (1, 2, 4, 7, 8, 11, 13, 14, 16, 17, ...)  (not div by 3 and not div by 5)

l2 = list(range(100))

# def divide_by_3(n):
#     return n%3 == 0

# def divide_by_5(n):
#     return n%5 == 0

# def divide_by_15(n):
#     return n%15 == 0

# def not_divided_by_3_5(n):
#     return n%3 != 0 and n%5 != 0

# a = list(filter(divide_by_3, l2))
# b = list(filter(divide_by_5, l2))
# c = list(filter(divide_by_15, l2))
# d = list(filter(not_divided_by_3_5, l2))

a = list(filter(lambda x: x % 3 == 0, l2))
b = list(filter(lambda x: x % 5 == 0, l2))
c = list(filter(lambda x: x % 15 == 0, l2))
d = list(filter(lambda x: x % 3 != 0 and x % 5 != 0, l2))
