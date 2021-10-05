# @authors: Christopher Chang, Danial Thai, Drew Finch
INFINITY = 100000000000


class Node:
    def __init__(self, data, parent):
        self.parent = parent
        self.children = []
        self.data = data


def make_tree(numbers):
    root = Node(0, None)
    make_tree_recursive(numbers, root)
    return root


def make_tree_recursive(numbers, node):
    if len(numbers) > 1:
        numbers_copy1 = numbers.copy()
        child1 = Node(numbers_copy1.pop(0), node)
        node.children.append(child1)
        make_tree_recursive(numbers_copy1, child1)

        numbers_copy2 = numbers.copy()
        child2 = Node(numbers_copy2.pop(-1), node)
        node.children.append(child2)
        make_tree_recursive(numbers_copy2, child2)


def is_leaf(node):
    return len(node.children) == 0


def maximize(node):
    if is_leaf(node):
        return node
    max_node = None
    max_score = -INFINITY

    for child in node.children:
        score = minimize(child).data
        if score > max_score:
            max_node = child
            max_score = score

    return max_node


def minimize(node):
    if is_leaf(node):
        return node
    min_node = None
    min_score = INFINITY

    for child in node.children:
        score = maximize(child).data
        if score < min_score:
            min_node = child
            min_score = score

    return min_node


def print_winner(max_score, min_score):
    print("MAX: ", max_score)
    print("MIN: ", min_score)
    if max_score > min_score:
        print("MAX WINS")
    elif min_score > max_score:
        print("MIN WINS")
    else:
        print("TIE")

def get_nums():
    # TODO add user input
    return [1, 2, 5, 2]


nums = get_nums()
root = make_tree(nums)
min_score = 0
max_score = 0
is_max_turn = True


while not is_leaf(root):
    if is_max_turn:
        turn = maximize(root)
        max_score = max_score + turn.data
        is_max_turn = False
        root = turn
    else:
        turn = minimize(root)
        min_score = min_score + turn.data
        is_max_turn = True
        root = turn

print_winner(min_score, max_score)
