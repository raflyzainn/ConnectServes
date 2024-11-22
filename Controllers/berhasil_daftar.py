from flask import Blueprint, render_template

berhasil_daftar_bp = Blueprint('berhasil_daftar', __name__)

@berhasil_daftar_bp.route('/berhasil_daftar')
def berhasil_daftar():
    return render_template("berhasil_daftar.html")