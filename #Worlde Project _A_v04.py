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

#user input function
def userWord (wordBank):
    while True:
        guess = input("input a 5 - letter word: ").strip().lower()
        if(len(guess)!= 5):
            #! = means not equal
            print("word must be exactly 5 - letters long.")
        elif(guess not in wordBank):
            print("Please submit a real correctly spelled word.")
        else:
            return(guess)
                 


def main():
    print("Wordle Test Project")
    words = loadWordBank(wordFile)
    #Change 2: Needs a way to call a random sample
    sample = random.choice(words)
    print(f"Debugging test: Selected word is {sample}")
    attempts = 0
    while attempts < 6:
        guess = userWord(words)
        print(f"Your guess: {guess}")
        attempts += 1
    #(f"Comparing {guess} to {sample}")
        if sample == guess:
         print("Congrats you got it!!!!!!")
        else:
            print(f"The word you selected was incorrect, try again you are on attempt {attempts}")
if __name__ == "__main__":
    main()