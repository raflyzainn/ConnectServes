from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import mysql.connector
from mysql.connector import Error

masuk_bp = Blueprint('masuk', __name__)

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

@masuk_bp.route('/masuk', methods=['GET', 'POST'])
def masuk():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        connection = create_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                
                # Sesuaikan query dengan tabel pengguna
                query = """
                SELECT * FROM pengguna 
                WHERE email = %s AND kata_sandi = %s
                """
                cursor.execute(query, (email, password))
                user = cursor.fetchone()
                
                cursor.close()
                connection.close()
                
                if user:
                    # Set session data
                    session['logged_in'] = True
                    session['user_email'] = user['email']
                    session['user_name'] = user['nama']
                    session['user_role'] = user['peran_pengguna']
                    
                    # Debug: Print peran_pengguna ke console
                    print("Peran Pengguna:", user['peran_pengguna'])

                    # Redirect berdasarkan peran pengguna
                    if user['peran_pengguna'] == 0:
                        print("Redirecting to homepage_merchant")  # Debug statement
                        return redirect(url_for('homepage_merchant.homepage_merchant')) 
                    else:
                        print("Redirecting to homepage_customer")  # Debug statement
                        return redirect(url_for('homepage_customer.homepage_customer'))  
                else:
                    flash('Email atau kata sandi salah. Silakan coba lagi.', 'error')
                    return redirect(url_for('masuk.masuk'))
                    
            except Error as e:
                print(f"Error: {e}")
                flash('Terjadi kesalahan. Silakan coba lagi.', 'error')
                return redirect(url_for('masuk.masuk'))
    
    return render_template("masuk.html")
