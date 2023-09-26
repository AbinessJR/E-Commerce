from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Connect to the database and retrieve data for the dashboard
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    # Execute SQL queries to fetch data for the dashboard

    # Close the database connection
    conn.close()

    # Render the dashboard template with data
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
