import random
import sys
import time
import matplotlib.pyplot as plt

def generateArabicDigitString(length):
    arabicDigits = "0123456789"
    result = ""
    for _ in range(length):
        result += random.choice(arabicDigits)
    return result

def visualizeFrequencyDistribution(string):
    frequencyMap = {}
    for char in string:
        frequencyMap[char] = frequencyMap.get(char, 0) + 1
    print("Frequency Distribution:")
    for char, count in frequencyMap.items():
        print(char, ":", count)

def bruteForcePassword(password):
    attempt = ""
    count = 0
    start = time.perf_counter()
    while attempt != password:
        attempt = str(count).zfill(len(password))
        count += 1
    end = time.perf_counter()
    duration = end - start
    return duration

def calculateAverageBruteForceTime(length):
    totalTime = 0.0
    for _ in range(100):
        arabicDigitString = generateArabicDigitString(length)
        totalTime += bruteForcePassword(arabicDigitString)
    averageTime = totalTime / 100.0
    return averageTime

def plotAverageTime(length):
    lengths = range(1, length + 1)
    averageTimes = [calculateAverageBruteForceTime(length) for length in lengths]
    
    plt.plot(lengths, averageTimes, marker='o')
    plt.xlabel('Length')
    plt.ylabel('Average Time')
    plt.title('Average Time vs. Length')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == "-generate":
            password = generateArabicDigitString(int(sys.argv[2]))
            print(password)
            visualizeFrequencyDistribution(password)
        elif action == "-average":
            for length in range(1, int(sys.argv[2]) + 1):
                averageTime = calculateAverageBruteForceTime(length)
                print(f"Average time for length = {length}: {averageTime:.6f}")
        elif action == "-plot":
            plotAverageTime(int(sys.argv[2]))
        else:
            print("Invalid action")
    else:
        print("Please provide an action")