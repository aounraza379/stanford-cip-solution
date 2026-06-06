import random

def main():
    print("Khansole Academy")

    x = random.randint(10,99)
    y = random.randint(10,99)

    print(f'What is {x} + {y}?')
    user_answer = int(input('Your answer: '))
    answer = x + y

    if user_answer == answer:
        print('Correct!')
    else:
        print('Incorrect.')
        print(f'The expected answer is {answer}')
    
if __name__ == '__main__':
    main()