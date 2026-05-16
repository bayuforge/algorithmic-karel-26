# Here we introduce a greedy approach to solve the problem
# In which wouldn't work for all size of worlds (optimize for 2x2, 5x5, 6x6 only)

# basic function for turning around karel
def turn_around_180():
    turn_left()
    turn_left()

def execute_move():
    if front_is_clear():
        move()
    else:
        turn_around_180()
        move()
        turn_around_180()

def bruteforcing_second_guess():
    for i in range(2):
        execute_move()
    put_beeper()

# From this point just call the bruteforcing_second_guess function, inside the main function:
bruteforcing_second_guess()
