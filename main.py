import turtle as t
import math
import random
from time import sleep

WIDTH = 500
HEIGHT = 500

def init():
    t.screensize(WIDTH, HEIGHT)
    t.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    t.speed(0) # Set to 0 once operational

def getMidpoint(p1, p2):
    """
    Return the midpoint of tuples p1 and p2
    """
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def placePoint(p):
    t.penup()
    t.setpos(p)
    t.pendown()
    t.circle(2)

def main():
    # Set up turtle
    init()
    
    tri_pt_1 = (0, 0)
    tri_pt_2 = (WIDTH, 0)
    tri_pt_3 = (WIDTH / 2, WIDTH * math.sin(math.radians(60)))
    
    cur_point = (WIDTH / 2, HEIGHT / 2)
    placePoint(cur_point)
    
    while True:
        # Get a random number between 0 and 1 that will be used later to select
        # which triangle point will be used for the midpoint
        roll = random.random()
        selected_point = tuple()

        # Assign equal probabilities to each of the triangle points
        if 0 <= roll < 0.33:
            selected_point = tri_pt_1
        elif 0.33 <= roll < 0.66:
            selected_point = tri_pt_2
        else:
            selected_point = tri_pt_3

        # Set the current point to the midpoint of the previous point, and the
        # triangle point that was selected as a result of the roll
        cur_point = getMidpoint(cur_point, selected_point)
        placePoint(cur_point)
        sleep(0.1)


if __name__ == "__main__":
    main()