import random


class WordsBase:
    "Classe da base de palavras"
    def __init__(self):
        file = open("words.txt", "r")
        self.words = str(file.read())
    def returnWord(self):
        "Retorna uma palavra sorteada da lista"
        wordsList = self.words.split(",")
        randomNumber = random.sample(range(len(wordsList)), k=1)[0]
        return wordsList[randomNumber]

if __name__ == '__main__':
    word = WordsBase()
    print(word.returnWord())