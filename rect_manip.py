# rect_manip.py
# A program to manipulate rectangles.
# Author: Tyler McCreary

import math

class Rectangle:
    
    def __init__ (self, position, height, width):
        self.x = position[0]
        self.y = position[1]
        self.height = height
        self.width = width
    def __str__ (self):
        return "position: (" + str(self.x) + ", " + str(self.y) + "), height " + str(self.height) + ", width " + str(self.width)
    def move (self, translate):
        self.x = self.x + translate[0]
        self.y = self.y + translate[1]
    def grow (self, change_h, change_w):
        self.height = self.height + change_h
        self.width = self.width + change_w

def main():
    rect1 = Rectangle((1, 2), 3, 4)   # position (1,2), height 3, width 4
    rect1.grow(4, 3)                  # height 7, width 7
    rect1.move((2, 1))                # position (3,3)
    print(rect1)                      # print "position: (3, 3), height 7, width 7"
    
    rect2 = Rectangle((5, 5), 10, 10) # position (5,5), height 10, width 10
    rect2.move((2, -2))               # position (7,3)
    rect2.grow(-5, -5)                # height 5, width 5
    print(rect2)                      # print "position: (7, 3), height 5, width 5"

main()

