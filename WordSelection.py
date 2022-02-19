import random
# A list of English letters as well as the arrays to
# store words that are in the word or not
vowels:str = ['a', 'e', 'i', 'o', 'u']
consonants:str = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
              'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
              'v', 'w', 'x', 'y', 'z']
included = []
excluded = []
fitness = 0

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

# When adding a random letter the ratio of vowels to consonants will be 30/70
def randomLetter():
    if random.randrange(0, 10) <= 3:
        return vowels[random.randrange(0,4)]
    else:
        return consonants[random.randrange(0, 20)]