from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="PASSORD123",
        database="server_monitor"
        )
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM system_status ORDER BY created_at DESC")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route("/")
def index():
    data = get_data()
    return render_template("index.html", data=data)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
