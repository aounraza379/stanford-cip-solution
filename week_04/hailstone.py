"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    user_number = int(input('Enter a number: '))

    while user_number != 1:
        if user_number % 2 == 0:
            new_user_number = user_number // 2
            print(f'{user_number} is even, so I take half: {new_user_number}')
            user_number = new_user_number
        else:
            new_user_number = (3 * user_number) + 1
            print(f'{user_number} is odd, so I make 3n + 1: {new_user_number}')
            user_number = new_user_number
    
if __name__ == "__main__":
    main()