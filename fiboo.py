def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def name():
    print(__name__)

    if __name__ == "__main__":
        name()
        import sys
        fib(int(sys.argv[1]))
        