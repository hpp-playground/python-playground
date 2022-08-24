from typing import List
import sys
from pathlib import Path


class Hoge:
    @classmethod
    def get_class_paths_in_my_project(cls) -> List[Path]:
        # specify the root directory of our project
        src_dir = Path.cwd() / "src"
        ret = []
        # lists classes with Method Resolution Order (MRO)
        for c in cls.mro():
            m = sys.modules[c.__module__]
            try:
                path = Path(m.__file__)
            except AttributeError:  # this module is `builtins` module
                continue
            try:
                path.relative_to(src_dir)
            except ValueError:  # not in src dir
                continue
            ret.append(path)
        return ret

    @classmethod
    def print_paths(cls):
        print(cls.__name__)
        for path in cls.get_class_paths_in_my_project():
            print(path)


if __name__ == "__main__":
    Hoge.print_paths()
