from ctypes.wintypes import tagRECT
import WordSelection
# My origional attempts to solve the genetic algorithm all ended up with the guesses not making any progress
# This attempt at a successful version was implimented based on https://www.geeksforgeeks.org/genetic-algorithms/

# Gets the user's input for the purpose of setting the target word
def getInput():
    print("Enter a five letter string")
    userin:str = input().lower()
    if (len(userin) != 5):
        print("The string you entered was not five letters")
        userin = getInput()
    return userin      

# Runs a generation like this: !ORIGIONAL ATTEMPT!
# 1. Pop of 40*40 is broken into 40 pairs of parents and mated to create 40 children
# 2. Group of 40 children is culled to remove those with 0 fitness since they have no chance to progress the guess to target
# 3. Group of culled children are mated to produce a healthy group of 40
# 4. The healthy group is added to a new pop of 9 random groups
def cycleGeneration(pop):
    children = WordSelection.runGeneration(pop)
    children = WordSelection.cullWeak(children)
    children = WordSelection.repopulatePop(children)
    return WordSelection.generateGroupsFromPop(children)

# Get target and generate initial group
def initilizePop():
    WordSelection.target = getInput()
    return WordSelection.generateGroups()

#pop = initilizePop()
#children = WordSelection.runGeneration(pop)
#guess = ""
#attempt = 0
#while guess != WordSelection.target:
#    children = WordSelection.cullWeak(children)
#    children = WordSelection.repopulatePop(children)
#    print("Guess: ", WordSelection.competitionSelection(children))
#    print("attempt: ", attempt)
#    attempt += 1

# My origional attempts to solve the genetic algorithm all ended up with the guesses not making any progress
# This attempt at a successful version was implimented based on https://www.geeksforgeeks.org/genetic-algorithms/
population = 100

def main():
    global population
    
    attempts = 1
    
    found = False
    pop = []
    WordSelection.target = getInput()
    
    # Generate initial pop
    for _ in range(population):
        individual = WordSelection.initialGuess()
        pop.append(individual)
        
    while not found:
        
        # Cull unfit pop
        pop = WordSelection.cullWeakImproved(pop)

        # Repopulate Pop
        pop = WordSelection.repopulatePopImproved(pop)
        
        # Get fresh genome from new pop
        newPop = []
        for _ in range(population):
            newPop.append(WordSelection.initialGuess())
        pos = 0
        temp = []
        for x in pop:
            temp.append("".join(WordSelection.matingPairImproved(x, newPop[pos])))
            pos += 1
        pop = temp
    
        print("Generation: ", attempts)
        best = WordSelection.competitionSelectionImproved(pop)[0]
        print("Best: ", best)
        if best == WordSelection.target:
            found = True
            break
        if attempts == 5:
            print("Do you want to continue? y/n")
            if input() == 'n':
                break
        attempts += 1
    
        
if __name__ == '__main__':
    main()