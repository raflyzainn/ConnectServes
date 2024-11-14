from flask import Blueprint, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

daftar_bp = Blueprint('daftar', __name__)

db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': '',  
    'database': 'tubes_ippl'
}

def create_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@daftar_bp.route('/daftar', methods=['GET', 'POST'])
def daftar():
    if request.method == 'POST':
        # Get form data
        nama = request.form['nama']
        email = request.form['email']
        password = request.form['password']
        nomorhp = request.form['nomorhp']
        peran = 1 if request.form['peran'] == 'pelanggan' else 0  

        connection = create_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                
                query = """
                INSERT INTO registrasi_akun 
                (nama_akun, email_akun, sandi_akun, nomorhp_akun, peran_pengguna) 
                VALUES (%s, %s, %s, %s, %s)
                """
                values = (nama, email, password, nomorhp, peran)
                
                cursor.execute(query, values)
                connection.commit()
                
                cursor.close()
                connection.close()
                
                return redirect(url_for('homepage.homepage'))  
                
            except Error as e:
                print(f"Error: {e}")
                return "Registration failed. Please try again."
                
    return render_template("daftar.html")