#Day6

"""
Reborg's world - https://aroberge.github.io/reeborg-staging/?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_around():
    turn_left()
    turn_left()
    
"""
#Using below to ignore syntax errors in code.
# these functions are already present in reborg's world
def turn_left(): () 
def move(): ()
#############################################

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def walk():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()

for i in range(6):
    walk()
    turn_left()
