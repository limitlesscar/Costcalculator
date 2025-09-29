from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# PostgreSQL connection pool (better for production)
try:
    db_pool = psycopg2.pool.SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        sslmode=os.getenv("DB_SSL_MODE")
    )
    if db_pool:
        print("✅ PostgreSQL connection pool created successfully")
except Exception as e:
    print(f"❌ Failed to create PostgreSQL pool: {e}")
    db_pool = None

@app.route('/', methods=['GET'])
def home():
    message = ""
    if db_pool:
        try:
            conn = db_pool.getconn()
            if conn:
                db_pool.putconn(conn)
                message = "✅ Connection established!"
        except Exception as e:
            message = f"❌ Connection failed: {e}"
    else:
        message = "❌ No database connection pool available."
    return render_template('index.html', message=message)

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('terms.html')

@app.route('/help')
def help():
    return render_template('terms.html')

@app.route('/choose', methods=['POST'])
def choose():
    option = request.form.get('option')
    if option == 'template':
        return redirect(url_for('template_page'))
    else:
        return redirect(url_for('database_page'))

@app.route('/template')
def template_page():
    return render_template('template.html')

@app.route('/database')
def database_page():
    return render_template('database.html')

# Production-ready: listen on all interfaces, port from environment
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
