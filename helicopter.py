# Вертолёт (игрок)
from map import UP_COST
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
        self.hp = 1000

    # Метод движения
    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        # Если новое значение x больше/равно нулю (Верхние границы карты) и меньше крайней x на карте (Нижние границы)
        # Аналогично с y
        if nx >=0 and ny >=0 and nx < self.w and ny < self.h:
            self.x = nx
            self.y = ny

    # Вывод статистики
    def prstats(self):
        print(f"💧: {self.tank}/{self.mxtank}    💲: {self.score}/{UP_COST}   ❤️: {self.hp}")

    def export(self):  # Сохранение
        return {"x": self.x,
                "y": self.y,
                "tank": self.tank,
                "mxtank": self.mxtank,
                "score": self.score,
                "hp": self.hp,
                }

    def importd(self, data):  # Загрузка
        self.x = data['x']
        self.y = data['y']
        self.tank = data['tank']
        self.mxtank = data['mxtank']
        self.score = data['score']
        self.hp = data['hp']