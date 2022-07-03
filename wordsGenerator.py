import random


class WordsBase:
    def __init__(self):
        pass
    def returnWord(self):
        file = open("words.txt", "r")
        words = str(file.read())
        wordsList = words.split(",")
        randomNumber = random.sample(range(len(wordsList)), k=1)[0]
        return wordsList[randomNumber]

if __name__ == '__main__':
    word = WordsBase()
    word.returnWord()