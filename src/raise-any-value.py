class MyObj(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

obj = MyObj(1, 2, 3)

raise obj from ValueError("this is an invalid value.")