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
def userGuess (wordBank):
    while True:
        guess = input("input a 5 - letter word: ").strip().lower()
        if(len(guess)!= 5):
            #! = means not equal
            print("word must be exactly 5 - letters long.")
        elif(guess not in wordBank):
            print("Please submit a real correctly spelled word.")
        else:
            return(guess)
                 
def scoreGuess(guess: str, target: str):

    # result codes: "G"=greeen, "Y"=yelow, "B"=black,gray
    result = ["B"] * 5
    targetChars = list(target)
    
    #correct = green
    for i in range(5):
        result[i] = "G"
        targetChars[1] = None #Use up that letter
        #pass 2: yellows (handles duplicates correctly)
        for i in range(5):
            if result[i] == "B" and guess[i] in targetChars:
                result[i] = "Y"
                targetChars[targetChars.index(guess[i])] = None
            return result


def emojiFeedback(score):
    emojiMap = {"G": "🟩", "Y": "🟨", "B": "⬛️"}
    return "".join(emojiMap[s] for s in score)

    
def main():
    print("Wordle Test Project")
    words = loadWordBank(wordFile)
    #Change 2: Needs a way to call a random sample
    target = random.choice(words)
    
    board = []
    
    for attempt in range(1,7):
        guess = userGuess(words)
        score = scoreGuess(guess, target)
        
        board.append(emojiFeedback(score))
        
        
        print("/nCurrent Board:")
        for row in board:
            print(row)
            
            if guess == target:
                print(f"/nYou got it in {attempt} guesses!")
                return
if __name__ == "__main__":
    main()
