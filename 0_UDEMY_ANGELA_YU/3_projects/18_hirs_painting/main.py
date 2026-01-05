from turtle import Turtle,Screen,colormode
import random

# #Insert color code
# import colorgram

# colors = colorgram.extract(
#     r'C:\\Users\\samhayder\\OneDrive\\Desktop\\python\\0_UDEMY_ANGELA_YU\\3_projects\\18_hirs_painting\\image1.png',
#     10
# )

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)
#     rgb_colors.append(rgb)

# print(rgb_colors)

tim = Turtle()
colormode(255)
tim.penup()
tim.speed("fastest")

tim.setheading(235)
tim.fd(420)
tim.setheading(0)
num_of_dots = 140

rgb_colors = [(101, 190, 171), (100, 164, 209), (207, 137, 182), (213, 230, 240), (56, 179, 154), (49, 124, 170), (187, 222, 211), (25, 26, 26), (217, 163, 85)]

for dot_count in range(1,num_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.fd(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)


tim.hideturtle()

screen = Screen()
screen.exitonclick()