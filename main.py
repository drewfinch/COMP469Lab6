# Two players (Max, Min) are given a list of numbers, e.g. [1,2,5,2]
# 1. The players take turn in picking a number from either the beginning or the end of the
# list.
# 2. Max starts first.
# 3. The game is over when there are no more numbers left in the list.
# 4. Winner: the player with more collected points
# 5. Min and Max both play optimally
INFINITY = 100000000000


class Node:
    def __init__(self, data, parent):
        self.parent = parent
        self.children = []
        self.data = data

def get_successors(tree):
    children = []
    return children


def max(numbers):
    v = -INFINITY

    for each successor of state:
        v = max(v, min - value(successor))
    return v


def min(numbers):
    return 0


def print_winner(min_score, max_score):
    print("hi")


numbers = [1, 2, 5, 2]
min_score = 0
max_score = 0

while len(numbers):
    max_score = max_score + max(numbers)
    min_score = min_score + min(numbers)

print_winner(min_score, max_score)
