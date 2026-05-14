import random

def main():
    user_input = int(input("How many sides does your dice have? "))
    result = random.randint(1, user_input)
    print(f"Your roll is {result}")

if __name__ == '__main__':
    main()
