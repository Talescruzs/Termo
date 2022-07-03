class CompareWord():
    def __init__(self, inputText, rightText):
        self.result = None
        self.difpos = set()
        self.equalpos = set()
        self.union = set()
        self.inputText = list()
        self.rightText = list()
        for word in inputText:
            self.inputText.append(word)
        for word in rightText:
            self.rightText.append(word)

        if self.inputText == self.rightText:
            self.result = True
        else:
            for letter in range(len(self.rightText)):
                if self.rightText[letter] in self.inputText and self.inputText[letter] not in self.union:
                    if self.rightText[letter] == self.inputText[letter]:
                        self.equalpos.add(self.rightText[letter])
                    else:
                        self.difpos.add(self.rightText[letter])
                self.union = self.equalpos.union(self.difpos)
            self.result = False

    def outcome(self):
        if self.result:
            print("ACERTOU")
        else:
            print("As letras a seguir estão na palavra:")
            for letter in self.inputText:
                if letter in self.union:
                    if letter in self.equalpos:
                        print("Posição correta:")
                    else:
                        print("Posição errada:")
                    print(letter)
        return self.result
