from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import mysql.connector
from mysql.connector import Error

masuk_bp = Blueprint('masuk', __name__)

# Database configuration
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
                
                query = """
                SELECT * FROM registrasi_akun 
                WHERE email_akun = %s AND sandi_akun = %s
                """
                cursor.execute(query, (email, password))
                user = cursor.fetchone()
                
                cursor.close()
                connection.close()
                
                if user:
                    session['logged_in'] = True
                    session['user_email'] = user['email_akun']
                    session['user_name'] = user['nama_akun']
                    session['user_role'] = user['peran_pengguna']
                    
                    if user['peran_pengguna'] == 1:
                        return redirect(url_for('homepage_customer.homepage_customer'))  
                    else:
                        return redirect(url_for('penyedia_dashboard'))  
                else:
                    flash('Email atau kata sandi salah. Silakan coba lagi.', 'error')
                    return redirect(url_for('masuk.masuk'))
                    
            except Error as e:
                print(f"Error: {e}")
                flash('Terjadi kesalahan. Silakan coba lagi.', 'error')
                return redirect(url_for('masuk.masuk'))
    
    return render_template("masuk.html")