from karel.stanfordkarel import *

def turn_around():
    turn_left()
    turn_left()

def back_to_start():
    turn_around()
    move()
    turn_around()

def place_at_one():
    put_beeper()
    move()

    if front_is_clear():
        back_to_start()
        threshold()
    else:
        back_to_start()

def go_home_pick_beeper():
    turn_around()
    
    while front_is_clear():
        move()
    
    turn_around()
    pick_beeper()

def place_at_third(): # 5 x 5
    go_home_pick_beeper()

    move()
    move()
    put_beeper()

def place_at_fifth(): # 6 x 6
    move()
    if front_is_clear():
        turn_around()
        move()
        turn_around()
        place_at_last()
    else:
        place_at_third()
    

def place_at_last(): # 11 x 11
    go_home_pick_beeper()

    for i in range(5):
        move()
    put_beeper()

def threshold():
    for i in range(4):
        move()
    
    if front_is_blocked(): # 5 x 5
        place_at_third()
    else:
        place_at_fifth()
    

def main():
    place_at_one()

if __name__ == '__main__':
    main()
