import sqlite3

conn = sqlite3.connect("shop.db")
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()

for (name,) in tables:
    columns = [row[1] for row in conn.execute(f'PRAGMA table_info("{name}")')]
    print(f"{name}: {columns}")

conn.close()