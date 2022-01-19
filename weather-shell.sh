#!/bin/bash
API=$(curl -s "http://api.openweathermap.org/data/2.5/weather?q=Stockholm&units=metric&appid=aee454f3fe00a9f1f321d2b4376a4bd1")
TEMPERATURE=$(echo $API | jq '.main.temp')
LOCATION=$(echo $API | jq -r '.name')
echo "TEMP in $LOCATION is $TEMPERATURE"

# TESTING ONGOING
sqlite3 weather.db <<SQL
    CREATE TABLE IF NOT EXISTS reports (
    weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
    temp VARCHAR NOT NULL,
    location TEXT NOT NULL,
    date DATE UNIQUE);
    INSERT INTO reports (temp, location, date) VALUES ($TEMPERATURE, '$LOCATION', strftime('%Y-%m-%d','now'));
    SELECT * FROM reports;
SQL

# sqlite3 weather.db "DROP TABLE weather;"
# DROP TABLE weather;

# sqlite3 weather.db "DROP TABLE weather;"
# sqlite3 weather.db "CREATE TABLE IF NOT EXISTS weather (
#     weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     temp TEXT,
#     date DATE UNIQUE);"
# sqlite3 weather.db "INSERT INTO weather (temp, date) VALUES ('$API', strftime('%Y-%m-%d','now'));"
# sqlite3 weather.db "SELECT * FROM weather;"
