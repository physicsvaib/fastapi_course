from typing import Any, Callable

routes: dict[str, Callable[[Any], Any]] = {}


def get(path):
    def fun(func):
        routes[path] = func
        return func

    return fun


@get("home")
def get_home():
    return "Home Sweet Home"


res = ""

while res != "quit":
    res = input("> ")
    if res in routes:
        print(routes[res]())
    else:
        print("No Idea")
