import os

srcPath = os.path.dirname(__file__)
textPath = os.path.join(srcPath, "alice.txt")

with open(textPath) as file:
    words = file.read().splitlines() # Get words from file

print(words[:10]) # Print out the first 10 words

letterPoints = {
    "a":  1,
    "b":  3,
    "c":  3,
    "d":  2,
    "e":  1,
    "f":  4,
    "g":  2,
    "h":  4,
    "i":  1,
    "j":  8,
    "k":  5,
    "l":  1,
    "m":  3,
    "n":  1,
    "o":  1,
    "p":  3,
    "q": 10,
    "r":  1,
    "s":  1,
    "t":  1,
    "u":  1,
    "v":  4,
    "w":  4,
    "x":  8,
    "y":  4,
    "z": 10,
}

bestScore = 0 # Keep track of the highest score
bestWord = None # Keep track of the highest scoring word

# Find the word with the highest Scrabble score

for word in words:
    score = 0

    # Loop through each letter in the current word
    for letter in word:
        score += letterPoints[letter]

    # Alternatively, we could use:
    # score = sum(letterPoints[letter] for letter in word)

    if score > bestScore:
        bestScore = score
        bestWord = word

print(bestWord)

# Challenge: for each letter of the alphabet, find the highest
# scoring word for that letter. Don't loop through the list of
# words more than once!

bestWords = {} # Keep track of the highest scoring word for each letter
bestScores = {} # Keep track of the scores for bestWords

# Find the word with the highest Scrabble score

for word in words:
    firstLetter = word[0]
    score = 0

    for letter in word:
        score += letterPoints[letter]

    if bestScores.get(firstLetter, 0) < score:
        bestWords[firstLetter] = word
        bestScores[firstLetter] = score

for letter in bestScores:
    print(letter, bestWords[letter], bestScores[letter])
