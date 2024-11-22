from flask import Blueprint, render_template

berhasil_masuk_bp = Blueprint('berhasil_masuk', __name__)

@berhasil_masuk_bp.route('/berhasil_masuk')
def berhasil_masuk():
    return render_template("berhasil_masuk.html")