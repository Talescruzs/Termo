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
                if len(inputText)!=len(rightWord):
                    print("OOOO CABEÇA DE CAVALO...")
            compare = CompareWord(inputText=inputText, rightText=rightWord)
            result = compare.outcome()


if __name__ == '__main__':
    StartGame()
