# First Version
def a(num: int) -> int:
    f = 0
    for i in range(1, num + 1):
        if num % i == 0:
            f += 1
    return f == 2 and f != 1


def b(num: int) -> None:
    for i in range(1, num + 1):
        if a(i):
            print(i)


b(100)