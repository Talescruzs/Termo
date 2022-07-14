from tkinter import *

class Teste:
    def __init__(self):
        self.root = Tk()

    def onClick(self):
        palavra = self.campo.get()
        self.campo.delete(0, END)
        txt = Label(self.root, text=palavra)
        txt.pack()

    def main(self):
        t1 = Label(self.root, text="TERMO")
        self.campo = Entry(self.root, width=50)
        self.campo.insert(0, "aaa")

        button = Button(self.root, text="CONFIRMA", state=NORMAL, command=self.onClick)

        t1.pack()
        self.campo.pack()
        button.pack()

        self.root.mainloop()

if __name__ == '__main__':
    Teste().main()