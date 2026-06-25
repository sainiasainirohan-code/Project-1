from turtle import*
import colorsys


bgcolor("black")
title("RAINBOW TURTLE ANIMATION")

speed(0)
pensize(2)
hideturtle()
tracer(0)

h=0

penup()
goto(0, 0)
pendown()

for i in range(16):
    for j in range(18):

        c=colorsys.hsv_to_rgb(h,1,1)
        pencolor(c)

        h+=0.005

        right(90)
        circle(150-j*6,90)
        left(90)
        circle(150-j*6,90)
        right(180)
        circle(40,24)
    right(5)
    update()
done()            
