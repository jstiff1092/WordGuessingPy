import WordSelection

def getInput():
    print("Enter a five letter string")
    userin:str = input().lower
    if (len(userin) != 5):
        print("The string you entered was not five letters")
        getInput()
    return userin            
    
print(WordSelection.fitnessCheck('ttttt', 'ttttt'))