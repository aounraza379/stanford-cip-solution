from karel.stanfordkarel import *

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        complete_row()
        back_to_base()
        step_up()
    turn_right()

def complete_row():
    while front_is_clear():
        put_beeper()
        move()

def back_to_base():
    put_beeper()
    turn_around()
    while front_is_clear():
        move()

def safe_move():
    if front_is_clear():
        move()
    else:
        turn_right()
        while front_is_clear():
            move()
        turn_around()
     
def step_up():
    turn_right()
    safe_move()
    turn_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()