"""
There are 90 cards with all two-digit numbers on them:

10,11,12,...,19

A player takes some of these cards. For each card taken she gets $1. 
However, if the player takes two cards that add up to 100 (say, 23 and 77), at the same time, 
she loses all the money. How much could she get? (In mathematical language: what is the maximum 
number of elements in a subset of \{10,12,...,99\}{10,12,...,99} that does not contain any two 
numbers xx and yy with x+y=100x+y=100?)
"""


result = []
for i in range(10,100):
    pair_result = 100 - i
    if i not in result and pair_result not in result:
        result.append(i)
    

print(len(result))
print([x for x in result])
