# Вертолёт (игрок)
from utils import randcell


# Класс вертолёта
class Helicopter:
    def __init__(self, w, h):  # w и h - максимальные точки поля
        rc = randcell(w, h)  # Выставить себя на случайных координатах поля (до границ)
        self.x = rc[0]
        self.y = rc[1]
        self.w = w
        self.h = h
        self.tank = 0
        self.mxtank = 1
        self.score = 0

    # Метод движения
    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        # Если новое значение x больше/равно нулю (Верхние границы карты) и меньше крайней x на карте (Нижние границы)
        # Аналогично с y
        if 0 <= ny < self.h and 0 <= nx < self.w:
            self.x = nx
            self.y = ny

    # Вывод статистики
    def prstats(self):
        print(f"💧: {self.tank}/{self.mxtank}    💲: {self.score}")
