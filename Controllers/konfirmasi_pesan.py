from flask import Blueprint, render_template, request, redirect, url_for, flash
import pymysql

konfirmasi_pesan_bp = Blueprint('konfirmasi_pesan', __name__)

@konfirmasi_pesan_bp.route('/konfirmasi_pesan', methods=['POST'])
def konfirmasi_pesan():
    # Ambil data dari form
    id_jasa = request.form.get('id_jasa')
    id_cust = request.form.get('id_cust')
    alamat = request.form.get('alamat')
    tanggal = request.form.get('tanggal')
    metode_pembayaran = request.form.get('metode_pembayaran')
    id_merch = request.form.get('id_merch')

    # Validasi input
    if not all([id_jasa, id_cust, alamat, tanggal, metode_pembayaran, id_merch]):
        flash("Semua field harus diisi.", "error")
        return redirect(url_for('homepage_customer.homepage_customer'))

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
            # Query untuk mendapatkan harga dari daftarjasa_merch berdasarkan id_jasa
            query = "SELECT harga FROM daftarjasa_merch WHERE id_jasa = %s"
            cursor.execute(query, (id_jasa,))
            result = cursor.fetchone()
        
            if result:
                harga = result['harga']
            else:
                flash("Jasa tidak ditemukan.", "error")
                return redirect(url_for('homepage_customer.homepage_customer'))
            
            # Query untuk menyimpan data ke tabel pesanjasa_cust
            query_insert = """
                INSERT INTO pesanjasa_cust 
                (id_jasa, id_cust, harga, alamat, tanggal_pemesanan, metode_pembayaran, id_merch)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            data = (id_jasa, id_cust, harga, alamat, tanggal, metode_pembayaran, id_merch)
            cursor.execute(query_insert, data)
            
            # Commit data
            connection.commit()

        flash("Pemesanan berhasil, silakan lanjut ke pembayaran.", "success")
        
        # Redirect ke halaman bayar_pesanan setelah menyimpan pemesanan
        return redirect(url_for('bayar_pesanan.bayar_pesanan', harga=harga, id_jasa=id_jasa))

    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
        return f"Error: {e}", 500
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Error: {e}", 500
    finally:
        if connection:
            connection.close()
