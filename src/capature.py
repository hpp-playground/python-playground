def f():
    x = 0

    def g():
        h()

    def h():
        nonlocal x
        x += 1
        print(x)

    g()


f()
