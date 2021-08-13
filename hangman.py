# from random import seed
# from random import random
import random
import os
# seed random number generator

def getWord():
    wordsList=[]
    with open ("./Archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            wordsList.append(line.replace("\n",""))    
    wordRandom= random.choice(wordsList)
    wordRandom=list(wordRandom)
    return wordRandom

# def wellcome():
#     print("Bienvenido a HangMan")

def inGame(word):
    lettersInGame=[]
    lettersInGame='_'* len(word)
    lettersInGame=list(lettersInGame)
    for i in range(0,6):
        os.system("cls")
        wordComp=" ".join(lettersInGame)
        print(wordComp)
        answ=list(input("Introduce una Letra: "))
        for letr in range(len(answ)):
            for n in range(len(word)):
                if answ[letr] == word[n]:
                    lettersInGame[n]=word[n]
        if lettersInGame == word :
            os.system("cls")
            print("Has ganado!")
            break
    word="".join(word)
    print("La palabra era: ", word)
    print("EndGame")

def run():
    word=getWord()
    # print(word)
    inGame(word)



if __name__ == '__main__':
    run()