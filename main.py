# Основной скрипт
from clouds import Clouds
from helicopter import Helicopter
from map import Map
import time
import os
from pynput import keyboard
from art import *
from random import randint as rnd
import json

tprint("Citr0n")

# Запрос ширины и высоты поля у игрока
MAP_W = int(input("Введите ширину экрана: "))
MAP_H = int(input("Введите высоту экрана: "))
TICKSLEEP = 0.05  # Интервал обновления экрана
TREE_UPD = 50  # Рост дерева раз в n тиков
FIRE_UPD = 100  # Выполнение операций с огнём раз в n тиков
CLOUDS_UPD = 50
TICK = 1  # Инициализация тиков
MOVES = {"w": (0, -1), "a": (-1, 0), "s": (0, 1), "d": (1, 0), "ц": (0, -1), "ф": (-1, 0), "ы": (0, 1),
         "в": (1, 0)}  # Набор движений по клавишам
CMXR = 10

# Инициализация поля
c1 = Map(MAP_W, MAP_H)  # Создание поля
heli = Helicopter(MAP_W, MAP_H)  # Размещение игрока на поле
clouds = Clouds(MAP_W, MAP_H)
c1.genforest(3, 10)  # Генерация деревьев
c1.genriver(12)  # Генерация реки с длиной n
c1.genriver(4)
c1.genshop()
c1.genhospital()


# Обработка движений
def on_release(key):
    # if hasattr(key, 'char') and key.char == 'a':
    #    print(1111111111111111111111111111111111111111111)
    global heli
    global TICK
    if hasattr(key, 'char'):  # Исправление ошибки с Enter
        c = key.char
        if c in MOVES.keys():  # Если клавиша есть в списке движений, то просмотреть коорды и провести передвижение
            dx = MOVES[c][1]
            dy = MOVES[c][0]
            heli.move(dx, dy)
        elif c == "f" or c == "а":  # Сохранение данных в save.json
            data = {'map': c1.export(),
                    "heli": heli.export(),
                    "clouds": clouds.export(),
                    "tick": TICK}
            with open("save.json", "w") as save:
                json.dump(data, save)
        elif c == "g" or c == "п":  # Загрузка данных из save.json
            with open("save.json", "r") as save:
                data = json.load(save)
                TICK = data['tick']
                heli.importd(data['heli'])
                clouds.importd(data['clouds'])
                c1.importd(data['map'])


# Вспомогательная функция
listener = keyboard.Listener(
    on_release=on_release)
listener.start()

# Основной игровой цикл
while True:
    os.system("cls")  # Очистка экрана
    print(f"[{TICK}]", end="   ")  # Выведение номера тика
    heli.prstats()  # Выведение статистики игры
    c1.heliproc(heli, clouds)
    c1.printmap(heli, clouds)  # Отрисовка карты
    TICK += 1
    time.sleep(TICKSLEEP)  # Задержка
    # Если тик делится без остатка на интервал обновления _ - выполнить
    if TICK % TREE_UPD == 0:
        c1.gentree()
    if TICK % FIRE_UPD == 0:
        c1.burn()
    if TICK % CLOUDS_UPD == 0:
        r = rnd(1, CMXR - 7)
        g = rnd(1, CMXR - 8)
        clouds.updateclouds(r, CMXR, g, CMXR)
