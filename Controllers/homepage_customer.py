from flask import Blueprint, render_template
import mysql.connector
from mysql.connector import Error

homepage_customer_bp = Blueprint('homepage_customer', __name__)

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

@homepage_customer_bp.route('/homepage-customer')
def homepage_customer():
    connection = get_database_connection()
    services = []
    categories = set()  # Untuk menampung kategori unik
    locations = set()  # Untuk menampung lokasi unik
    
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM daftarjasa_merch")
            rows = cursor.fetchall()

            for row in rows:
                # Menambahkan jasa ke dalam list
                service = {
                    'id_jasa': int(row.get('id_jasa', 0)),
                    'nama': row.get('nama', ''),
                    'kategori': row.get('kategori', ''),
                    'harga': float(row.get('harga', 0.0)),
                    'lokasi': row.get('lokasi', ''),
                    'foto_jasa': row.get('foto_jasa', ''),
                    'deskripsi': row.get('deskripsi', ''),
                    'id_review': int(row.get('id_review', 0))
                }
                services.append(service)

                # Menambahkan kategori dan lokasi unik
                categories.add(row.get('kategori', ''))
                locations.add(row.get('lokasi', ''))
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    return render_template("homepage_customer.html", services=services, categories=categories, locations=locations)
