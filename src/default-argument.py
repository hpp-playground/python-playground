def test(arg1 = 0, arg2 = []):
    arg1 += 1
    arg2.append(arg1)
    return (arg1, arg2)

print(*test())
print(*test())
print(*test())
print(*test())
print(*test())
