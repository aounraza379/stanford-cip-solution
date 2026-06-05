"""
Program: Liftoff
--------------------
Countdown from 10 to 1 and then print Liftoff!
"""

def main():

    number = 10
    while number > 0:
        print(number)
        number -= 1

    print("Liftoff!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()