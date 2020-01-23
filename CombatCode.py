import turtle as trtl
import random as rand
 
 
Joah = trtl.Turtle()
Fireball = trtl.Turtle()
Meteor = trtl.Turtle()
Tornado = trtl.Turtle()
Super_fireball = trtl.Turtle()
Cursed_armor = trtl.Turtle()
hp_bar = trtl.Turtle()
enemy = trtl.Turtle()
#how a background changes
wn = trtl.Screen()
wn.bgpic("firstcity.png")
background = 0

#how a background changes

def next_arrow():
    wn.bgpic("forest.png")
    background = (background + 1)
 
back_arrow_pic = "back_arrow.gif"
def back_arrow():
    wn.bgpic("firstcity.png")

wn.onclick(next_arrow)
    
myList = [enemy, nothing]
 
#this determines if an encounter happens when the background changes
 
wn.background()
if background >= 1:
    rand.choice(myList)   
 
#this code is for when an encounter happens
Cursed_armor = "CursedArmor.gif"
hp_bar.pencolor("red")
hp_bar.pensize(5)
 
def encounter():
   if outcomes[enemy]:
       Cursed_armor.goto(200,1)
       hp_bar.penup()
       hp_bar.goto(200,200)
       hp_bar.pendown()
       hp_bar.forward(50)
    
 
#this code are the spell gifs
 
Fireball = "Fireball.gif"
Meteor = "meteor.gif"
Tornado = "tornado.gif"
Super_fireball = "opfireball.gif"
 
#this code will keep track of the pp
Fb = 5
Torn = 5
Met = 5
Super = 5
 
#this code is the spell list
wn = trtl.Screen()
Combat_list = ["Fireball", "Tornado", "Meteor", "Super_fireball"]
#This needs to be completed it going to pop out spell moves when pp=0
    
 
#this code will be the user choosing a spell
Joah.print("These are your spells", Combat_list )
Spell = input("Choose a spell?")
 
#this might be wrong
if Spell is Fireball():
    wn.setup(width=1.0, height=1.0)
    wn.addshape(Fireball)
    (Fb - 1)
 
elif Spell is Tornado():
    wn.setup(width=1.0, height=1.0)
    wn.addshape(Tornado)
    (Torn - 1)
 
elif Spell is Meteor():
    wn.setup(width=1.0, height=1.0)
    wn.addshape(Meteor)
    (Met - 1)
 
elif Spell is Super_fireball():
    wn.setup(width=1.0, height=1.0)
    wn.addshape(Super_Fireball)
    (Super - 1)
#movement functions
def Up():
    Joah.setheading(90)
    Joah.forward(10)

def Down():
    Joah.setheading(270)
    Joah.forward(10)
    
def Left():
    Joah.setheading(180)
    Joah.forward(10)

def Right():
    Joah.setheading(0)
    Joah.forward(10)

 
 
 
 
 
 
 
 #-----events----------------
wn.onkeypress(Right, "Right")
wn.onkeypress(Left, "Left")
wn.onkeypress(Up,"Up")
wn.onkeypress(Down,"Down")
wn.onclick(next_arrow)
wn.onclick(back_arrow)
 
wn.listen()
trtl.mainloop()
