from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

# Without Extension
def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    for i in range(N_CIRCLES):
        color = random_color()
        x = random.randint(0, CANVAS_WIDTH) 
        y = random.randint(0, CANVAS_HEIGHT)

        canvas.create_oval(
            x,
            y,
            x + CIRCLE_SIZE, 
            y + CIRCLE_SIZE, 
            color 
            )
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)


# Possible Extensions:
# If you find you have extra time you can try adding the following extensions on to this problem
# 1. Draw a random number of circles between 1 and 20
# 2. Draw circles of a random size 
# 3. Draw the circles such that all parts of the circle are within the canvas 

# Possible Extension Solutions:
#______________________________
# from graphics import Canvas
# import random

# CANVAS_WIDTH = 300
# CANVAS_HEIGHT = 300
# N_CIRCLES = random.randint(0,20) # Random circles between 0 and 20

# def main():
#     print(f'{N_CIRCLES} Random Circles')
#     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

#     for i in range(N_CIRCLES):
#         CIRCLE_SIZE = random.randint(0,20) # Random circle size
#         color = random_color()
        
#         # All circles are inside canvas
#         x = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE) 
#         y = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)

#         canvas.create_oval(
#             x,
#             y,
#             x + CIRCLE_SIZE, 
#             y + CIRCLE_SIZE, 
#             color 
#             )
    
# def random_color():
#     """
#     This is a function to use to get a random color for each circle. We have
#     defined this for you and there is no need to edit code in this function,
#     but feel free to read it over if you are interested. 
#     """
#     colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
#     return random.choice(colors)

# if __name__ == '__main__':
#     main()
# _________________________
if __name__ == '__main__':
    main()