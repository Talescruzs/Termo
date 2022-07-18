from createdFunctions.wordsGenerator import WordsBase
from createdFunctions.comparator import CompareWord
from tkinter import *

class Game:
    "Ponto inicial do jogo"
    def __init__(self):
        pass

    def selectGameType(self):
        "Jogador define o modo de jogo"
        a = True
        while a:
            choicedGameType = int(input(
                "Tipos: \n1=Normal(apenas palavras de 5 letras) \n2=Hardcore(palavras de todos os tamanhos)" 
                "\n3=Versus\nDigite qual modo queres: "
                ))
            if choicedGameType == 1 or choicedGameType == 2:
                word = WordsBase()
                self.rightWord = word.returnWord(choiceGameType=choicedGameType)
                break
            elif choicedGameType == 3:
                self.rightWord = input("digita a palavra para o seu adversário: ").lower()
                break
            else:
                print("OOOO CABEÇA DE CAVALO...\n")

    def startGame(self):
        "Insere palavra do jogador e retorna se está certa ou não"
        result = False
        compare = CompareWord()
        while (result == False):
            inputText = str()
            while (len(inputText) != len(self.rightWord)):
                inputText = input("digita uma palavra com %d letras: " % len(self.rightWord)).lower()
                if len(inputText) != len(self.rightWord):
                    print("OOOO CABEÇA DE CAVALO...são %d letras" %len(self.rightWord))
            compare.income(inputText=inputText, rightText=self.rightWord)
            result = compare.outcome()
            final = compare.overview()
            if result:
                print("ACERTOU")
            else:
                print("Errou:")
                for letter in range(len(final)):
                    # if self.final[letter] != "Letra errada":      PODE SER USADO CASO QUEIRA MOSTRAR APENAS AS LETRAS QUE ESTÃO NA PALAVRA, EU ACHO MAIS CONFUSO
                        # print("%s : %s" %(self.inputText[letter], self.final[letter]))
                    print("%s : %s" %(inputText[letter], final[letter])) 
            final = compare.cleanFinal()



if __name__ == '__main__':
    game = Game()
    game.selectGameType()
    game.startGame()
