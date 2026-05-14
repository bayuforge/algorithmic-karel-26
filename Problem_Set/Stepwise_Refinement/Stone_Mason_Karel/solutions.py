# add the parts below after "from karel.stanfordkarel import *" line

def go_down():
    turn_left()
    turn_left()

    while front_is_clear():
        move()

    turn_left()

def build_collumns():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    go_down()

def next_collumns():
    for i in range(4):
        move()

def build_last_collumns():
    turn_left()
    build_collumns()

# inside the main function add below:
while front_is_clear():
        if no_beepers_present():
            turn_left()
            build_collumns()
        else:
            next_collumns()
    build_last_collumns()

# make sure to lways watch for the correct indentation before hitting run
