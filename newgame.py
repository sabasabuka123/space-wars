import random
import time
import turtle
import keyboard



score=0
live=3
# screen est up
wn=turtle.Screen()
wn.title('Space Wars')
wn.bgcolor('black')
wn.bgpic('rel.png')
wn.setup(width=800,height=600)
wn.tracer(4)

wn.register_shape('space\kometa.gif')
wn.register_shape('space\spaceship.gif')
wn.register_shape('space\hear.gif')
wn.register_shape('space\co.gif')

# goodplayer

name = turtle.Turtle()
name.speed(0)
name.shape('space\spaceship.gif')
name.color('white')
name.penup()
name.goto(-60,-50)
name.direction = 'stop'

# coin
nices=[]

for nice in range(4):
    nice = turtle.Turtle()
    nice.speed(0)
    nice.shape('space\co.gif')
    nice.color('green')
    nice.penup()
    nice.goto(-150,-100)
    nice.speed=random.randint(1,10)
    nices.append(nice)

# health
harts=[]

for hart in range(1):
    hart = turtle.Turtle()
    hart.speed(0)
    hart.shape('space\hear.gif')
    hart.color('green')
    hart.penup()
    hart.goto(100,-100)
    hart.speed=random.randint(1,10)
    harts.append(hart)

bads=[]
# badplyer
for bad in range(10):
    bad = turtle.Turtle()
    bad.speed(0)
    bad.shape('space\kometa.gif')
    bad.color('black')
    bad.penup()
    bad.goto((10,200))
    bad.speed=random.randint(1,10)
    bads.append(bad)
# pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.goto(0,260)
s=('curier', 24, 'normal')
pen.write('score:{} lives:{}'.format(score,live),align='center',font=s)

# moveee
def g_left():
    name.direction='left'
def g_right():
    name.direction='right'
def g_up():
    name.direction='up'
def g_down():
    name.direction='down'

wn.listen()
wn.onkeypress(g_left,"Left")
wn.onkeypress(g_right,"Right")
wn.onkeypress(g_up,"Up")
wn.onkeypress(g_down,"Down")


while True:
    wn.update()


    if name.xcor()>400 or name.xcor()<-400 or name.ycor()>300 or name.ycor()<-300:
        time.sleep(1)
        name.goto(0,0)
        name.direction='stop'

    if name.direction=='left':
        x=name.xcor()
        x-=4
        name.setx(x)
    if name.direction=='right':
        x=name.xcor()
        x+=4
        name.setx(x)
    if name.direction=='up':
        y=name.ycor()
        y+=4
        name.sety(y)
    if name.direction=='down':
        y=name.ycor()
        y-=4
        name.sety(y)
    # for baddd
    for bad in bads:    
        y = bad.ycor()
        y-= bad.speed
        bad.sety(y)
        # outside replay
        if y<-300:
            x=random.randint(-400,400)
            y=random.randint(300,400)
            bad.goto(x,y)
        if bad.distance(name)<30:
            x=random.randint(-400,400)
            y=random.randint(300,400)
            name.goto(x,y)
            live-=1
            score-=30
            pen.clear()
            pen.write('score:{} lives:{}'.format(score,live),align='center',font=s)
            print('score: {}'.format(score))
        if live==-1:
            time.sleep(1)
            pen.goto(0,0)
            k=('curier', 40, 'normal')
            pen.write('GAME OVER',align='center',font=k)
    # forr healthhh
    for nice in nices:    
        y = nice.ycor()
        y-= nice.speed
        nice.sety(y)
        # outside replay
        if y<-300:
            x=random.randint(-400,400)
            y=random.randint(300,400)
            nice.goto(x,y)
        if nice.distance(name)<30:
            x=random.randint(-400,400)
            y=random.randint(300,400)
            nice.goto(x,y)
            score+=30
            pen.clear()
            pen.write('score:{} lives:{}'.format(score,live),align='center',font=s)
            print('score: {}'.format(score))
    for hart in harts:    
        y = hart.ycor()
        y-= hart.speed
        # time.sleep(3)
        hart.sety(y)
        # outside replay
        if y<-300:
            x=random.randint(-400,400)
            y=random.randint(300,400)
            hart.goto(x,y)
        if hart.distance(name)<30:
            x=random.randint(-400,400)
            y=random.randint(300,400)
            hart.goto(x,y)
            live+=1
            pen.clear()
            pen.write('score:{} lives:{}'.format(score,live),align='center',font=s)
            print('score: {}'.format(score))
        if score==200:
            live+=1
        if live==-1:
            time.sleep(1)
            pen.goto(0,0)
            k=('curier', 40, 'normal')
            pen.write('GAME OVER',align='center',font=k)
        if score>500:
            time.sleep(1)
            pen.goto(0,0)
            z=('curier', 44, 'normal')
            pen.write('YOU WIN___I LOSE',align='center',font=z)


wn.mainloop()


