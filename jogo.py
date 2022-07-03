from wordsGenerator import WordsBase
from comparator import CompareWord

class StartGame:
    def __init__(self):
        word = WordsBase()
        rightWord = word.returnWord()
        result = False

        while(result == False):
            inputText = str()
            while(len(inputText)!=len(rightWord)):
                inputText = input("digita uma palavra com %d letras: " %len(rightWord))
                if len(inputText)!=5:
                    print("OOOO CABEÇA DE CAVALO...")
            comparaPalavra = CompareWord(inputText=inputText, rightText=rightWord)
            result = comparaPalavra.retorno()


if __name__ == '__main__':
    StartGame()