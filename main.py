# Two players (Max, Min) are given a list of numbers, e.g. [1,2,5,2]
# 1. The players take turn in picking a number from either the beginning or the end of the
# list.
# 2. Max starts first.
# 3. The game is over when there are no more numbers left in the list.
# 4. Winner: the player with more collected points
# 5. Min and Max both play optimally

class Node:
    def __init__(self, data, parent):
        self.parent = parent
        self.children = []
        self.data = data


def max(numbers):
    return


def min(numbers):
    return


def print_winner(min_score, max_score):
    print("hi")


numbers = [1, 2, 5, 2]
min_score = 0
max_score = 0

while len(numbers):
    max(numbers)
    min(numbers)

print_winner(min_score, max_score)
