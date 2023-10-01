import unittest
import tkinter as tk
from tkinter import Canvas
from main import TriangleDrawer

class TestTriangleDrawer(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.canvas = Canvas(self.root, width=300, height=300)
        self.canvas.pack()
        self.triangle_drawer = TriangleDrawer(self.canvas)

    def test_initial_triangle_pattern(self):
        # Проверка, что начальный образец треугольника отображается правильно
        objects_on_canvas = self.canvas.find_all()
        self.assertTrue(len(objects_on_canvas) > 0, "На холсте нет объектов")

    def test_move_triangle(self):
        # Проверка перемещения треугольника вправо
        initial_x = self.triangle_drawer.x
        event = tk.Event()
        event.keysym = "Right"
        self.triangle_drawer.move_triangle(event)
        expected_x = initial_x + self.triangle_drawer.step
        self.assertEqual(self.triangle_drawer.x, expected_x, "Координата x изменилась неправильно")

    def test_change_pattern(self):
        # Проверка изменения образца
        initial_pattern_index = self.triangle_drawer.pattern_index
        event = tk.Event()
        self.triangle_drawer.change_pattern(event)
        expected_pattern_index = (initial_pattern_index + 1) % len(self.triangle_drawer.triangle_patterns)
        self.assertEqual(self.triangle_drawer.pattern_index, expected_pattern_index, "Индекс образца изменился неправильно")

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
