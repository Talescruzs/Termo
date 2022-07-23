from createdFunctions.wordsGenerator import WordsBase
from createdFunctions.comparator import CompareWord
from tkinter import *

class GameWithGraphics:
    def __init__(self):
        self.rightWord = str()

    def __again(self):
        self.root.destroy()
        self.selectGameType()
    
    def __congratulations(self):
        self.root = Tk()
        self.root.title("Acertou")   
        self.root.resizable(False, False)
        self.root.state("zoomed")    
        title = Label(self.root, text="ACERTOUU NA RODADA %d" %self.counter, font="Arial 30 bold", fg="green")
        confirm = Button(self.root, text="JOGAR NOVAMENTE", font="Arial 15 bold", state=NORMAL, command=lambda: self.__again())
        title.place(relx=0.5, rely=0.25, anchor=CENTER)
        confirm.place(relx=0.5, rely=0.50, anchor=CENTER)
        self.root.mainloop()

    def __gameOver(self):
        self.root = Tk()
        self.root.title("Game Over")   
        self.root.resizable(False, False)
        self.root.state("zoomed")    
        title = Label(self.root, text="GAME OVER", font="Arial 30 bold", fg="red")
        confirm = Button(self.root, text="JOGAR NOVAMENTE", font="Arial 15 bold", state=NORMAL, command=lambda: self.__again())
        title.place(relx=0.5, rely=0.25, anchor=CENTER)
        confirm.place(relx=0.5, rely=0.50, anchor=CENTER)
        self.root.mainloop()

    def __gameOverview(self, result):
        letter = str()
        for a in range(len(self.inputText)):
            if result[a] == "Posição certa":
                letter = Label(
                    self.frame, text=self.inputText[a], bg="green", padx=10, 
                    )
            elif result[a] == "Posição errada":
                letter = Label(
                    self.frame, text=self.inputText[a], bg="blue", padx=10
                    )
            else:
                letter = Label(
                    self.frame, text=self.inputText[a], bg="white", padx=10
                    )
            letter.grid(row=(self.counter+4), column=a) #usar frame
        self.counter+=1



    def __getWord(self, word):
        self.inputText = word
        self.field.delete(0, END)
        if len(self.inputText) != len(self.rightWord):
            cavalo = Label(self.root, text="OOOOO CAVALO, SÃO %d LETRAS"%len(self.rightWord), font="Arial 15", fg="red") 
            cavalo.place(relx=0.5, rely=0.05, anchor=CENTER)
        else:
            compare = CompareWord()
            compare.income(inputText=self.inputText, rightText=self.rightWord)
            result = compare.outcome()
            if result:
                self.root.destroy()
                self.__congratulations()
            else:
                if self.counter >= 5:
                    self.root.destroy()
                    self.__gameOver()
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
            self.root.resizable(False, False)
            self.root.state("zoomed")      
            title = Label(self.root, text="DIGITE A PALAVRA PARA O SEU ADVERSÁRIO", font="Arial 24 bold")
            field = Entry(self.root, font="Arial 15 bold", width=50)
            confirm = Button(self.root, text="CONFIRMAR PALAVRA", font="Arial 15 bold", state=NORMAL, command=lambda: self.__getRightWord(field.get().lower()))

            title.place(relx=0.5, rely=0.15, anchor=CENTER)
            field.place(relx=0.5, rely=0.25, anchor=CENTER)
            confirm.place(relx=0.5, rely=0.35, anchor=CENTER)
            self.root.mainloop()

        self.startGame()

    def selectGameType(self):
        "Jogador define o modo de jogo"
        self.root = Tk()
        self.root.title("Seleção de tipo de jogo")
        self.root.resizable(False, False)
        self.root.state("zoomed")

        title = Label(self.root, text="SELECIONE O TIPO DE JOGO:", font="Arial 24 bold")
        button1 = Button(self.root, text="Normal(apenas palavras de 5 letras)", font="Arial 15 bold", state=NORMAL, command=lambda: self.__gameType(1))
        button2 = Button(self.root, text="Hardcore(palavras de todos os tamanhos)", font="Arial 15 bold", state=NORMAL, command=lambda: self.__gameType(2))
        button3 = Button(self.root, text="Versus", font="Arial 15 bold", state=NORMAL, command=lambda: self.__gameType(3))
        
        title.place(relx=0.5, rely=0.15, anchor=CENTER)
        button1.place(relx=0.5, rely=0.25, anchor=CENTER)
        button2.place(relx=0.5, rely=0.35, anchor=CENTER)
        button3.place(relx=0.5, rely=0.45, anchor=CENTER)
        self.root.mainloop()

    def startGame(self):
        "Insere palavra do jogador e retorna se está certa ou não"
        self.root = Tk()
        self.root.title("Termo")
        self.root.resizable(False, False)
        self.root.state("zoomed")
        self.frame = Frame(self.root, width=50)
        self.counter = 1

        title = Label(self.root, text="DIGITE A PALAVRA COM %d LETRAS" %len(self.rightWord), font="Arial 24 bold")
        self.field = Entry(self.root, width=50, font="Arial 15 bold")
        confirmWord = Button(self.root, text="CONFIRMAR PALAVRA", state=NORMAL, font="Arial 15 bold", command=lambda: self.__getWord(self.field.get().lower()))

        title.place(relx=0.5, rely=0.15, anchor=CENTER)
        self.field.place(relx=0.5, rely=0.25, anchor=CENTER)
        confirmWord.place(relx=0.5, rely=0.55, anchor=CENTER)
        self.frame.place(relx=0.5, rely=0.40, anchor=CENTER)

        self.root.mainloop()

if __name__ == '__main__':
    game = GameWithGraphics()
    game.selectGameType()
