import sqlite3
from pathlib import Path

DB_PATH = Path("data/movies.db")

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        year INTEGER,
        genre TEXT,
        status TEXT,  -- Заплановано / Дивлюсь / Переглянуто / Відкладено / Кинуто
        episodes_total INTEGER,
        episodes_watched INTEGER,
        description TEXT,
        image_path TEXT
    )
    """)

    conn.commit()
    conn.close()
