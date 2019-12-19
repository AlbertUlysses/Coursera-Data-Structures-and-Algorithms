# Uses python3
import sys

def get_change(m):
    coins = [1, 3, 4]
    if m in coins:
        return m
    #write your code here
    return m // 4

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
