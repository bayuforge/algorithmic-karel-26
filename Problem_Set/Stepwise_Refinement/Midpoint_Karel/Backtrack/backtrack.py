from karel.stanfordkarel import *

def turn_around():
    turn_left()
    turn_left()

def move_back_one_step():
    turn_around()
    move()

def move_to_edge():
    while front_is_clear():
        move()

def trace_end_point():
    move_to_edge()
    turn_around()
    put_beeper()

def analyze_start_end_point():
    trace_end_point()
    trace_end_point()
    move()

def backtracking():
    while no_beepers_present():
        move()
    move_back_one_step()
    put_beeper()
    move()

def turn_back_pivot():
    turn_around()
    while no_beepers_present():
        move()    

def pick_all_beepers():
    while beepers_present():
        pick_beeper()
        if front_is_clear():
            move()
        else:
            turn_back_pivot()
            move()

def main():
    analyze_start_end_point()
    while no_beepers_present():
        backtracking()
    # pivot point found next, pick the rest of the beepers
    pick_all_beepers()
    # last condition
    turn_back_pivot()
    turn_around()

# don't change this code
if __name__ == '__main__':
    main()
