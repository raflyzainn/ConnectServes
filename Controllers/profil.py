from flask import Blueprint, render_template, request, redirect, url_for, flash
import pymysql

profil_bp = Blueprint('profil', __name__)

@profil_bp.route('/profil', methods=['GET', 'POST'])
def profil():
    if request.method == 'POST':
        # Ambil data dari form
        owner_name = request.form.get('owner_name')
        nik = request.form.get('nik')
        email = request.form.get('email')
        location = request.form.get('location')

        # Validasi data
        if not all([owner_name, nik, email, location]):
            flash("Semua field wajib diisi.", "error")
            return redirect(url_for('profil.profil'))

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
                # Simpan data ke tabel user_merch
                query = """
                    INSERT INTO user_merch_copy (email_merch, nama_ktp, nik, lokasi, foto_ktp)
                    VALUES (%s, %s, %s, %s, NULL)
                """
                cursor.execute(query, (email, owner_name, nik, location))
                connection.commit()

            flash("Data berhasil disimpan!", "success")
            return redirect(url_for('profil.profil'))
        except pymysql.MySQLError as e:
            flash(f"Database error: {e}", "error")
            return redirect(url_for('profil.profil'))
        finally:
            if connection:
                connection.close()

    return render_template("profil.html")
