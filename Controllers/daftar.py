from flask import Blueprint, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

daftar_bp = Blueprint('daftar', __name__)

# Konfigurasi database
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
        # Ambil data dari form
        nama = request.form['nama']
        email = request.form['email']
        password = request.form['password']
        nomorhp = request.form['nomorhp']
        peran = 1 if request.form['peran'] == 'pelanggan' else 0  
        ava_pengguna = request.form.get('ava_pengguna', None)  # Optional, bisa diisi jika ada gambar profil

        # Buat koneksi database
        connection = create_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                
                # Query untuk memasukkan data pengguna
                query = """
                INSERT INTO pengguna
                (email, no_hp, nama, kata_sandi, peran_pengguna, ava_pengguna) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                values = (email, nomorhp, nama, password, peran, ava_pengguna)
                
                cursor.execute(query, values)
                connection.commit()
                
                # Tutup koneksi
                cursor.close()
                connection.close()
                
                flash("Registration successful!", "success")
                return redirect(url_for('homepage.homepage'))  
                
            except Error as e:
                print(f"Error: {e}")
                flash("Registration failed. Please try again.", "danger")
                return redirect(url_for('daftar.daftar'))
        else:
            flash("Database connection failed.", "danger")
            return redirect(url_for('daftar.daftar'))
                
    return render_template("daftar.html")
