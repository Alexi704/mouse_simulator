import pyautogui as pg
from time import sleep
from datetime import datetime
import random

MOVING_AREA = 80  # область перемещения в процентах
MIN_PAUSE = 11  # минимальное время ожидания между передвижениями мыши (в секундах)
MAX_PAUSE = 55  # максимальное время ожидания между передвижениями мыши (в секундах)

""" пауза и досрочное прекращение """
pg.PAUSE = 1  # вызывается пауза (в секундах), если мы перехватили управление
pg.FAILSAFE = False  # отключаем отказоустойчивость

x, y = pg.size()  # узнаем размер экрана

# задаем координаты области перемещения курсора
x1 = int(x * (100 - MOVING_AREA) / 100 / 2)
x2 = int(x - x * (100 - MOVING_AREA) / 100 / 2)
y1 = int(y * (100 - MOVING_AREA) / 100 / 2)
y2 = int(y - y * (100 - MOVING_AREA) / 100 / 2)

print(f'Размер вашего монитора: {x} x {y} пикселей.')
print(f'Активная территория передвижения мЫши по монитору: {MOVING_AREA}% (от центра).')

# переходим в центр экрана
sleep(0.1)
x_coordinate = x / 2
y_coordinate = y / 2
pg.moveTo(x_coordinate, y_coordinate, duration=1.2)
total_distance = 0

try:
    i = 1
    while True:
        sleep(random.randint(1, 3) / 10)

        # перемещаемся в рандомное место, в пределах нами заданной области
        movement_speed = random.randint(5, 22) / 10
        new_x_coordinate = random.randint(x1, x2)
        new_y_coordinate = random.randint(y1, y2)

        pg.moveTo(new_x_coordinate, new_y_coordinate, duration=movement_speed)
        # now_ = datetime.now()
        now_ = datetime.today()

        print(f'{i}) Мышь ушла по адресу: {new_x_coordinate:>4}x{new_y_coordinate:<4}', end=' ')
        # print(f'Сейчас: {now_.hour}ч.{now_.minute}м.{now_.second}c. /{now_.day}-{now_.month}-{now_.year}/')
        print(f'Сейчас: {now_.strftime("%Hч.%Mм.%Sс. /%d-%m-%Y/")}')

        x_coordinate = new_x_coordinate
        y_coordinate = new_y_coordinate

        # делаем клик правой кнопкой мыши
        # pg.click(x_coordinate, y_coordinate, 1, 1,'right')
        # sleep(random.randint(1, 3) / 10)
        # жмем  Esc
        pg.press('esc')

        # ждем от 1 до 5 минут
        pause_time = random.randint(MIN_PAUSE, MAX_PAUSE)

        # ставим правильное окончание
        numb_ending = str(pause_time)[-2:]
        if numb_ending in ['11', '12', '13', '14']:
            ending = ''
        else:
            numb_ending = numb_ending[-1]
            if numb_ending in ['2', '3', '4']:
                ending = 'ы'
            elif numb_ending == '1':
                ending = 'a'
            else:
                ending = ''
        print(f'... отдыхаем: {pause_time} секунд{ending} ...')
        sleep(pause_time)

        i += 1
except KeyboardInterrupt:
    pass
