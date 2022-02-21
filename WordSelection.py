import random
# A list of English letters as well as the arrays to
# store words that are in the word or not
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
              'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
              'v', 'w', 'x', 'y', 'z']
target = ""
included = []
excluded = []
fitness = 0

# Function determines the value of a guess where 10 points are given for a letter
# existing in a word and an additional 10 points for the letter in the correct place
def fitnessCheck(aiword):
    fitness:int = 0
    indexpos = 0
    for letter in aiword:
        if (letter not in target and letter not in excluded):
            excluded.append(letter)
        if letter in target:
            if letter in included and letter == target[indexpos]:
                fitness += 20
            if letter not in included:
                fitness += 10
                included.append(letter)
                if letter == target[indexpos]:
                    fitness += 10
        indexpos += 1
    return fitness

# When adding a random letter the ratio of vowels to consonants will be 30/70
def randomLetter():
    if random.randrange(0, 10) <= 3:
        return vowels[random.randrange(0,4)]
    else:
        return consonants[random.randrange(0, 20)]
    
# Initial guess is random, THIS IS THE RANDOM WORD GENERATION
def initialGuess():
    out = ""
    for i in range(5):
        out += randomLetter()
    return out

# 40 groups of 40 will compete to be the guess
def generateGroups():
    battleRoyale = []
    for i in range(40):
        group = []
        for x in range(40):
            group.append(initialGuess())
        battleRoyale.append(group)
    return battleRoyale

def generateGroupsFromPop(inputPop):
    battleRoyale = [inputPop]
    for i in range(9):
        group = []
        for x in range(40):
            group.append(initialGuess())
        battleRoyale.append(group)
    return battleRoyale

# Takes the initial pop of 40*40 and breaks it into 40 pairs of parents, then mates the parents to create 40 children
def runGeneration(inputPopArray):
    children = []
    for x in inputPopArray:
        children.append(competitionSelection((x)))
    return children

# Takes in an array of words and selects the most fit parents and produces a child
def competitionSelection(inputPop):
    mother = "abcde"
    father = "fghij"
    for x in inputPop:
        if fitnessCheck(x) > fitnessCheck(mother):
            father = mother
            mother = x
        if fitnessCheck(x) == fitnessCheck(mother):
            if random.random() >= 0.50:
                father = mother
                mother = x
    return matingPairs(mother, father)

# Improved to use the new improved functions
def competitionSelectionImproved(inputPop):
    mother = "abcde"
    father = "fghij"
    for x in inputPop:
        if fitnessCheck(x) > fitnessCheck(mother):
            father = mother
            mother = x
        if fitnessCheck(x) == fitnessCheck(mother):
            if random.random() >= 0.50:
                father = mother
                mother = x
    return (mother, father)

# Function to remove guesses with fitness <= 20
def cullWeak(inputPop):
    newPop = []
    for x in inputPop:
        if fitnessCheck(x) <= 20:
            newPop.append(x)
    return newPop

# Version of cull that uses improved method
def cullWeakImproved(inputPop):
    newPop = []
    for x in inputPop:
        if fitnessCheckImproved(x) < 5:
            newPop.append(x)
    return newPop

# Mates a pair and gives the child the opportunity to mutate
# Mother gives first 2 letters father gives 3rd and 4th
# 5th letter is coinflipped between the two
def matingPairs(mother, father) -> str:
    MUTATION_RATE = 0.015
    #mother = parentsPair[0]
    #father = parentsPair[1]
    child = mother[:2] + father[2:-1]
    if random.random() >= 0.50:
        child += mother[-1:]
    else:
        child += father[-1:]
    pos = 0
    for x in child:
        if random.random() <= MUTATION_RATE:
            temp = child[:pos] + randomLetter() + child[pos+1:]
            child = temp
        pos += 1
    return child


# Improved version of above method referenced from https://www.geeksforgeeks.org/genetic-algorithms/
def matingPairImproved(mother, father):
    child = list()
    for i in range(0, 5):
        ran = random.random()
        if ran < 0.45:
           child.append(mother[i])
        elif ran < 0.90:
           child.append(father[i])
        else:
            child.append(randomLetter())
    return child

# Improved method referenced from https://www.geeksforgeeks.org/genetic-algorithms/
def fitnessCheckImproved(aiword):
    global target
    fitness = 0
    for gs, gt in zip(aiword, target):
        if gs != gt: fitness += 1
    return fitness

# Repopulates a culled population to 40 by mating the remaining pairs randomly
# Regenerates an empty list or single parent list to have 2 parents
def repopulatePop(inputPop):
    if not inputPop:
        inputPop.append(initialGuess())
        inputPop.append(initialGuess())
    if len(inputPop) == 1:
        inputPop.append(initialGuess())
    tempPop = inputPop
    while(len(tempPop) < 40):
        #parents = (tempPop[random.randrange(0, len(tempPop))], tempPop[random.randrange(0, len(tempPop))])
        tempPop.append(matingPairs(tempPop[random.randrange(0, len(tempPop))], tempPop[random.randrange(0, len(tempPop))]))
    return tempPop

# Improved based on new matingpair method and parent selection based on https://www.geeksforgeeks.org/genetic-algorithms/
def repopulatePopImproved(inputPop):
    if not inputPop:
        inputPop.append(initialGuess())
        inputPop.append(initialGuess())
    if len(inputPop) == 1:
        inputPop.append(initialGuess())
    tempPop = inputPop
    while(len(tempPop) < 100):
        parent1 = tempPop[random.randrange(0, len(tempPop))]
        parent2 = tempPop[random.randrange(0, len(tempPop))]
        child = "".join(matingPairImproved(parent1, parent2))
        tempPop.append(child)
    return tempPop