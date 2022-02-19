import numpy

# A list of English letters as well as the arrays to
# store words that are in the word or not
vowels:str = ['a', 'e', 'i', 'o', 'u']
consonants:str = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
              'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
              'v', 'w', 'x', 'y', 'z']
included = []
excluded = []

def getInput():
    print("Enter a five letter string")
    userin:str = input().lower
    if (len(userin) != 5):
        print("The string you entered was not five letters")
        getInput()
    return userin

# Function determines the value of a guess where 10 points are given for a letter
# existing in a word and an additional 10 points for the letter in the correct place
def fitnessCheck(userword:str, aiword:str):
    fitness:int = 0
    indexpos = 0
    for letter in aiword:
        if (letter not in userword and letter not in excluded):
            excluded.append(letter)
        if letter in userword:
            if letter in included and letter == userword[indexpos]:
                fitness += 20
            if letter not in included:
                fitness += 10
                included.append(letter)
                if letter == userword[indexpos]:
                    fitness += 10
        indexpos += 1
    return fitness
            
    
print(fitnessCheck('ttttt', 'ttttt'))