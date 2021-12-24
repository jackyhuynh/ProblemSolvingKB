# import turtle as t
# import random
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colour = (r, g, b)
#     return colour
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(360//size_of_gap):
#         timmy.circle(100)
#         timmy.color(random_color())
#         timmy.setheading(timmy.heading()+size_of_gap)
#
#
# timmy = t.Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# t.colormode(255)
# color = ['green', 'blue', 'red', 'black', 'gray']
# """
# Pattern solve
# """
# # tommy = Turtle()
# # tommy.color("red")
# # shape = 3
# # circle = 360
# # outer=200
# #
# # for i in range(10):
# #     for _ in range(shape):
# #         tommy.forward(outer)
# #         timmy.forward(100)
# #         timmy.right(circle/shape)
# #         tommy.right(90)
# #         outer+=10
# #     shape += 1
# #     timmy.color(color[i%4])
# """
# Random direction
# """
# directions = [0, 90, 180, 270]
# timmy.pensize(1)
# timmy.speed("fastest")
# # for _ in range(200):
# #     timmy.color(random_color())
# #     timmy.forward(30)
# #     timmy.setheading(random.choice(directions))
# """
#
# """
# draw_spirograph(5)
#
# my_screen = t.Screen()
# my_screen.exitonclick()

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()