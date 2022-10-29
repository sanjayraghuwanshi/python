def turn_left(): () 
def move(): ()
def at_goal(): ()
def front_is_clear(): ()
def right_is_clear(): ()
def wall_on_right(): ()
def wall_in_front(): ()

#Code starts from here.
#This code leaves a edge case and needs a revisit on Day15 

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
       
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    if front_is_clear():
        move()
    else:
        turn_left()