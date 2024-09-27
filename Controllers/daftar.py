from flask import Blueprint, render_template

daftar_bp = Blueprint('daftar', __name__)

@daftar_bp.route('/daftar')

def daftar():
    return render_template("daftar.html")