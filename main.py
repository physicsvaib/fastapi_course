def decorate(f):
    def wrap():
        print("*" * 10)
        f()
        print("*" * 10)

    return wrap


@decorate
def log():
    print("Alo")


log()
