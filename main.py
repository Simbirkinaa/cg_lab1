import tkinter as tk
class TriangleDrawer:
    def __init__(self, canvas):
        # Этот конструктор инициализирует объект класса и принимает один аргумент - холст canvas.
        # Холст представляет собой область для рисования. Внутри конструктора устанавливаются
        # начальные значения для различных параметров:
        # self.canvas: Ссылка на холст, на котором будет отображаться треугольник.
        # self.x и self.y: Начальные координаты треугольника на холсте.
        # self.step: Шаг перемещения при нажатии клавиш управления.
        # self.triangle_patterns: Список образцов треугольников, представленных в виде координат линий.
        # self.pattern_index: Текущий индекс выбранного образца треугольника (начинается с первого образца).

        self.canvas = canvas
        self.x, self.y = 120, 150
        self.step = 10
        self.triangle_patterns = [
    [
        (0, 0, 50, 0),
        (0, 0, 25, -50),
        (50, 0, 25, -50)
    ],
    [
        (0, 0, 50, 0),
        (0, 0, -25, 50),
        (50, 0, -25, 50)
    ],
    [
        (0, 0, 50, 0),
        (0, 0, 25, 50),
        (50, 0, 25, 50)
    ],
    [
        (0, 0, 50, 0),
        (50, 0, 75, 50),
        (0, 0, 75, 50)
    ],
]
        self.pattern_index = 0
        self.draw_triangle()

    def draw_triangle(self):
        # Этот метод отвечает за отображение треугольника на холсте.
        # Сначала он удаляет все предыдущие элементы с тегом "triangle" с холста.
        # Затем для текущего выбранного образца треугольника, он создает линии на холсте, используя координаты
        # из образца. Эти линии представляют собой отрезки, которые образуют треугольник.
        # Цвет линий устанавливается как "black", а ширина линий - 2 пикселя.

        self.canvas.delete("triangle")
        for coords in self.triangle_patterns[self.pattern_index]:
            self.canvas.create_line(
                self.x + coords[0], self.y + coords[1], self.x + coords[2], self.y + coords[3],
                fill="black", width=2, tags="triangle"
            )

    def move_triangle(self, event):
        #Этот метод обрабатывает события перемещения треугольника в ответ на нажатия клавиш управления курсором
        # (вверх, вниз, влево, вправо).	В зависимости от нажатой клавиши, метод изменяет координаты треугольника
        # на холсте, добавляя или вычитая значение шага (self.step) к self.x или self.y.
        # После изменения координат вызывается метод draw_triangle() для обновления отображения треугольника.

        step = 10  # Шаг перемещения
        if event.keysym == "Right":
            self.x += step
        elif event.keysym == "Left":
            self.x -= step
        elif event.keysym == "Down":
            self.y += step
        elif event.keysym == "Up":
            self.y -= step
        self.draw_triangle()

    def change_pattern(self, event):
        # Этот метод обрабатывает событие смены образца треугольника при нажатии клавиши Enter.
        # Он увеличивает значение self.pattern_index на 1, переходя к следующему образцу в списке.
        # Если конец списка образцов достигнут, индекс обнуляется и выбирается первый образец.
        # После изменения образца вызывается метод draw_triangle() для его отображения.

        self.pattern_index = (self.pattern_index + 1) % len(self.triangle_patterns)
        self.draw_triangle()

    def exit_program(self, event):
        # Метод exit_program обрабатывает событие завершения работы приложения при нажатии клавиши Escape.
        # Он вызывает метод root.quit(), который завершает выполнение программы.
        if event.keysym == "Escape":
            root.quit()

root = tk.Tk()
root.title("Управление треугольником")
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
triangle_drawer = TriangleDrawer(canvas)

# <Right>, <Left>, <Down>, <Up>:
# Эти строки устанавливают обработчики для клавиш управления курсором (вправо, влево, вниз, вверх).
# Когда пользователь нажимает одну из этих клавиш, вызывается метод move_triangle,
# который отвечает за перемещение треугольника в соответствующем направлении.


# <Return> устанавливает обработчик для клавиши Enter.
# При нажатии клавиши Enter вызывается метод change_pattern, который отвечает за смену образца треугольника.
# <Escape> устанавливает обработчик для клавиши Escape.
# Когда пользователь нажимает клавишу Escape, вызывается метод exit_program, который завершает работу программы.
root.bind("<Right>", triangle_drawer.move_triangle)
root.bind("<Left>", triangle_drawer.move_triangle)
root.bind("<Down>", triangle_drawer.move_triangle)
root.bind("<Up>", triangle_drawer.move_triangle)
root.bind("<Return>", triangle_drawer.change_pattern)
root.bind("<Escape>", triangle_drawer.exit_program)

root.mainloop()