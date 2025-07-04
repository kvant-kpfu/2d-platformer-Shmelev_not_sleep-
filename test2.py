import turtle
import random
import time
import math
import sys
import os
from tkinter import Tk, Label, Butto
screen = turtle.Screen()
shmelev = turtle.Turtle()
screen.tracer(0)
shmelev.penup()
shmelev.speed(0)
shmelev.shape("circle")
shmelev.color('yellow')
deti = []
screen.setup(width=700, height=700)
screen.title("ШМЕЛЁВ НЕ СПИТ")
score = 0
start = time.time()
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(330, 310)

def setup_score_display():
    score_display = turtle.Turtle()
    score_display.hideturtle()
    score_display.penup()
    score_display.goto(-222, 310)
 
    def update_score():
        score_display.clear()
        score_display.write(f"Ваше очко: {score}", align="center", font=("Arial", 20, "normal"))
        screen.ontimer(update_score, 100) 

    update_score()

setup_score_display()

def spawnRebenok():
    for i in range(random.randrange(1, 2)):
        reb = turtle.Turtle()
        reb.shape("square")
        reb.color("green")
        reb.speed(0)
        reb.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        reb.dx = random.randrange(-20, 20)/75
        reb.dy = random.randrange(-20, 20)/75
        reb.penup()
        x = random.randrange(-300, 300)
        y = random.randrange(-300, 300)
        reb.goto(x, y)
        deti.append(reb)
spawnRebenok()
count_step = 0

highlighting = turtle.Turtle()
highlighting.ht()
highlighting.penup()
highlighting.setpos(305, 305)
highlighting.pendown()
for i in range(4): 
    highlighting.forward(-610) 
    highlighting.right(270)

highlighting.ht()

def move_forward():
  y = shmelev.ycor()
  y += 20
  shmelev.sety(y)
   

def move_backword():
  y = shmelev.ycor()
  y += -20
  shmelev.sety(y)
  
def turn_left():
  x = shmelev.xcor()
  x += -20
  shmelev.setx(x)
def turn_right():
  x = shmelev.xcor()
  x += 20
  shmelev.setx(x)
screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backword, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
pen.clear()

def checking(figura):
  if figura.xcor() > 300:
    figura.setx(-300)

  if figura.xcor() < -300:
    figura.setx(300)

  if figura.ycor() > 300:
    figura.sety(-300)

  if figura.ycor() < -300:
    figura.sety(300)

def get_distance_shmelev_reb(reb):
    x_distance = (shmelev.xcor() - reb.xcor()) ** 2
    y_distance = (shmelev.ycor() - reb.ycor()) ** 2
    return (x_distance + y_distance) ** 0.5

def checker_stolknovenia(reb):
    if get_distance_shmelev_reb(reb) <= 10:
        return True
    else:
        return False

game_over = False
step_over = False
while not game_over:
    egg = time.time()
    pen.clear()
    pen.write(f"Время: {round(egg - start, 1)} сек", align="right", font=("Arial", 24, "normal"))
    
    checking(shmelev)
    screen.update()
    count_step += 1
    for reb in deti:
        checking(reb)
        if checker_stolknovenia(reb):
            ind = deti.index(reb)
            deti = deti[0:ind] + deti[ind + 1:]
            reb.ht()
            score += 1
        reb.setpos(reb.xcor() + reb.dx, reb.ycor() + reb.dy)
        if count_step == 7500:
            reb.dx = random.randrange(-20, 20)/75
            reb.dy = random.randrange(-20, 20)/75
            step_over = True
    
    if step_over is True:
        count_step = 0
    if len(deti) == 0:
        game_over = True
        end = time.time()
        pen.clear()
        screen.bgcolor("green")
        
        win = turtle.Turtle()
        win.ht()
        win.penup()
        win.goto(0, 0)
        win.write("ПОБЕДА!!!\n", align="center", font=("Arial", 40, "normal"))
        length = round(end - start,3)
        win.write(f"{length} СЕКУНД", align="center", font=("Times", 18, "normal"))

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
root = Tk()
Label(root, text="Игра закончилась!").pack()
Button(root, text="начать заново", command=restart_program).pack()
root.mainloop()


main_window()

    
screen.update()

screen.mainloop()
