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
    def __init__(self, data, parent):
        self.parent = parent
        self.data = data

def get_successors(tree):
    children = []
    return children

def isEmpty(numbers):
    return len(numbers) == 0

### The max and min functions cannot be called max or min because they are reserved functions!
def maximize(numbers):
    v = -INFINITY

    # for each successor of state:
    #     v = max(v, min - value(successor))
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
        v = max_num
    return v


def minimize(numbers):
    v = INFINITY
    min_num = numbers[-1]
    for i in numbers:
        if i < min_num:
            min_num = i
        v = min_num
    return v

#driver code that runs minimize and maximize
def play(numbers):
    numCpy = copy.deepcopy(numbers)
    maxScore = 0
    minScore = 0
    
    currNode = None
    
    gameEnded = isEmpty(numbers)
    
    while (not gameEnded):
        maxChoice = maximize(numCpy)            #asserts that that maximize will return the choice branch that will make max win
        if (maxChoice == numCpy[0]):    #numbers is automatically decreased each choice, just worry about getting the ideal path from a given state of numbers
            currNode = Node(numCpy.pop(0), currNode)
        else:
            currNode = Node(numCpy.pop(), currNode)
        maxScore += maxChoice
        
        gameEnded = isEmpty(numCpy)
        
        if (not gameEnded):
            minChoice = minimize(numCpy)        #asserts that minimize will return the choice branch that will make max lose
            if (minChoice == numCpy[0]):
                currNode = Node(numCpy.pop(0), currNode)
            else:
                currNode = Node(numCpy.pop(), currNode)
            minScore += minChoice
            
        gameEnded = isEmpty(numCpy)
        
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
        path.append(currNode.data)
        currNode = currNode.parent
        
    path.append(currNode.data)
        
    path.reverse()
    
    print("Path:")
    for e in path:
        if (e == numCpy[0]):
            numCpy.pop(0)
        else:
            numCpy.pop()
            
        print(numCpy)
        
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
    
scores = play(numbers) #(max_score, min_score)

winState = checkWinner(scores[0], scores[1])

printPath(scores[2], numbers)

if (winState[0]):
    print("The maximizer won")
elif (winState[1]):
    print("Tie!")
else:
    print("The maximizer lost")
