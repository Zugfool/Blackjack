#Blackjack
import random
import pandas as pd
import numpy as np
import turtle as t

kartlar="2 3 4 5 6 7 8 9 10 J Q K A "
full_kartlar=kartlar*4
full_kartlar_list=full_kartlar.split()
players=[]

timmy=t.Turtle()
timmy.pensize(6)
screen=t.Screen()
timmy.penup()
timmy.speed("fastest")
screen.screensize(600,450)
timmy.setpos(-300,200)

number= screen.numinput("","Enter the number of players: ")
for i in range(int(number)):
    name=screen.textinput("","Enter players name: ")
    players.append(name)
    
start= np.zeros(int(number))
start= list(start)
Points= pd.Series(start,players)
print("\n" + Points.to_string())

toplam=0
def pick(kart):
    global toplam
    if kart in "JQK":
        kart=10
        toplam+=int(kart)
    elif kart=="A":
        kart=11
        toplam+=int(kart)
        if toplam>=22:
            toplam=toplam-10
    else:
        toplam+=int(kart)
    return toplam

for j in players:
    timmy.penup()
    timmy.setx(-290)
    timmy.pendown()
    screen.clearscreen()
    timmy.penup()
    timmy.sety(200)
    timmy.pendown()
    timmy.write(j.capitalize() + " is playing", font=("Aria",30,"normal"))
    toplam=0
    cards_drawn=[]
    for i in range(3):
        kart=random.choice(full_kartlar_list)
        timmy.penup()
        timmy.seth(0)
        timmy.forward(70)
        timmy.sety(110)
        timmy.pendown()
        for y in range(4):
            timmy.color("black")
            timmy.forward(60)
            timmy.left(90)
        if i==1 or i==2:
            timmy.penup()
            timmy.sety(100)
            timmy.pendown()
            timmy.write(kart[0:], font=("Aria",50,"normal"))
            cards_drawn.append(kart)
            full_kartlar_list.remove(kart)
            toplam = pick(kart)
        else:
            pass
    while toplam<22:
        choice= screen.textinput("",f"\nYou are currently at {toplam}. Enter if you want to draw or stay: ")
        if choice.capitalize()=="Draw":
            kart=random.choice(full_kartlar_list)
            timmy.penup()
            timmy.sety(110)
            timmy.seth(0)
            timmy.forward(70)
            timmy.pendown()
            for x in range(4):
                timmy.forward(60)
                timmy.left(90)
            timmy.penup()
            timmy.sety(100)
            timmy.pendown()
            timmy.write(kart[0:], font=("Aria",50,"normal"))
            cards_drawn.append(kart)
            print(f"You drew {kart}")
            print(cards_drawn)
            toplam=pick(kart)      
        elif choice.capitalize()=="Stay":
            break
        else:
            print("Write your play correctly please.\n")
        if toplam>=22:
            print("You went above 21. Bad choice friend. Play Again :) \n")
            toplam="BROKE"
            break
        if len(cards_drawn)==5:
            print("You WIN regardless of the others points. \n")
            toplam="WIN"
            break
    Points[str(j)]=toplam
    print(Points.to_string())

screen.clearscreen()
timmy.write(Points.to_string(), font=("Aria",50,"normal"))
timmy.hideturtle()
screen.exitonclick()