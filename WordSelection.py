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
    
# Initial guess is random
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
    for i in range(39):
        group = []
        for x in range(39):
            group.append(initialGuess())
        battleRoyale.append(group)
    return battleRoyale

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
    return [mother, father]

# Function to remove guesses with fitness <= 20
def cullWeak(inputPop):
    newPop = []
    for x in inputPop:
        if fitnessCheck(x) > 20:
            newPop.append(x)
    return newPop

# Mates a pair and gives the child the opportunity to mutate
# Mother gives first 2 letters father gives 3rd and 4th
# 5th letter is coinflipped between the two
def matingPairs(mother, father):
    MUTATION_RATE = 0.015
    child = mother[:2] + father[2:-1]
    if random.random() >= 0.50:
        child += mother[-1:]
    else:
        child += father[-1:]
    pos = 0
    for x in child:
        if random.random() <= MUTATION_RATE:
            child = child[:pos] + randomLetter() + child[pos+1:]
        pos += 1
    
    return child

# Repopulates a culled population to 40 by mating the remaining pairs randomly
def repopulatePop(inputPop):
    tempPop = inputPop
    while(len(tempPop) < 40):
        tempPop.append(matingPairs(tempPop[random.randrange(0, len(tempPop))], tempPop[random.randrange(0, len(tempPop))]))
    return tempPop