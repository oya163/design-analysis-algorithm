'''
    CMSC 641 Fall 2018
    HW1 - String Transform
    Due Date - 09/13/2018

    Dynamic Programming

    This algorithm gives minimum number
    of operations required to transform
    one string into another

    Reference - JHU notes
'''


def string_transform(x, y):
    if len(x) == 0: return len(y)
    if len(y) == 0: return len(x)
    delta = 1 if x[-1] != y[-1] else 0
    diag = string_transform(x[:-1], y[:-1]) + delta
    vert = string_transform(x[:-1], y) + 1
    horz = string_transform(x, y[:-1]) + 1
    return min(diag, vert, horz)


def main():
    s1 = "oyesh"
    s2 = "singh"
    print('Minimum number of operations required = ', string_transform(s1, s2))


if __name__ == '__main__':
    main()