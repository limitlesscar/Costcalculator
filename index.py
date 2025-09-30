from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    message = ""
    try:
        # Test PostgreSQL connection
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            sslmode=os.getenv("DB_SSL_MODE")
        )
        conn.close()
        message = "✅ Connection established!"
    except Exception as e:
        message = f"❌ Connection failed: {e}"
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

if __name__ == '__main__':
    # Only run the Flask development server locally
    app.run(debug=True, host='0.0.0.0', port=1000)
