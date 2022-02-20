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
for i in pop:
    children.append(WordSelection.competitionSelection(i))
while 'pizza' not in children:
    WordSelection.cullWeak(children)
    WordSelection.repopulatePop(children)
    print(WordSelection.competitionSelection(children))
    print("Attempts: ", attempts)
    attempts += 1
