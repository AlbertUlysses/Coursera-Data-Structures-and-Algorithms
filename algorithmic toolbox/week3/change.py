# Uses python3
import sys

def get_change(m):
    count = 0
    while m:
        if m >= 10:
            temp = m // 10
            count = count + temp
            m = m - (temp*10)
        elif m >= 5:
            count += 1
            m = m - 5
        else:
            count = count + m
            m = m - m
    return count 

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
