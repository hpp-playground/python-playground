import fcntl, os

# with open("test.txt", "r") as f:
#     lines = f.readlines()

# print(lines)
# with open("test.txt", "w") as f:
#     x = input("prompt > ")
#     f.write("\n".join(lines + [x]))
#     f.flush()

filename = 'test.txt'
with open(filename, 'r+') as f:
    try:
        fcntl.flock(f, fcntl.LOCK_EX)
        data = f.readlines()
        f.truncate(0)
        f.seek(os.SEEK_SET)
        data.append(input("prompt > ")+"\n")
        f.writelines(data)
        print(data)
    except IOError:
        print('flock() failure')