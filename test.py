from libraries.Graphics import *

# def square(pt1x, pt1y, p2x, pt2y):
#     ln = Line(Point(pt1x, pt1y), Point(p2x,pt2y))

#     return ln

def main():
    win = GraphWin(title="Teste", width=700,  height=600)
    win.setBackground(color_rgb(0,0,0))

    gameName = Text(Point(350, 75), text="TERMO")
    gameName.setTextColor(color_rgb(255,255,255))
    gameName.setSize(35)
    gameName.draw(win)

    # for b in range(150, 500, 70):    #Colunas
    b=150
    for a in range(100, 600, 100): # Linhas
        rect = Rectangle(Point(a, b), Point(a+50, b+50))
        rect.setOutline(color_rgb(255,255,255))
        rect.setFill(color_rgb(255,255,0))
        rect.draw(win)

    inputBox = Entry(Point(300, 500), 5)
    inputBox.draw(win)

    txt = Text(Point(500, 600), text="")
    
    
    # if len(inputBox.getText())<=5:
    #     resposta = inputBox.getText()
    #     txt.setText(resposta)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()