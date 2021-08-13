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

def wellcome():
    os.system("cls")
    print("""
    ||==========================================================================================||
    ||                               _   _                      ___  ___                        ||
    ||                              | | | |                     |  \/  |                        ||
    ||                              | |_| |  __ _  _ __    __ _ | .  . |  __ _  _ __            ||
    ||   Bienvenido al              |  _  | / _` || '_ \  / _` || |\/| | / _` || '_ \           ||
    ||       juego:                 | | | || (_| || | | || (_| || |  | || (_| || | | |          ||
    ||                              \_| |_/ \__,_||_| |_| \__, |\_|  |_/ \__,_||_| |_|          ||
    ||                                                     __/ |                                ||
    ||                                                    |___/                                 ||
    ||==========================================================================================||

    Se seleccionará una palabra al azar y tienes que adivinarla. Usa solo minusculas.
    """)


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
    wellcome()
    if input("Estas listo para jugar? (y/n)") == 'y':
        word=getWord()
        # print(word)
        inGame(word)
    else :
        os.system("cls")

if __name__ == '__main__':
    run()