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

if __name__ == '__main__':
    main()