import random
import WordSelection

def getInput():
    print("Enter a five letter string")
    userin:str = input().lower()
    if (len(userin) != 5):
        print("The string you entered was not five letters")
        userin = getInput()
    return userin            

WordSelection.target = 'trunk'
pop = WordSelection.generateGroups()
children = []
for i in pop:
    children.append(WordSelection.competitionSelection(i))
secondgen = WordSelection.competitionSelection(children)
print("Best second gen child is: ", secondgen, " with fitness of: ", WordSelection.fitnessCheck(secondgen))