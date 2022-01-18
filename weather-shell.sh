#!/bin/bash
API="TEMP in Stockholm "$(curl -s "http://api.openweathermap.org/data/2.5/weather?q=Stockholm&units=metric&appid=aee454f3fe00a9f1f321d2b4376a4bd1" | jq '.main.temp')

sqlite3 weather.db "CREATE TABLE IF NOT EXISTS weather (
    weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
    temp TEXT,
    date DATE UNIQUE);"
sqlite3 weather.db "INSERT INTO weather (temp, date) VALUES ('$API', strftime('%Y-%m-%d','now'));"
sqlite3 weather.db "SELECT * FROM weather;"

# TESTING ONGOING
# sqlite3 /c/Users/src/Documents/python/weather-app/weather.db <<'END_SQL'
#     DROP TABLE weather;
#     CREATE TABLE IF NOT EXISTS weather (
#     weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     temp VARCHAR);
#     INSERT INTO weather (temp) VALUES ('$API');
#     SELECT * FROM weather;
# END_SQL
# sqlite3 weather.db "DROP TABLE weather;"
