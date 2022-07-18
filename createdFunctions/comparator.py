class CompareWord():
    "Instancia o comparadar de palavras"
    def __init__(self):
        self.result = None
        self.final = list()

    def income(self, inputText, rightText):
        "compara as ruas palavras e atualiza o resultado como Passou ou Não passou e as posições das letras certas e erradas"
        self.inputText=inputText
        self.rightText=rightText
        self.passedWords=list()
        if self.inputText == self.rightText:
            self.result = True
        else:
            for letter in range((len(self.rightText))):
                if self.inputText[letter] == self.rightText[letter]:
                    self.final.append("Posição certa")
                    self.passedWords.append(self.inputText[letter])
                elif self.inputText[letter] in self.rightText:
                    self.final.append("Posição errada")
                else:
                    self.final.append("Letra errada")
            self.result = False

    def outcome(self):
        "Retorna o resultado da comparação"
        return self.result

    def overview(self):
        "Retorna os detalhes da comparação"
        return self.final

    def cleanFinal(self):
        "Limpa os detalhes da comparação"
        self.final.clear()

