"""
__author__      = "Jithin Pradeep"
__email__       = "jithinpr2@gmail.com"
Solution to Josephus problem using recursion
"""

import sys
# todo : Implementing the same using generator functions
# To overcome the recursion limit error,
sys.setrecursionlimit(1500)

def josephus(n,skip):
    if(n == 1):
        return 1
    else :
        return(josephus(n-1,skip)+ skip-1)% n + 1

# input parameter
# number of people available
n = 100
# skip
skip = 2
# skip-1 persons are skipped and the next person is killed in circle. if skip = 2 then person 1 kill 2 and hand over the weapon to 3, and so on
print("For the person to be alive he/she must be in position : ", josephus(n, skip))
