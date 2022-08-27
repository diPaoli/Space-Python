import turtle
import random
#import matplotlib.pyplot as plt

# setup the window and background
scr = turtle.Turtle()
scr.screen.bgpic('spaceBG.gif')
scr.screen.setup(600, 400)

# loads gif images
scr.screen.addshape('explosion.gif')
scr.screen.addshape('myShip.gif')
obsShapes = ['rock1.gif', 'rock2.gif', 'rock3.gif', 'rock4.gif', 'ufo.gif']
for s in obsShapes:
    scr.screen.addshape(s)


# shows how many lives are left
trtLives = turtle.Turtle(visible=False)
trtLives.penup()
scr.screen.addshape('lives.gif')
trtLives.shape('lives.gif')
trtLives.speed(0)
trtLives.setpos(-250,150)
stampLives = []
stampLives.append(trtLives.stamp())
trtLives.setx(-210)
stampLives.append(trtLives.stamp())
trtLives.setx(-170)
stampLives.append(trtLives.stamp())


# show the Score on top of the screen
score = 0
trtScore = turtle.Turtle(visible=False)
trtScore.penup()
trtScore.speed(0)
trtScore.setpos(250,150)
trtScore.pencolor('white')
trtScore.write('Score: '+ str(0), False, align="right", font=("Impact", 14, "normal"))


# adds my spaceship
myShip = turtle.Turtle()
myShip.penup()
myShip.setpos(-150,0)
myShip.shape('myShip.gif')
myShip.seth(180)
myShip.shapesize(2,4,3)
myShip.fillcolor('red')


# these defs control the movement of our 'turtle'
def up():
    if myShip.pos()[1] < 100:
        myShip.sety(myShip.pos()[1] + 50)


def down():
    if myShip.pos()[1] > -100:
        myShip.sety(myShip.pos()[1] - 50)

def close():
    scr.screen.bye()
    

# now associate the defs from above with certain keyboard events
scr.screen.onkey(up, 'Up')
scr.screen.onkey(down, 'Down')
scr.screen.onkey(close, 'Escape')
scr.screen.listen()


# Main game Loop
lives = 3
while lives > 0:
    #creates other turtle to simulate obstacles
    obs = turtle.Turtle(visible=False)
    obs.shape(random.choice(obsShapes))
    #obs.shapesize(2,random.randrange(1,3))
    obs.penup()
    obs.speed(0)
    obs.setpos(350,random.randrange(-100,100,50))
    obs.speed(random.randrange(2,4))
    obs.showturtle()
    obs.setx(-110)

    # tests if the ship crashed, show explosion
    if myShip.pos()[1] == obs.pos()[1]:
        # new Turtle to show explosion when it chashes
        explosion = turtle.Turtle(visible=False)
        explosion.speed(0)
        explosion.penup()
        explosion.shape('explosion.gif')
        explosion.setpos(myShip.pos())
        explosion.showturtle()
        explosion.screen.delay(100)
        lives -= 1
        trtLives.clearstamp(stampLives[lives])

        if lives == 0:
            # Game Over
            op = turtle.Turtle(visible=False)
            op.speed(0)
            op.penup()
            op.setpos(-50,100)
            op.pencolor('white')
            op.write('You Died!', font=('Constantia', 18, 'bold'))
            scr.screen.delay(0)
            
            # asks the name of the player to save in the DB
            pl_name = scr.screen.textinput('Record your score!', 'Type your name: ')

            # record player's score
            import db_func
            db_func.reg_Score(pl_name, score)

            # shows registered scores
            import gridScores
            gridScores.show_Score()
            

            break
        
        obs.hideturtle()
        explosion.hideturtle()
        explosion.screen.delay(10)
    else:
        # shows the score points earned for avoid obstacles
        score += 100
        trtScore.clear()
        trtScore.write('Score: '+ str(score), False, align="right", font=("Impact", 14, "normal"))

    obs.setx(-300)
    obs.hideturtle()
