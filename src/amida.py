import random

names = [
    "dora",
]


def main():
    """
    write a text file filled with fibonacci
    """
    with open("fib.txt", "w") as f:
        for i in range(1, 100):
            f.write(str(i) + "\n")
            
    

    