# Скрипт карты/поля
# Из utils.py импортировать метод/функцию randbool
from utils import randbool, randcell, randcell2

# Типы клеток
CELLTYPES = "🟩🌲🌊🏥💵🔥"


class Map:  # Класс карты
    def __init__(self, w, h):  # Инициализация поля
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]  # Пустое поле

    # Отрисовка поля
    def printmap(self, heli):
        print("🟥" * (self.w + 2))  # Отрисовка верхних
        for i in range(self.h):
            print("🟥", end="")  # слева каждой строки
            for j in range(self.w):
                if heli.x == i and heli.y == j:
                    print("🚁", end="")
                else:
                    print(CELLTYPES[self.cells[i][j]], end="")
            print("🟥")  # справа каждой строки
        print("🟥" * (self.w + 2))  # И нижних границ поля

    # Проверка вылезания клетки за границы карты
    def checkcell(self, y, x):
        if x < 0 or y < 0 or x >= self.w or y >= self.h:  # Если x и y Меньше 0/Больше высоты или ширины
            return False
        return True

    # Генерация леса
    # r - Числитель
    # mxr - Знаменатель
    # В итоге шанс r/mxr (Например 5/10 - 50%)
    def genforest(self, r, mxr):
        for i in range(self.h):
            for j in range(self.w):
                if randbool(r, mxr):
                    self.cells[i][j] = 1

    # Генерация рек
    def genriver(self, L):
        rc = randcell(self.w, self.h)
        rx = rc[0]
        ry = rc[1]
        if self.checkcell(rx, ry):  # Проверка выхода за границу
            self.cells[rx][ry] = 2
        while L > 0:
            rc2 = randcell2(rx, ry)
            rx2 = rc2[0]
            ry2 = rc2[1]
            if self.checkcell(rx2, ry2):  # Проверка выхода за границу
                self.cells[rx2][ry2] = 2
            L -= 1

    # Генерация деревьев
    def gentree(self):
        c = randcell(self.w, self.h)
        cx = c[0]
        cy = c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1

    # Генерация огня
    def genfire(self):
        c = randcell(self.w, self.h)  # В рандомной клетке генерировать огонь (если там есть дерево)
        cx = c[0]
        cy = c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    # Сжигание
    def burn(self):
        for i in range(self.h):  # Если в клетке есть огонь, то очистить её (превратить в поле)
            for j in range(self.w):
                cell = self.cells[i][j]
                if cell == 5:
                    self.cells[i][j] = 0
        for i in range(10):  # Сгенерировать огонь 10 раз
            self.genfire()

    def heliproc(self, heli):

        # Набор воды в бак
        c = self.cells[heli.x][heli.y]
        if c == 2:
            heli.tank = heli.mxtank

        # Тушение огня
        elif c == 5:
            if heli.tank > 0:
                self.cells[heli.x][heli.y] = 1
                heli.tank -= 1
                heli.score += 1
