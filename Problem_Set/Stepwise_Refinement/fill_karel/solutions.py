# below are the parts you should add after this line: 'from karel.stanfordkarel import *'

# basic karel input for directions
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# func for last iteration
def max_celling():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

# 3 main func for the algo
def go_up():
    turn_left()
    turn_left()
    turn_left()
    move()
    ### NOTE
    ### front_is_blocked() = checks whether the front is blocked / equals to if not front_is_clear
    ### front_is_clear() = literary CHECKS if the way is CLEAR, it will still run even tho u are on top, idk why.
    
    # acts as a threshold
    if front_is_blocked():
        turn_right()
        max_celling()
    else:
        turn_right()
        fill_space()

def go_back():
    turn_around()
    while front_is_clear():
        move()

    go_up()

def fill_space():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

    go_back()

# at the main function just call below function, and you're ready to go!
fill_space()
