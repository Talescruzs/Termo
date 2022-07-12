class CompareWord():
    "Instancia o comparadar de palavras"
    def __init__(self):
        self.result = None
        self.final = list()

    def income(self, inputText, rightText):
        "compara as ruas palavras e atualiza o resultado como Passou ou Não passou e as posições das letras certas e erradas"
        self.inputText=inputText
        self.rightText=rightText
        if self.inputText == self.rightText:
            self.result = True
        else:
            for letter in range((len(self.rightText))):
                if self.inputText[letter] == self.rightText[letter]:
                    self.final.append("Posição certa")
                elif self.inputText[letter] in self.rightText:
                    self.final.append("Posição errada")
                else:
                    self.final.append("Letra errada")
            self.result = False

    def outcome(self):
        "Printa o resultado da comparação"
        if self.result:
            print("ACERTOU")
        else:
            print("Errou:")
            for result in range(len(self.final)):
                # if self.final[result] != "Letra errada":      PODE SER USADO CASO QUEIRA MOSTRAR APENAS AS LETRAS QUE ESTÃO NA PALAVRA, EU ACHO MAIS CONFUSO
                #     print("%s : %s" %(self.inputText[result], self.final[result]))
                print("%s : %s" %(self.inputText[result], self.final[result])) 
        self.final.clear()
        return self.result
