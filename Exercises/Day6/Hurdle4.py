def turn_left(): () 
def move(): ()
def at_goal(): ()
def front_is_clear(): ()
def wall_on_right(): ()
def wall_in_front(): ()

#Code starts from here.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def pass_the_wall():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()    
        
while not at_goal():
    if wall_in_front():
        pass_the_wall()
    else:
        move()