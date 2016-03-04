# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if n < 2:
        return n
    else:
        n1, n2 = 1, 1
        for i in range(2, n):
            new_n = n1 + n2 % 10
            n1 = n2
            n2 = new_n
    return n2 % 10

def main():
    x = int(sys.stdin.readline())
    print(get_fibonacci_last_digit(x))

if __name__ == '__main__':
    main()
