import sqlite3


class weather_cloud:

    def __init__(self):

        self.conn = sqlite3.connect('weatherdb.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # self.c.execute("""DROP TABLE weather_history""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS weather_history (
            weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
            condition TEXT,
            temp TEXT,
            maxTemp TEXT,
            minTemp TEXT,
            windSpeed TEXT,
            sunrise TEXT,
            sundown TEXT,
            date DATE UNIQUE
            )""")
        self.conn.commit()

    def insert_data(self, finalInfo):
        self.c.execute("""INSERT INTO weather_history VALUES
        (NULL,?,?,?,?,?,?,?,?)""", finalInfo)
        self.conn.commit()

    def show_all(self):
        self.c.execute("SELECT * FROM weather_history")
        items = self.c.fetchall()

        for item in items:
            print(item)
        self.conn.commit()
