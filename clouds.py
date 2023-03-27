# Облака
from utils import randbool


class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(h)] for j in range(w)]

    def updateclouds(self, r, mxr, g, mxg):
        for i in range(self.w):
            for j in range(self.h):
                if randbool(r, mxr):  # Генерация облаков
                    self.cells[i][j] = 1
                    if randbool(g, mxg):  # Генерация по соотношению обычные/грозовые
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0

    def export(self):  # Сохранение
        return {"cells": self.cells}

    def importd(self, data):  # Загрузка
        self.cells = data["cells"]
