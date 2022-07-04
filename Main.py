from wordsGenerator import WordsBase
from comparator import CompareWord

class StartGame:
    "Ponto inicial do jogo"
    def __init__(self):
        pass

    def selectGameType(self):
        "Jogador define o modo de jogo"
        a = True
        while a:
            choiceGameType = int(input("Tipos: \n1=Normal \n2=Versus\nDigite qual modo queres: "))
            if choiceGameType == 1:
                word = WordsBase()
                self.rightWord = word.returnWord()
                break
            elif choiceGameType == 2:
                self.rightWord = input("digita a palavra para o seu adversário: ")
                break
            else:
                print("OOOO CABEÇA DE CAVALO...\n")
    def startGame(self):
        "Insere palavra do jogador e retorna se está certa ou não"
        result = False
        while (result == False):
            inputText = str()
            while (len(inputText) != len(self.rightWord)):
                inputText = input("digita uma palavra com %d letras: " % len(self.rightWord))
                if len(inputText) != len(self.rightWord):
                    print("OOOO CABEÇA DE CAVALO...\n")
            compare = CompareWord(inputText=inputText, rightText=self.rightWord)
            result = compare.outcome()


if __name__ == '__main__':
    game = StartGame()
    game.selectGameType()
    game.startGame()
