import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎬 Записник фільмів / серіалів")
        self.geometry("1000x600")
        self.configure(bg="#1e1e1e")  # темная тема по умолчанию

        self.theme = "dark"  # текущая тема

        # Создаем верхнюю панель
        self.create_header()

        # Основная зона контента
        self.content_frame = tk.Frame(self, bg=self["bg"])
        self.content_frame.pack(fill="both", expand=True)

    # ──────────────────────────────────────────────
    def create_header(self):
        header = tk.Frame(self, bg="#2d2d2d", height=60)
        header.pack(fill="x", side="top")

        # Сетка для выравнивания: 3 колонки
        header.columnconfigure(0, weight=1)
        header.columnconfigure(1, weight=3)
        header.columnconfigure(2, weight=1)

        # ───── Логотип ─────
        logo = tk.Label(header, text="🎬", bg="#2d2d2d", fg="white", font=("Arial", 18, "bold"))
        logo.grid(row=0, column=0, sticky="w", padx=20)

        # ───── Центральная панель вкладок ─────
        tab_frame = tk.Frame(header, bg="#2d2d2d")
        tab_frame.grid(row=0, column=1)

        tabs = ["Заплановано", "Дивлюсь", "Переглянуто", "Відкладено", "Кинуто"]
        self.tab_buttons = []

        for tab in tabs:
            btn = tk.Button(
                tab_frame,
                text=tab,
                bg="#3a3a3a",
                fg="white",
                activebackground="#0078D7",
                relief="flat",
                font=("Arial", 11, "bold"),
                padx=10,
                pady=5,
                command=lambda t=tab: self.switch_tab(t)
            )
            btn.pack(side="left", padx=5)
            self.tab_buttons.append(btn)

        # ───── Правая часть ─────
        right_frame = tk.Frame(header, bg="#2d2d2d")
        right_frame.grid(row=0, column=2, sticky="e", padx=20)

        # Переключатель темы
        self.theme_button = tk.Button(
            right_frame, text="🌙", bg="#2d2d2d", fg="white",
            font=("Arial", 14), relief="flat", command=self.toggle_theme
        )
        self.theme_button.pack(side="left", padx=5)

        # Кнопка меню (⚙️)
        self.menu_button = tk.Button(
            right_frame, text="⚙️", bg="#2d2d2d", fg="white",
            font=("Arial", 14), relief="flat", command=self.open_settings
        )
        self.menu_button.pack(side="left", padx=5)

    # ──────────────────────────────────────────────
    def switch_tab(self, tab_name):
        # Здесь позже будет логика смены контента
        print(f"Вкладка: {tab_name}")

    # ──────────────────────────────────────────────
    def toggle_theme(self):
        if self.theme == "dark":
            self.theme = "light"
            self.configure(bg="#f0f0f0")
            self.theme_button.config(text="🌞")
        else:
            self.theme = "dark"
            self.configure(bg="#1e1e1e")
            self.theme_button.config(text="🌙")

    # ──────────────────────────────────────────────
    def open_settings(self):
        win = tk.Toplevel(self)
        win.title("Налаштування")
        win.geometry("300x200")
        tk.Label(win, text="Тут будуть налаштування", font=("Arial", 12)).pack(pady=40)
