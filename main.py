# @authors: Christopher Chang, Danial Thai, Drew Finch

# Minimax Game:
# Two players (Max, Min) are given a list of numbers, e.g. [1,2,5,2]
# 1. The players take turn in picking a number from either the beginning or the end of the
# list.
# 2. Max starts first.
# 3. The game is over when there are no more numbers left in the list.
# 4. Winner: the player with more collected points
# 5. Min and Max both play optimally
INFINITY = 100000000000

import copy


class Node:
    def __init__(self, data, parent, utilScore=0):
        self.parent = parent
        self.children = []
        self.data = data
        self.utilScore = utilScore
        
class retNode:
    def __init__(self, data, parent, direction=None):
        self.parent = parent
        self.data = data
        self.dir = direction

def get_successors(tree):
    children = []
    return children

def isEmpty(numbers):
    return len(numbers) == 1


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
    # elif len(numbers) == 1:
    #     numbers_copy1 = numbers.copy()
    #     child1 = Node(numbers_copy1.pop(0), node)
    #     node.children.append(child1)


def is_leaf(node):
    return len(node.children) == 0

### The max and min functions cannot be called max or min because they are reserved functions!
def maximize(node):
    if is_leaf(node):
        node.utilScore = node.data
        return node
    max_node = None
    max_score = -INFINITY

    for child in node.children:
        score = minimize(child).utilScore
        if score > max_score:
            max_node = child
            max_score = score

    return max_node


def minimize(node):
    if is_leaf(node):
        node.utilScore = node.data
        return node
    min_node = None
    min_score = INFINITY

    for child in node.children:
        score = maximize(child).data
        child.utilScore = score
        if score < min_score:
            min_node = child
            min_score = score

    return min_node

#driver code that runs minimize and maximize
#@return (maxScore, minScore, pathTree)
def play(numbers):
    numCpy = copy.deepcopy(numbers)
    root = make_tree(numbers)
    maxScore = 0
    minScore = 0
    maxTurn = True
    
    currNode = None
    
    gameEnded = isEmpty(numbers)
    
    while (not gameEnded):
        root = maximize(root)
        maxChoice = root.data
        if (maxChoice == numCpy[0]):    #numbers is automatically decreased each choice, just worry about getting the ideal path from a given state of numbers
            currNode = retNode(numCpy.pop(0), currNode, "left")
        else:
            currNode = retNode(numCpy.pop(), currNode, "right")
        maxScore += maxChoice
        
        gameEnded = isEmpty(numCpy)
        maxTurn = False
        
        if (not gameEnded):
            root = minimize(root)
            minChoice = root.data
            if (minChoice == numCpy[0]):
                currNode = retNode(numCpy.pop(0), currNode, "left")
            else:
                currNode = retNode(numCpy.pop(), currNode, "right")
            minScore += minChoice
            maxTurn = True
            
            gameEnded = isEmpty(numCpy)
        
    if maxTurn:
        currNode = retNode(numCpy.pop(), currNode, "left")
        maxScore += currNode.data
    else:
        currNode = retNode(numCpy.pop(), currNode, "left")
        minScore += currNode.data
        
    return (maxScore, -minScore, currNode)

#determines who won
def checkWinner(maxScore, minScore):
    maxWon = False
    tie = False
    scoreSum = maxScore + minScore
    
    if (scoreSum > 0):
        maxWon = True
    elif (scoreSum == 0):
        tie = True
    
    return (maxWon, tie)

#Start Misc. Functions --------------------------------------------------------
def scanFile(file):
    data = file.read().replace(' ', '').split(",")
        
    numbers = list(map(int, data))
    
    return numbers

def scanInput(strIn):
    data = strIn.replace(' ', '').split(",")
    
    numbers = list(map(int, data))
    
    return numbers

def printPath(lastNode, numbers):
    numCpy = copy.deepcopy(numbers)
    path = []
    currNode = lastNode
    
    while (currNode.parent != None):
        path.append((currNode.data, currNode.dir))
        currNode = currNode.parent
        
    path.append((currNode.data, currNode.dir))
        
    path.reverse()
    
    maxScore = 0
    minScore = 0
    maxTurn = True
    
    print("Path:")
    print(numCpy)
    for e in path:    #With the way the ai works, we cannot get the proper pathing for the choices. This gives wrong results
        if (e[1] == "left"):
            if maxTurn:
                maxScore += numCpy.pop(0)
                maxTurn = False
            else:
                minScore -= numCpy.pop(0)
                maxTurn = True
        else:
            if maxTurn:
                maxScore += numCpy.pop()
                maxTurn = False
            else:
                minScore -= numCpy.pop()
                maxTurn = True
            
        print("{}\t\tMax = {} Min = {}".format(numCpy, maxScore, minScore))
        
def printScore(maxScore, minScore):
    print("MAX:\t{}".format(maxScore))
    print("MIN:\t{}".format(minScore))
        
#End Misc. Functions ----------------------------------------------------------


numbers = [1, 2, 5, 2]

##uncomment these lines of code to test different input
option = input("manuel or file input?\n")

if (option.lower() == "file"):
    print("Give a file path to a list of numbers\nThe numbers should be seperated with commas")
    filePath = input("File Path:\n")
    
    f = open(filePath, 'r')
    numbers = scanFile(f)
    f.close()
else:
    print("Give a list of numbers\nThe numbers should be seperated with commas")
    numbers = scanInput(input("List:\n"))
    
scores = play(numbers) #(max_score, min_score, path)

winState = checkWinner(scores[0], scores[1])

#printPath(scores[2], numbers)  #Gives wrong results

printScore(scores[0], scores[1])

if (winState[0]):
    print("The maximizer won")
elif (winState[1]):
    print("Tie!")
else:
    print("The maximizer lost")
