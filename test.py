def is_admin(*args, **kwargs):
    if kwargs['num1'] > 5:
        return True
    return False


def make_pretty(func):
    def inner(*args, **kwargs):
        print("I got decorated")
        if is_admin(*args, **kwargs):
            func(*args, **kwargs)
        else:
            print("you are not allowed to call this function")

    return inner


@make_pretty
def ordinary(num1, num2):
    print(f"I am ordinary my first parmaeter is {num1} my second parameter is {num2}")


if __name__ == '__main__':
    ordinary(num1=6, num2=6)
