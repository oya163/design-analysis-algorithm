'''
    CMSC 641 Fall 2018
    HW2 - Binary Loose Change
    Due Date - 09/18/2018

    Greedy Algorithm

    This algorithm finds the minimum number of coins
    with power-of-two denominations to exchange N cents.
'''

import math


def coin_change(n, count):
    val = int(math.log(n, 2))
    coin = int(math.pow(2, math.ceil(val)))
    print(coin)
    n = n - coin
    count = count + 1
    if n == 0:
        return count
    else:
        return coin_change(n, count)


def main():
    init_count = 0
    n = int(input("Enter a number: "))
    print('Minimum number of coins required for exchange = ', coin_change(n, init_count))


if __name__ == '__main__':
    main()