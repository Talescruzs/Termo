from sympy import root
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
        self.rightWord = str()
    
    def __congratulations(self):
        self.root = Tk()
        self.root.title("Acertou")      
        title = Label(self.root, text="ACERTOUU NA RODADA %d" %self.counter)
        title.grid(row=1, column=1)
        self.root.mainloop()

    def __gameOverview(self, result):
        letter = str()
        for a in range(len(self.inputText)):
            if result[a] == "Posição certa":
                letter = Label(
                    self.root, text=self.inputText[a], bg="green", padx=10
                    )
            elif result[a] == "Posição errada":
                letter = Label(
                    self.root, text=self.inputText[a], bg="blue", padx=10
                    )
            else:
                letter = Label(
                    self.root, text=self.inputText[a], bg="white", padx=10
                    )
            letter.grid(row=(self.counter+4), column=a)
        self.counter+=1



    def __getWord(self, word):
        self.inputText = word
        self.field.delete(0, END)
        if len(self.inputText) != len(self.rightWord):
            cavalo = Label(self.root, text="OOOOO CAVALO, SÃO %d LETRAS"%len(self.rightWord)) 
            cavalo.grid(row=1, column=0, columnspan=len(self.rightWord))
        else:
            compare = CompareWord()
            compare.income(inputText=self.inputText, rightText=self.rightWord)
            result = compare.outcome()
            if result:
                self.root.destroy()
                self.__congratulations()
            else:
                if self.counter >= 5:
                    pass
                else:
                    overview = compare.overview()
                    self.__gameOverview(overview)
                    compare.cleanFinal()
        



    def __getRightWord(self, rightWord):
        self.rightWord = rightWord
        self.root.destroy()

    def __gameType(self, choicedGameType):
        self.root.destroy()
        if choicedGameType == 1 or choicedGameType == 2:
            word = WordsBase()
            self.rightWord = word.returnWord(choiceGameType=choicedGameType)

        elif choicedGameType == 3:
            self.root = Tk()
            self.root.title("Seleção de palavra para  modo versus")      
            title = Label(self.root, text="DIGITE A PALAVRA PARA O SEU ADVERSÁRIO")
            field = Entry(self.root, width=50)
            confirm = Button(self.root, text="CONFIRMAR PALAVRA", state=NORMAL, command=lambda: self.__getRightWord(field.get().lower()))

            title.grid(row=0, column=1)
            field.grid(row=2, column=1)
            confirm.grid(row=3, column=1)
            self.root.mainloop()

        self.startGame()

    def selectGameType(self):
        "Jogador define o modo de jogo"
        self.root = Tk()
        self.root.title("Seleção de tipo de jogo")
        title = Label(self.root, text="SELECIONE O TIPO DE JOGO:")
        button1 = Button(self.root, text="Normal(apenas palavras de 5 letras)", state=NORMAL, command=lambda: self.__gameType(1))
        button2 = Button(self.root, text="Hardcore(palavras de todos os tamanhos)", state=NORMAL, command=lambda: self.__gameType(2))
        button3 = Button(self.root, text="Versus", state=NORMAL, command=lambda: self.__gameType(3))
        
        title.grid(row=0, column=1)
        button1.grid(row=3, column=1)
        button2.grid(row=3, column=3)
        button3.grid(row=3, column=5)

        self.root.mainloop()

    def startGame(self):
        "Insere palavra do jogador e retorna se está certa ou não"
        self.root = Tk()
        self.root.title("Termo")
        self.counter = 1

        title = Label(self.root, text="DIGITE A PALAVRA COM %d LETRAS" %len(self.rightWord))
        self.field = Entry(self.root, width=50)
        confirmWord = Button(self.root, text="CONFIRMAR PALAVRA", state=NORMAL, command=lambda: self.__getWord(self.field.get().lower()))

        title.grid(row=2, column=0, columnspan=len(self.rightWord))
        self.field.grid(row=4, column=0, columnspan=len(self.rightWord))
        confirmWord.grid(row=9, column=0, columnspan=len(self.rightWord))

        self.root.mainloop()

if __name__ == '__main__':
    game = GameWithGraphics()
    game.selectGameType()
