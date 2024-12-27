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
            rows = cursor.fetchall()
            for row in rows:
                service = {
                    'id_jasa': int(row['id_jasa']) if row.get('id_jasa') is not None else 0,
                    'nama': row.get('nama', ''),
                    'kategori': row.get('kategori', ''),
                    'harga': float(row['harga']) if row.get('harga') is not None else 0.0,
                    'lokasi': row.get('lokasi', ''),
                    'foto_jasa': row.get('foto_jasa', ''),
                    'deskripsi': row.get('deskripsi', ''),
                    'id_review': int(row['id_review']) if row.get('id_review') is not None else 0
                }
                services.append(service)
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    return render_template("homepage.html", services=services)
