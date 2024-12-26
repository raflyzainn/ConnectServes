from flask import Blueprint, render_template, request, redirect, url_for
import pymysql

konfirmasi_pesan_bp = Blueprint('konfirmasi_pesan', __name__)

@konfirmasi_pesan_bp.route('/konfirmasi_pesan', methods=['POST'])
def konfirmasi_pesan():
    # Ambil data dari form
    id_jasa = request.form.get('id_jasa')
    id_cust = request.form.get('id_cust')
    harga = request.form.get('harga')
    alamat = request.form.get('alamat')
    tanggal = request.form.get('tanggal')
    metode_pembayaran = request.form.get('metode_pembayaran')
    id_merch = request.form.get('id_merch')

    # Validasi input
    if not all([id_jasa, id_cust, harga, alamat, tanggal, metode_pembayaran, id_merch]):
        return "Error: All fields are required", 400

    try:
        # Koneksi ke database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='tubes_ippl',
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            # Query untuk menyimpan data ke tabel pesanjasa_cust
            query = """
                INSERT INTO pesanjasa_cust 
                (id_jasa, id_cust, harga, alamat, tanggal_pemesanan, metode_pembayaran, id_merch)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            data = (id_jasa, id_cust, harga, alamat, tanggal, metode_pembayaran, id_merch)
            cursor.execute(query, data)
            connection.commit()

        return redirect(url_for('homepage_customer.homepage_customer'))  # Redirect ke halaman sukses (buat halaman success_page)
    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
        return f"Error: {e}", 500
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Error: {e}", 500
