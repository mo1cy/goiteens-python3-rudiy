"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.

"""

from random import * # рандомні числа (випадкові числа)
from turtle import *  # бібліотека для графіки
from freegames import vector # додаткова бібліотека для turtle

bird = vector(0, 0) # птах
balls = [] # це м'ячі
# функція для нажимання на екран, підстрибування
def tap(x, y):
    "Move bird up in response to screen tap."
    up = vector(0, 30) # 0,30 це відстань на яку ми підстрибуємо
    bird.move(up)
# перевірка на те чи ми заходимо за межі карти
def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200
# для малювання кольорів і графіки
def draw(alive):
    "Draw screen objects."
    clear()

    goto(bird.x, bird.y)
# якщо ми живі то світимося зеленим кольором
    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red') # якщо помираємо світимося червоним кольором
# м'ячі позначені чорним кольором
    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()

def move():
    "Update object positions."
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()