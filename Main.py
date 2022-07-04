from wordsGenerator import WordsBase
from comparator import CompareWord

class StartGame:
    def __init__(self):
        a=True
        while a:
            choiceGameType = int(input("Tipos: \n1=Normal \n2=Versus\nDigite qual modo queres: "))

            if choiceGameType == 1:
                word = WordsBase()
                rightWord = word.returnWord()
                break
            elif choiceGameType == 2:
                rightWord = input("digita a palavra para o seu adversário: ")
                break
            else:
                print("OOOO CABEÇA DE CAVALO...")

        result = False
        while(result == False):
            inputText = str()
            while(len(inputText)!=len(rightWord)):
                inputText = input("digita uma palavra com %d letras: " %len(rightWord))
                if len(inputText)!=len(rightWord):
                    print("OOOO CABEÇA DE CAVALO...")
            compare = CompareWord(inputText=inputText, rightText=rightWord)
            result = compare.outcome()


if __name__ == '__main__':
    StartGame()
