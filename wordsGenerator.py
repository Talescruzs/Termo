import random

class WordsBase:
    "Classe da base de palavras"
    def __init__(self):
        file = open("words.txt", "r")
        self.words = str(file.read())

    def returnWord(self, choiceGameType=1):
        "Retorna uma palavra sorteada da lista"
        wordsList = self.words.split(",")
        a=False
        randomNumber = int()
        while a==False:
            randomNumber = random.sample(range(len(wordsList)), k=1)[0]
            if choiceGameType==2 or len(wordsList[randomNumber]) == 5:
                a=True
        return wordsList[randomNumber].lower()

if __name__ == '__main__':
    word = WordsBase()
    print(word.returnWord())