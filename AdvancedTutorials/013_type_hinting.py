def myFunc(a: int, b: str) -> str:
    return str(a) + b


# mypy tool can be used to check the type hinting of the code

# python is dynamically typed language, so the type hinting is not enforced


def set_list(lst: list[int]): # This will not work in python 3.8 or below
    pass