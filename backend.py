#import os and binary search
import os 
import bisect

#stores placed words to check validity of suggested word
placedWords = []


#get list of sorted dictionary words and return 
def getSortedWords():
    with open ("words.txt","r",encoding = "utf-8") as file:
        return [line.strip() for line in file]


#function for user to suggest word to place
def suggestWord():
   suggestedWord = str(input("Place word: ")).lower()
   if checkValid(suggestedWord) == True: 
        if checkWord(suggestedWord) == True:
           addWord(suggestedWord)
        else:
            print("not a valid word")
   else:
       print("does not match any letters on placed word")


#firstly checks if suggested word matches any letter in last placed word on grid     
def checkValid(sW):
    if sW[0] in placedWords[-1]: return(True)
    

#secondly checks if suggested word is a valid word in the dictionary, returning true 
def checkWord(target):
    try:
        index = bisect.bisect_left(wordList, target)
        return index < len(wordList) and wordList[index] == target
    except:
        print("Error checking word in dictionary")
        return False


#adds word to placed words array 
def addWord(word):
    placedWords.append(word)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Word placed, last placed word is : {word}")

wordList = getSortedWords()

firstWord = str(input("input first word: "))
placedWords.append(firstWord)

while True:
    suggestWord()

