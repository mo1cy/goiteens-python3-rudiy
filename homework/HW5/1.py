 # підключаємо бібліотеки 
from turtle import * # черепашка
from random import randrange # рандом
from freegames import square, vector # freegames - вектори

food = vector(0, 0) # 0, 0 початкові координати
snake = [vector(20, 5)] # 20, 5 початкові координати змійки
aim = vector(0, -15) # 0, -15 початковий напрям змійки

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    # Перевірка на те чи ми знаходимось всередині карти
    # Границі карти в пікселях, можна міняти
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    # рух змійки
    head = snake[-1].copy()
    head.move(aim)
    # Створюємо червоний квадрат перед змійкою, якщо вона вилазить за межі карти
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    
    # рандомна поява їжі
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    # колір змійки 
    
    for body in snake:
        square(body.x, body.y, 9, 'blue')
    
    # колір їжі
    square(food.x, food.y, 9, 'black')
    update()
    ontimer(move, 100)
# початковий розмір екрану
setup(450, 450, 390, 0)
hideturtle()
tracer(False)
listen()
# колір бекграунду
setup bgcolor("white")
# клавіші управління, можна міняти
onkey(lambda: change(10, 0), 'Right') # d
onkey(lambda: change(-10, 0), 'Left') # a
onkey(lambda: change(0, 10), 'Up') # w
onkey(lambda: change(0, -10), 'Down') # s
move()
done()