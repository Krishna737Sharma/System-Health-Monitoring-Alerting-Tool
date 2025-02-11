import sqlite3

def init_db():
    conn = sqlite3.connect('system_health.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS metadata
                 (id INTEGER PRIMARY KEY, name TEXT, environment TEXT, location TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS alerts
                 (id INTEGER PRIMARY KEY, metric_type TEXT, threshold REAL, status TEXT, timestamp DATETIME)''')
    conn.commit()
    conn.close()

def add_metadata(name, environment, location):
    conn = sqlite3.connect('system_health.db')
    c = conn.cursor()
    c.execute("INSERT INTO metadata (name, environment, location) VALUES (?, ?, ?)",
              (name, environment, location))
    conn.commit()
    conn.close()

def add_alert(metric_type, threshold, status):
    conn = sqlite3.connect('system_health.db')
    c = conn.cursor()
    c.execute("INSERT INTO alerts (metric_type, threshold, status, timestamp) VALUES (?, ?, ?, datetime('now'))",
              (metric_type, threshold, status))
    conn.commit()
    conn.close()