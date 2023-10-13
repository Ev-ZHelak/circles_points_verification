import matplotlib

matplotlib.use('TkAgg')  # Выберите подходящий бэкенд (например, 'TkAgg' или 'Qt5Agg')

import matplotlib.pyplot as plt
from random import randint as ran
from time import sleep


def check(circle_in: tuple[int, int, int], point: [int, int]) -> bool:
    '''уравнение - (x−h)^2+(y−k)^2=r^2 '''

    # координаты центра и радиус окружности
    x_center, y_center, radius = circle_in

    # координаты точки
    x_point, y_point = point
    return (x_point - x_center) ** 2 + (y_point - y_center) ** 2 <= radius ** 2


def draw(circle_in: tuple[int, int, int], point_in: [int, int]) -> None:
    # Задаем координаты центра и радиус окружности
    x_center, y_center, radius = circle_in

    # Задаем координаты точки
    x_point, y_point = point_in

    # Создаем фигуру
    fig, ax = plt.subplots()

    # Рисуем окружность
    circle = plt.Circle((x_center, y_center), radius, fill=False, color='b', label='Окружность')
    ax.add_patch(circle)

    # Рисуем центр окружности
    ax.plot(x_center, y_center, 'go', label='Центр окружности')

    # Рисуем точку
    ax.plot(x_point, y_point, 'ro', label='Точка проверки')

    # Устанавливаем аспект графика, чтобы окружность не выглядела сжатой
    ax.set_aspect('equal', 'box')

    # Добавляем подписи к осям
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    # # Устанавливаем пределы осей
    merge_point = max(tuple(abs(i) for i in circle_in[:-1]) + point_in) + radius + 10
    x = -merge_point
    y = merge_point
    ax.set_xlim([x, y])
    ax.set_ylim([x, y])

    # Добавляем легенду
    plt.legend()

    # Цвет фона
    ax.set_facecolor('lightblue')

    # Добавляем подписи к осям и заголовок
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    func_check = check(circle_in, point_in)
    ax.set_title(f'Окружность и Точка '
                    f'(func_check - {func_check})\n'
                    f'Координаты circle {circle_in}, point {point_in}')

    # Показываем график
    plt.show(block=False)
    plt.close()
    sleep(3)
    if func_check:
        input('Продолжить --> Enter')


def main_loop() -> None:
    while True:
        # Генерация окружности
        x, y, r = ran(-100, 100), ran(-100, 100), ran(10, 100)
        # Генерация точки
        px, py = ran(-100, 100), ran(-100, 100)
        # Рисуем график
        draw((x, y, r), (px, py))


if __name__ == "__main__":
    main_loop()
