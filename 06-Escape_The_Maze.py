# Day 6 -  Escape the Maze
# Python Functions and Karel
# Using https://reeborg.ca/index_en.html

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world.json&url=user_world%3Aproblem_world.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
'''
def hurdle():
    turn_left()
    move()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()
'''
# follow right edge as much as possible

# get to a wall 
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    

