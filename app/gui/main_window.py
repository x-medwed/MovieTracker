import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Записник фільмів / серіалів")
        self.geometry("900x600")

        # Верхняя панель вкладок
        tabs = ttk.Notebook(self)
        self.frames = {}

        for name in ["Заплановано", "Дивлюсь", "Переглянуто", "Відкладено", "Кинуто"]:
            frame = ttk.Frame(tabs)
            tabs.add(frame, text=name)
            self.frames[name] = frame

        tabs.pack(expand=True, fill="both")
