"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = random_score()
    result = find_score(score)
    print(result)


def find_score(score):
    if score < 0 or score > 100:
        result = "Invalid Score"
    elif score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


def random_score():
    score = (random.randint(1, 100))
    return score


main()