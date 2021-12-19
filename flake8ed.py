import sys


def hello():
    print("Hello" + 1)


def print_out_syspath():
    print(sys.path )


if __name__ == "__main__":
    hello()
    print_out_syspath()
