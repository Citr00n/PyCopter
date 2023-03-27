# PyCopter
Простая консольная игра, написанная на питоне в рамках проекта "Код будущего" (с некоторыми доработками)
## Смысл игры
Игрок управляет вертолётом, главная цель игры - тушить (периодически загорающиеся) деревья
## Игровое поле
**Размеры игрового поля задаются в начале игры**

![Игровое поле](https://i.imgur.com/FuOIvrg.png)

Поле состоит из двух частей - строки статистики и игровой карты
В строке статистики отображается количество воды в баке (💧), количество очков (💲, *баланс/цена улучшения*) и количество жизней (❤️).

В игре существует несколько типов клеток:

 - Поле - 🟩  [Просто клетка 🗿]
 - Вода - 🌊 [При попадании на клетку бак заполняется до максимума]
 - Деревья  - 🌲 [Может возгореться раз в 100 тиков, новое появляется раз в 50 тиков]
 - Магазин - 🏪 [При попадании на клетку с игрока снимается 5 очков (если они есть) и вместительность бака увеличивается на одну единицу]
 - Госпиталь - 🏥 [При попадании на клетку с игрока снимается 5 очков (если они есть) и  его здоровье восстанавливается на 100 очков]
 - Огонь - 🔥 [Пропадает через 100 тиков после появления, оставляя поле. Игрок может потушить его, потратив 1 воду, и получить 1 очко]
 
 Также в игре существует отдельный слой облаков:
 
 - Обычное облако - ☁️ [Закрывает обзор]
 - Грозовое облако - 🌩️ [Снимает с игрока по 10 hp за каждый тик в котором он находится в облаке]
 
 ## Управление
 Управление в игре осуществляется при помощи данных клавиш:
 
|Клавиша| Действие |
|-- |--|
|W/Ц| Вверх |
|A/Ф| Влево |
|S/Ы | Вниз
D/В| Вправо |
F/А | Сохранить состояние
G/П | Загрузить состояние

## Сохранение
Игра поддерживает возможность сохранять и своё состояние (в файл save.json) и загружать его, таким образом можно выйти из игры и продолжить играть позже с сохранённым прогрессом.


# Внимание!!
Приведённое выше изображение поля актуально только для пользователей Win11, т.к. в каждой ОС предустановлены разные шрифты для emoji.



