import sys

print(sys.stdout.__enter__())

with sys.stdout as f:
    f.write("test\ntest desu\n")

print("test", file=sys.stdout)