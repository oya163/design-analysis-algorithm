'''
    CMSC 641 Fall 2018
    HW1 - Cookie Thief Problem
    Due Date - 09/13/2018

    Greedy Algorithm

    This algorithm maximizes the number of cookies
    stolen from a given jar.
'''


def steal_cookie(jar):
    x = [None] * len(jar)
    x[0] = jar[0]
    x[1] = max(jar[0], jar[1])
    for i in range(2, len(jar)):
        x[i] = max(jar[i] + x[i - 2], x[i - 1])

    return x[len(jar) - 1]

def main():
    jar_with_cookies = [6, 5, 2, 8, 3, 1, 7, 3, 9]
    print('Maximum number of cookies stolen = ', steal_cookie(jar_with_cookies))


if __name__ == '__main__':
    main()