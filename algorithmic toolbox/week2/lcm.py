# Uses python3
import sys

def lcm_naive(a, b):
    c = a
    d = b
    while d:
        c, d = d, c%d
    lcm = (a*b)//c
    return lcm


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

