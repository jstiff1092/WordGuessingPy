from operator import contains
import WordSelection

def getInput():
    print("Enter a five letter string")
    userin:str = input().lower()
    if (len(userin) != 5):
        print("The string you entered was not five letters")
        userin = getInput()
    return userin            

WordSelection.target = 'pizza'
pop = WordSelection.generateGroups()
children = []
attempts = 0

while 'pizza' not in children:
    pop = WordSelection.generateGroups()
    for i in pop:
        parents = WordSelection.competitionSelection(i)
        children.append(WordSelection.matingPairs(parents[0], parents[1]))
        children = WordSelection.cullWeak(children)
        children = WordSelection.repopulatePop(children)
    print("Guess: ", WordSelection.competitionSelection(children)[0])
    print("Attempts: ", attempts)
    attempts += 1
    
# TODO have the repopulated pop of 40 compete with 39 other groups of new pops
