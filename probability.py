"""Calculates the probability of dice"""

# Source: http://rosettacode.org/wiki/Dice_game_probabilities#Python
from itertools import product
from typing import Tuple, List

def gen_dict(n_faces: int, n_dice: int) -> Tuple[List, int]:
    """
    The gen_dict function generates a dictionary of the number of times each
    sum appears for a given number of dice. For example, if you roll three six-sided
    dice, there are 21 possible sums (3 through 24). The gen_dict function will count
    how many times each sum appears when rolling three six-sided dice

    :param n_faces:int: Specify the number of faces on each die
    :param n_dice:int: Specify the number of dice to roll
    :return: A dictionary with the number of occurences of each possible sum
    """
    counts = [0] * ((n_faces + 1) * n_dice)
    for t in product(range(1, n_faces + 1), repeat=n_dice):
        counts[sum(t)] += 1
    return counts, n_faces ** n_dice


def beating_probability(n_sides1: int, n_dice1: int, n_sides2: int, n_dice2: int) -> float:
    """
    The beating_probability function computes the probability that a player with n_dice and n_sides
    beats another player with m_dice and m_sides. The function returns this probability as a float.
    
    :param n_sides1: Determine the number of sides on each die in player 1's dice
    :param n_dice1: Determine the number of dice that are being thrown
    :param n_sides2: Determine the number of sides on the second die
    :param n_dice2: Determine the number of dice in player 2's hand
    :return: The probability of the first dice beating the second
    """
    c1, p1 = gen_dict(n_sides1, n_dice1)
    c2, p2 = gen_dict(n_sides2, n_dice2)
    p12 = float(p1 * p2)

    return sum(p[1] * q[1] / p12
               for p, q in product(enumerate(c1), enumerate(c2))
               if p[0] > q[0])


print(beating_probability(4, 9, 6, 6))
print(beating_probability(10, 5, 7, 6))
