class CompareWord():
    def __init__(self, inputText, rightText):
        self.result = None
        self.difpos = set()
        self.equalpos = set()
        self.inters = set()
        self.inputText = list()
        self.rightText = list()
        for palavra in inputText:
            self.inputText.append(palavra)
        for palavra in rightText:
            self.rightText.append(palavra)

        if self.inputText == self.rightText:
            self.result = True
        else:
            for letra in range(len(self.rightText)):
                if self.rightText[letra] in self.inputText and self.rightText[letra] not in self.inters:
                    if self.rightText[letra] == self.inputText[letra]:
                        self.equalpos.add(self.rightText[letra])
                    else:
                        self.difpos.add(self.rightText[letra])
                self.inters = self.equalpos.union(self.difpos)
            self.result = False

    def retorno(self):
        if self.result:
            print("ACERTOU")
        else:
            print("As letras a seguir estão na palavra:")
            for letra in self.inputText:
                if letra in self.inters:
                    if letra in self.equalpos:
                        print("Posição correta:")
                    else:
                        print("Posição errada:")
                    print(letra)
        return self.result