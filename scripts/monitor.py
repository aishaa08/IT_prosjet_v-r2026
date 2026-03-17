import psutil
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PASSORD123",
    database="server_monitor"
)

cursor = conn.cursor()

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent

sql = "INSERT INTO system_status (cpu, ram) VALUES (%s, %s)"
cursor.execute(sql, (cpu, ram))

conn.commit()
conn.close()

print("Data lagret i databasen")
print("CPU:", cpu)
print("RAM:",ram)
