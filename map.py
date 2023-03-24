#Скрипт карты/поля

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
    def printmap(self):
        print("🟥" * (self.w + 2))  # Отрисовка верхних
        for row in self.cells:
            print("🟥", end="")  # слева каждой строки
            for cell in row:
                print(CELLTYPES[cell], end="")
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

    #Генерация рек
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


# Тестовая часть
c1 = Map(20, 10)
print(c1.checkcell(1, 1))
c1.genforest(3, 10)
c1.genriver(12)
c1.genriver(2)
c1.printmap()
