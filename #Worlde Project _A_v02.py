#Worlde Project _A_v01

from pathlib import Path
#change 1, something must be changed
import random
wordFile = Path ("words.txt")


def findWordFile():
     if wordFile.exists():
        return wordFile
     else:
         print("We couldn't find it")
   
#using reference doc approach
def loadWordBank(filename = "words.txt"):
     with open(filename, "r") as file:
        return[line.strip().lower() for line in file if len(line.strip()) == 5]
    
wordBank = loadWordBank()

def main():
    print("Wordle Test Project")
    words = loadWordBank(wordFile)
    #Change 2: Needs a way to call a random sample
    sample = random.choice(words)
    print(f"First sample test: {sample}")
if __name__ == "__main__":
    main()