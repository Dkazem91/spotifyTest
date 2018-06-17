#!/usr/bin/python3
"""computes the number of ways to make the amount of money with coins of the available denominations"""
solutions = []


def changePossibilities(amount, denoms):
    denoms = list(reversed(sorted(denoms)))
    if denoms == [] or amount == 0:
        print(len(solutions))
        return
    poss = [denoms[0]]
    for x in reversed(denoms):
        while sum(poss) < amount:
            poss.append(x)
        if sum(poss) == amount and poss not in solutions:
            solutions.append(poss)
            poss = [denoms[0]]
        else:
            poss.pop()
    del denoms[0]
    changePossibilities(amount, denoms)

#while researching this I found the dynamic/recursive/greedy solutions to this problem but I wanted to go in from scratch so this is my solution without having used those answers
