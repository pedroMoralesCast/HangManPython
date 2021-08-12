# from random import seed
# from random import random
import random
# seed random number generator

def getWord():
    wordsList=[]
    with open ("./Archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            wordsList.append(line.replace("\n",""))    
    wordRandom= random.choice(wordsList)
    wordRandom=list(wordRandom)
    return wordRandom

    
def inGame(word):
    lettersInGame=[]
    lettersInGame='_'* len(word)
    lettersInGame=list(lettersInGame)
    for i in range(0,6):
        answ=input("Introduce una Letra: ")
        for n in range(len(word)):
            if answ == word[n]:
                lettersInGame[n]=word[n]
        wordComp=" ".join(lettersInGame)
        print(wordComp)
    print("EndGame")

def run():
    word=getWord()
    print(word)
    inGame(word)



if __name__ == '__main__':
    run()