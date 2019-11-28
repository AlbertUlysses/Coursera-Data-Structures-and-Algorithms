# Uses python3
import sys

def gcd(a, b):
    while b: # O(n)
        a, b = b, a%b # O(1)
    return a # O(1)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))

""" is O(n) """
