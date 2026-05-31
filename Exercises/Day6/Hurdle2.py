def turn_left(): () 
def move(): ()
def at_goal(): ()

#Code starts from here.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    jump()

#### OR ####

while not at_goal():
    jump()