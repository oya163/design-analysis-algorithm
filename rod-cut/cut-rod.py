#!/usr/bin/env python
#'''
#    Implementation of rod cutting problem
#    08/08/2017
#    Oyesh
#'''

import argparse
import sys

# Minimum integer (from C++)
INT_MIN = -32767

# Price range for n = 1 to 10 inch length rod
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

parser = argparse.ArgumentParser(description = "Rod cutting problem")

parser.add_argument('--arch','-a', metavar='ARCH', 
                    default='cut-rod', help='cut-rod-ineffi | cut-rod-top-down | cut-rod-bottom-up | bottom-up-solution (default: cut-rod-ineffi')
 
parser.add_argument('-n', default = 5, type=int, metavar = 'N', help = 'number of pieces of rod (default: 5)')

########################################
# Inefficient implementation of rod-cutting
# problem because of exponential running time
def cut_rod(p, n):
    if n == 0:
        return 0
    q = 0
    for i in range (1,n):
        q = max(q, p[i] + cut_rod(p, n-i-1))
    return q

########################################
# Implementation of dynamic programming
# top-down memoization approach

# Helper function
def memoized_cut_rod_aux(p, n, r):
    # Returns the known value
    if r[n] >= 0:
        return r[n]
    
    # Calculates unknow value
    if r[n] == 0:
        q = 0
    else:
        q = INT_MIN
        for i in range(n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-i-1, r))
    
    # Saves calulated value
    r[n] = q
    
    return q
        
# Main function and initializes variable
def memoized_cut_rod(p,n):
    r = [INT_MIN for i in range(0,n+1)]
    r[0] = 0
    return memoized_cut_rod_aux(p,n,r)


########################################
# Implementation of dynamic programming
# bottom_up approach
def bottom_up_cut_rod(p, n):
    r = [INT_MIN for i in range(0, n+1)]
    r[0] = 0
    for j in range(1,n+1):
        q = INT_MIN
        for i in range(j):
            q = max(q, p[i] + r[j-i-1])
        r[j] = q
    
    return r[n]

########################################
# Implementation of dynamic programming
# bottom_up approach with solution
def bottom_up_cut_rod_solution(p,n):
    r = [0 for i in range(0, n+1)]
    s = [0 for i in range(0, n+1)]
    r[0] = 0
    s[0] = 0
    for j in range (1, n+1):
        q = INT_MIN
        for i in range(j):
            if q < p[i] + r[j-i-1]:
                q = p[i] + r[j-i-1]
                s[j] = i+1
        r[j] = q
    return r,s
            

def print_cut_rod_solution(p, n):
    r,s = bottom_up_cut_rod_solution(p, n)
    print('Best revenue: %d' % r[n])
    print('Best solutions: ')
    while n > 0:
        print(s[n])
        n = n - s[n]

########################################
def main():
    args = parser.parse_args()

    if args.arch == 'cut-rod-ineffi':
        print ('Using default')
        print('Result from inefficient algorithm : %d' % cut_rod(p,args.n))
    elif args.arch == 'cut-rod-top-down':
        print('Result from dynamic programming (top-down) : %d' % memoized_cut_rod(p, args.n))
    elif args.arch == 'cut-rod-bottom-up':	
        print('Result from dynamic programming (bottom-up) : %d' % bottom_up_cut_rod(p, args.n))
    elif args.arch == 'bottom-up-solution':
        print('Solution of dynamic programming (bottom-up) :')
        print_cut_rod_solution(p, args.n)
    else:
        print(parser.help())

if __name__== '__main__':
    main()
