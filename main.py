import tkinter as tk

class TriangleDrawer:
    def __init__(self, canvas):
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
        self.canvas.delete("triangle")
        for coords in self.triangle_patterns[self.pattern_index]:
            self.canvas.create_line(
                self.x + coords[0], self.y + coords[1], self.x + coords[2], self.y + coords[3],
                fill="black", width=2, tags="triangle"
            )

    def move_triangle(self, event):
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
        self.pattern_index = (self.pattern_index + 1) % len(self.triangle_patterns)
        self.draw_triangle()

    def exit_program(self, event):
        if event.keysym == "Escape":
            root.quit()

root = tk.Tk()
root.title("Управление треугольником")
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

triangle_drawer = TriangleDrawer(canvas)

root.bind("<Right>", triangle_drawer.move_triangle)
root.bind("<Left>", triangle_drawer.move_triangle)
root.bind("<Down>", triangle_drawer.move_triangle)
root.bind("<Up>", triangle_drawer.move_triangle)
root.bind("<Return>", triangle_drawer.change_pattern)
root.bind("<Escape>", triangle_drawer.exit_program)

root.mainloop()