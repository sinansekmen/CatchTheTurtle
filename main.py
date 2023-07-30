import time
import turtle
from random import randint

CizimTahtasi = turtle.Screen()
CizimTahtasi.bgcolor("light blue")
CizimTahtasi.title("Catch The Turtle Game")
# CizimTahtasi.setup(1000, 1000)


CizimKaplumbagasi = turtle.Turtle()
CizimKaplumbagasi.color("black")
CizimKaplumbagasi.shape("turtle")
CizimKaplumbagasi.shapesize(3)


def karistir():
    CizimKaplumbagasi.speed(10)
    CizimKaplumbagasi.hideturtle()
    CizimKaplumbagasi.penup()
    CizimKaplumbagasi.goto(
        randint(-350, 0),
        randint(0, 350)
    )
    CizimKaplumbagasi.showturtle()
    time.sleep(1)


score = 0
def addscore():
    global score
    score += 1

CizimKaplumbagasi.onclick(lambda x, y: (CizimKaplumbagasi.hideturtle(), addscore()))




x = 0
while x < 20:
    karistir()
    x = x + 1
    print(score)

CizimTahtasi.title("GG FINAL SCORE: {}".format(score))
turtle.mainloop()