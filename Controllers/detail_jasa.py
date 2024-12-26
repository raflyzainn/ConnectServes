from flask import Blueprint, render_template, request
import pymysql

detail_jasa_bp = Blueprint('detail_jasa', __name__)

@detail_jasa_bp.route('/detail_jasa/<int:service_id>')
def detail_jasa(service_id):
    # Koneksi ke database
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='tubes_ippl'
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Query untuk mengambil data berdasarkan id_jasa
    query = "SELECT * FROM daftarjasa_merch WHERE id_jasa = %s"
    cursor.execute(query, (service_id,))
    service = cursor.fetchone()

    # Tutup koneksi ke database
    cursor.close()
    connection.close()

    # Render template dengan data 'service'
    return render_template("detail_jasa.html", service=service)
