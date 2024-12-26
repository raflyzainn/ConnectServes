from flask import Blueprint, render_template, request
import pymysql

pesan_jasa_bp = Blueprint('pesan_jasa', __name__)

@pesan_jasa_bp.route('/pesan_jasa')
def pesan_jasa():
    # Ambil parameter ID dari URL
    id_jasa = request.args.get('id_jasa')
    print(f"Received id_jasa: {id_jasa}")  # Debugging
    
    # Koneksi ke database
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='tubes_ippl'
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Jika ada parameter ID, ambil data jasa berdasarkan ID
    if id_jasa:
        query = "SELECT * FROM daftarjasa_merch WHERE id_jasa = %s"
        cursor.execute(query, (id_jasa,))
        service = cursor.fetchone()
        print(f"Service data: {service}")  # Debugging
    else:
        service = None  # Jika tidak ada ID, set service menjadi None

    # Tutup koneksi ke database
    cursor.close()
    connection.close()

    # Render template dengan data 'service'
    return render_template("pesan_jasa.html", service=service)

