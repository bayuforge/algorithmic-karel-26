# Notice:
# You can solve this problem with either the help of while and conditions when doubling things
# But the more efficient way is to use Recursive Function
# Recursive Function allows you to call 'themself', this case we want to double the result
# Just like how you did it in your head, but model it computationally!

# Function to double each inputted numbers
def double_the_number(n:int):
    res = n + n
    print(res)
    if res < 100:
        double_the_number(res) # this is where the magic happens with recursion
    else:
        return res

def main():
    curr_value = int(input("Enter a number: "))

    # We do not need start variable
    # Because it will makes the program failed because at (res < 100) condition, the function returns none.
    start = double_the_number(curr_value)

if __name__ == '__main__':
    main()


# func a -> n + n
# func a -> res < 100 -> call a -> else: return res
