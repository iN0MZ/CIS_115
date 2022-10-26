# stopSign.py
# Ryan Carroll
# CIS 115 (NLE01)
# Draws a stop sign in turtle with correct colors and specifications

import turtle as t         # Imports turtle module and sets it to t

angle = 360/8              # Sets angle variable for 8 sides
t.penup()                  # Lifts pen so no additional line is drawn while traveling
t.goto(-50,-50)            # Moves starting position -50 X and -50 Y on the turtle window
t.pendown()                # Sets pen back down to start drawing
t.begin_fill()             # Starts the fill process for the stop sign
t.bgcolor("DeepSkyBlue")   # Sets background color
t.fillcolor("darkred")     # Sets stop sign fill color
t.pencolor("white")        # Sets pen (outline) color
t.width("3")               # Sets thiccness of outline

for i in range(9):         # run this loop for a total of 8 times
    t.forward(100)         # each time move forward 100
    t.left(angle)          # each time move left by the angle variable

t.end_fill()               # stops coloring
t.done()                   # error handling
