import tkinter as tk

# Глобальные переменные для хранения координат и образца треугольника
x, y = 120, 150
triangle_patterns = [
    [
        (0, 0, 50, 0),   # основание снизу
        (0, 0, 25, -50),  # левая сторона
        (50, 0, 25, -50)  # правая сторона
    ],
[
        (0, 0, 50, 0),   # основание вверху
        (0, 0, -25, 50),  # левая сторона
        (50, 0, -25, 50)  # правая сторона
    ],
    [
        (0, 0, 50, 0),   # основание
        (0, 0, 25, 50),  # левая сторона
        (50, 0, 25, 50)  # правая сторона
    ],
    [
        (0, 0, 50, 0),  # верхнее основание
        (50, 0, 75, 50),   # правая сторона
        (0, 0, 75, 50)  # левая сторона
    ],
]
pattern_index = 0

# Функция для отображения треугольника
def draw_triangle():
    canvas.delete("triangle")
    for coords in triangle_patterns[pattern_index]:
        canvas.create_line(
            x + coords[0], y + coords[1], x + coords[2], y + coords[3],
            fill="black", width=2, tags="triangle"
        )

# Функция для перемещения треугольника
def move_triangle(event):
    global x, y
    step = 10  # Шаг перемещения
    if event.keysym == "Right":
        x += step
    elif event.keysym == "Left":
        x -= step
    elif event.keysym == "Down":
        y += step
    elif event.keysym == "Up":
        y -= step
    draw_triangle()

# Изменение образца треугольника
def change_pattern(event):
    global pattern_index
    pattern_index = (pattern_index + 1) % len(triangle_patterns)
    draw_triangle()

# Выход из программы
def exit_program(event):
    if event.keysym == "Escape":
        root.quit()

# Создание основного окна
root = tk.Tk()
root.title("Управление треугольником")

# Создание поля для отображения треугольника
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Назначение обработчиков событий клавиш корневому окну
root.bind("<Right>", move_triangle)
root.bind("<Left>", move_triangle)
root.bind("<Down>", move_triangle)
root.bind("<Up>", move_triangle)
root.bind("<Return>", change_pattern)
root.bind("<Escape>", exit_program)

# Отображение первого образца
draw_triangle()

root.mainloop()
