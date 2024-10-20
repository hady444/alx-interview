#!/usr/bin/python3
"""
Solving Prime game
"""


def findPrim(prev):
    """
    find next prim number
    """
    if prev == 2:
        return 3
    elif prev == 3:
        return 5
    elif prev == 5:
        return 7
    turn = prev + 1
    while (1):
        if (turn in [2, 3, 5, 7]):
            return turn
        if ((turn % 2) != 0 and (turn % 3) != 0 and
                (turn % 5) != 0 and (turn % 7) != 0):
            return turn
        turn += 1


def isWinner(x, nums):
    """ Who is the winner """
    game = {'Maria': 0, 'Ben': 0}
    for rounde in nums:
        prev = 1
        seq = [True] * rounde
        falses = 0
        turn = True      # for Maria turn
        while (falses < rounde):
            p = findPrim(prev)
            prev = p
            change = False
            for i in range(1, rounde + 1):
                if seq[i - 1] and (i % p) == 0:
                    seq[i - 1] = False
                    change = True
            if not change:
                if turn:
                    game['Ben'] += 1
                else:
                    game['Maria'] += 1
                break
            turn = not turn
    return 'Maria' if game['Maria'] > game['Ben'] else 'Ben'
