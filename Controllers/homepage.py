from flask import Blueprint, render_template
import mysql.connector
from mysql.connector import Error

homepage_bp = Blueprint('homepage', __name__)

def get_database_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='tubes_ippl',
            user='root',
            password=''
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@homepage_bp.route('/')
@homepage_bp.route('/homepage')
def homepage():
    connection = get_database_connection()
    services = []
    
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM daftarjasa_merch")
            services = cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    return render_template("homepage.html", services=services)