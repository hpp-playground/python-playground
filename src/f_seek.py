import os
from pathlib import Path

hoge = Path("./hoge.txt")
hoge.touch()

with hoge.open("r+") as f:
    f.seek(0, os.SEEK_END)
    print(f.tell())
    f.write("hoge\n")
