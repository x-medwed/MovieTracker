# main.py
import tkinter as tk
from app.db import database

def main():
    # создаём главное окно
    root = tk.Tk()
    root.title("Записник фільмів і серіалів")
    root.geometry("400x300")

    # базовая метка
    label = tk.Label(root, text="Вітаю у твоєму записнику!", font=("Arial", 14))
    label.pack(pady=20)

    # запускаем интерфейс
    root.mainloop()

if __name__ == "__main__":
    main()
