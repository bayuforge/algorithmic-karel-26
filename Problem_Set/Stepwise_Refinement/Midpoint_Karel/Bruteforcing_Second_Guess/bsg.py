# This method works perfectly for 2x2, 5x5, 6x6 size!
# it is designed as the greedy approach to solve the problems.

# basic function for turning around karel
def turn_around():
    turn_left()
    turn_left()

def execute_move():
    # If the way is clear for the next 2 steps, then move
    if front_is_clear():
        move()
    # if not then go back one step
    else:
        turn_around()
        move()
        turn_around()

# Here we introduce a greedy approach to the problems
def bruteforcing_second_guess():
    for i in range(2):
        execute_move()
    put_beeper() # then place the beeper at the end of the move

# To start this function, just call the function below inside the main function
bruteforcing_second_guess()
