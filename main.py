# Основной скрипт
from helicopter import Helicopter
from map import Map
import time
import os
from pynput import keyboard

# Запрос ширины и высоты поля у игрока
MAP_W = int(input("Введите ширину экрана: "))
MAP_H = int(input("Введите высоту экрана: "))
TICKSLEEP = 0.05  # Интервал обновления экрана
TREE_UPD = 50  # Рост дерева раз в n тиков
FIRE_UPD = 100  # Выполнение операций с огнём раз в n тиков
TICK = 1  # Инициализация тиков
MOVES = {"w": (0, -1), "a": (-1, 0), "s": (0, 1), "d": (1, 0)}  # Набор движений по клавишам

# Инициализация поля
c1 = Map(MAP_W, MAP_H)  # Создание поля
heli = Helicopter(MAP_W, MAP_H)  # Размещение игрока на поле
c1.genforest(3, 10)  # Генерация деревьев
c1.genriver(12)  # Генерация реки с длиной n
c1.genriver(4)


# Обработка движений
def on_release(key):
    # if hasattr(key, 'char') and key.char == 'a':
    #    print(1111111111111111111111111111111111111111111)
    global heli
    if hasattr(key, 'char'):  # Исправление ошибки с Enter
        c = key.char
        if c in MOVES.keys():  # Если клавиша есть в списке движений, то просмотреть коорды и провести передвижение
            dx = MOVES[c][1]
            dy = MOVES[c][0]
            heli.move(dx, dy)


# Вспомогательная функция
listener = keyboard.Listener(
    on_release=on_release)
listener.start()

# Основной игровой цикл
while True:
    os.system("cls")  # Очистка экрана
    print(f"[{TICK}]", end="   ")  # Выведение номера тика
    heli.prstats() # Выведение статистики игры
    c1.heliproc(heli)
    c1.printmap(heli)  # Отрисовка карты
    TICK += 1
    time.sleep(TICKSLEEP)  # Задержка
    # Если тик делится без остатка на интервал обновления _ - выполнить
    if TICK % TREE_UPD == 0:
        c1.gentree()
    if TICK % FIRE_UPD == 0:
        c1.burn()
