import random
import sys
import time
import matplotlib.pyplot as plt

def cypher(text, m, n):
    text = text.replace(" ", "")
    textLength = len(text)
    cypheredText = ""
    blockNumber = 0
    while textLength > 0:
        amountToAdd = m * n - textLength
        for _ in range(amountToAdd):
            random_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
            text = text + random_letter
        for i in range(m):
            for j in range(n):
                cypheredText = cypheredText + text[j*m+i+m*n*blockNumber]
        textLength = textLength - m * n
        blockNumber += 1
    return cypheredText

def cypherWithCode(text, m, n, code):
    text = text.replace(" ", "")
    cypherPartList = [None] * m
    textLength = len(text)
    while textLength > 0:
        amountToAdd = m * n - textLength
        for _ in range(amountToAdd):
            random_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
            text = text + random_letter
        for i in range(m):
            cypheredPart = ""
            for j in range(n):
                cypheredPart = cypheredPart + text[j*m+i]
            ic = code.index(str(i+1))
            cypherPartList[ic] = cypheredPart
        textLength = textLength - m * n

    cypheredText = ''.join(cypherPartList)
    return cypheredText
    
def decypher(text, m, n):
    textLength = len(text)
    decypheredText = ""
    blockNumber = 0
    while textLength > 0:
        for i in range(n):
            for j in range(m):
                decypheredText = decypheredText + text[j*n+i+m*n*blockNumber]
        textLength = textLength - m * n
        blockNumber += 1
    return decypheredText

def decypherWithCode(text, m, n, code):
    textLength = len(text)
    decypheredText = ""
    while textLength > 0:
        for i in range(n):
            for j in range(m):
                jc = code.index(str(j+1))
                decypheredText = decypheredText + text[jc*n+i]
        textLength = textLength - m * n
    return decypheredText

def findDividerCombinations(number):
    dividerCombinations = []
    for i in range(1, number + 1):
        if number % i == 0:
            for j in range(1, number + 1):
                if number % (i * j) == 0:
                    dividerCombinations.append((i, j))
    return dividerCombinations

def attackCypher(cypheredText, neededResult):
    length = len(cypheredText)
    dividerCombinations = findDividerCombinations(length)
    attemptCount = 1
    for dividerCombination in dividerCombinations:
        print(dividerCombination, attemptCount)
        decypheredPasswordAttempt = decypher(cypheredText, dividerCombination[0], dividerCombination[1])
        print(decypheredPasswordAttempt)
        if decypheredPasswordAttempt.startswith(neededResult):
            return decypheredPasswordAttempt
        attemptCount += 1
    return "Could not decypher the text."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == "-cypher":
            cypheredPassword = cypher(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
            print(cypheredPassword)
        elif action == "-decypher":
            decypheredPassword = decypher(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
            print(decypheredPassword)
        elif action == "-cypherCode":
            decypheredPassword = cypherWithCode(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
            print(decypheredPassword)
        elif action == "-decypherCode":
            decypheredPassword = decypherWithCode(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
            print(decypheredPassword)
        elif action == "-attack":
            attackCypher(sys.argv[2], sys.argv[3])
        else:
            print("Invalid action")
    else:
        print("Please provide an action")