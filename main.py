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

class GameWithGraphics:
    def __init__(self):
        self.root = Tk()

    def __getWord(self, rightWord):
        self.rightWord = rightWord
        # print(self.rightWord)

    def __gameType(self, choicedGameType):
        if choicedGameType == 1 or choicedGameType == 2:
            word = WordsBase()
            self.rightWord = word.returnWord(choiceGameType=choicedGameType)
            # print(self.rightWord)
        elif choicedGameType == 3:
            self.title.destroy()
            self.button1.destroy()
            self.button2.destroy()
            self.button3.destroy()

            self.title = Label(self.root, text="DIGITE A PALAVRA PARA O SEU ADVERSÁRIO")
            self.field = Entry(self.root, width=50)
            self.confirm = Button(self.root, text="CONFIRMAR PALAVRA", state=NORMAL, command=lambda: self.__getWord(self.field.get().lower()))

            self.title.grid(row=0, column=1)
            self.field.grid(row=2, column=1)
            self.confirm.grid(row=3, column=1)

            self.root.mainloop()

    def selectGameType(self):
        "Jogador define o modo de jogo"
        self.title = Label(self.root, text="SELECIONE O TIPO DE JOGO:")
        self.button1 = Button(self.root, text="Normal(apenas palavras de 5 letras)", state=NORMAL, command=lambda: self.__gameType(1))
        self.button2 = Button(self.root, text="Hardcore(palavras de todos os tamanhos)", state=NORMAL, command=lambda: self.__gameType(2))
        self.button3 = Button(self.root, text="Versus", state=NORMAL, command=lambda: self.__gameType(3))
        
        self.title.grid(row=0, column=1)
        self.button1.grid(row=3, column=1)
        self.button2.grid(row=3, column=3)
        self.button3.grid(row=3, column=5)

        self.root.mainloop()

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

if __name__ == '__main__':
    game = GameWithGraphics()
    game.selectGameType()
    game.startGame()
