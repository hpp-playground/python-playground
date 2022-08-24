def main():
    with open("./test.txt") as f:
        for line in f:
            print(line.strip())
            input()


if __name__ == "__main__":
    main()
