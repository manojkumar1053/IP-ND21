# Read
with open('queries.txt', 'r') as inline:
    contents = inline.read()

# print(type(contents))
print(contents)
queries = contents.split('\n')
print(queries)
print(queries[::2])

normalized = [query.strip().lower() for query in queries[::2]]

print(normalized)

# Write
with open('normalized-quries.txt', 'w') as outfile:
    for query in normalized:
        outfile.write(query + '\n')
