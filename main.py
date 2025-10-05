from app.db.database import init_db
from app.gui.main_window import MainWindow

if __name__ == "__main__":
    init_db()
    app = MainWindow()
    app.mainloop()
