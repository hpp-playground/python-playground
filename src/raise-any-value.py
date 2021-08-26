class MyObj(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        print(*args)

obj = MyObj(1, 2, 3)

raise obj