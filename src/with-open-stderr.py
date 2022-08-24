import sys

print(sys.stderr.__enter__())

with sys.stderr as f:
    f.write("error\nerror desu\n")

print("error", file=sys.stderr)
