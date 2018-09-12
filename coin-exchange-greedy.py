'''
    Binary Loose Change
    Date - 09/12/2018
    CMSC 641 Fall 2018
    Greedy Algorithm

    This algorithm finds the minimum number of coins
    with power-of-two denominations to exchange N cents.
'''

import math


def coin_change(N, count):
    val = int(math.log(N, 2))
    coin = math.pow(2, math.ceil(val))
    N = N - coin
    count = count + 1
    if N == 0:
        return count
    else:
        return coin_change(N, count)


print('Minimum number of coins required for exchange = ', coin_change(43, 0))