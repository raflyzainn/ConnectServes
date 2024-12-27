from flask import Blueprint, render_template, request, redirect, url_for, flash
import pymysql

tambahjasa_merch_bp = Blueprint('tambahjasa_merch', __name__)

@tambahjasa_merch_bp.route('/tambahjasa_merch', methods=['GET', 'POST'])
def tambahjasa_merch():
    if request.method == 'POST':
        # Ambil data dari form
        nama = request.form.get('nama')
        harga = request.form.get('harga')
        kategori = request.form.get('kategori')
        lokasi = request.form.get('lokasi')
        email_merch = request.form.get('email_merch')
        deskripsi = request.form.get('deskripsi')

        # Validasi data wajib
        if not all([nama, harga, kategori, lokasi, email_merch, deskripsi]):
            flash("Semua field wajib diisi.", "error")
            return redirect(url_for('tambahjasa_merch.tambahjasa_merch'))

        # Simpan data ke database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='tubes_ippl',
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                # Query untuk menyimpan data tanpa id_merch
                query = """
                    INSERT INTO daftarjasa_merch 
                    (id_jasa, email_merch, nama, kategori, harga, lokasi, deskripsi, id_review)
                    VALUES (NULL, %s, %s, %s, %s, %s, %s, 1)
                """
                cursor.execute(query, (email_merch, nama, kategori, harga, lokasi, deskripsi))
                connection.commit()
                flash("Data jasa berhasil ditambahkan.", "success")
        finally:
            connection.close()

        return redirect(url_for('tambahjasa_merch.tambahjasa_merch'))

    return render_template("tambahjasa_merch.html")
