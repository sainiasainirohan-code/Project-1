import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Food Slicing Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Score
score = 0

# Score display
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(-350, 250)
score_pen.write(f"Score: {score}", font=("Arial", 16, "bold"))

# Food list
foods = []

colors = ["red", "green", "yellow", "orange", "purple"]

# Create food
for _ in range(5):
    food = turtle.Turtle()
    food.shape("circle")
    food.color(random.choice(colors))
    food.penup()
    food.goto(random.randint(-350, 350), random.randint(100, 300))
    food.speed(0)
    food.dy = random.randint(2, 5)
    foods.append(food)

# Update score
def update_score():
    score_pen.clear()
    score_pen.write(f"Score: {score}", font=("Arial", 16, "bold"))

# Slice food
def slice_food(x, y):
    global score

    for food in foods:
        if food.distance(x, y) < 25:
            food.goto(random.randint(-350, 350), 300)
            score += 1
            update_score()

screen.onclick(slice_food)

# Game loop
while True:
    screen.update()

    for food in foods:
        food.sety(food.ycor() - food.dy)

        # Reset food if it reaches bottom
        if food.ycor() < -300:
            food.goto(random.randint(-350, 350), 300)

screen.mainloop()