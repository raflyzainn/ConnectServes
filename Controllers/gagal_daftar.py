from flask import Blueprint, render_template

gagal_daftar_bp = Blueprint('gagal_daftar', __name__)

@gagal_daftar_bp.route('/gagal_daftar')
def gagal_daftar():
    return render_template("gagal_daftar.html")