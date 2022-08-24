a = [list(range(5)) for _ in range(3)]
b = [list(range(5, 10)) for _ in range(3)]

print([val for _ in b for val in a if val is not None])
print([val for a in b for val in a if val is not None])

print([y for x in range(5) for y in range(5, 10)])
