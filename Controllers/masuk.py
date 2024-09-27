from flask import Blueprint, render_template

masuk_bp = Blueprint('masuk', __name__)

@masuk_bp.route('/masuk')

def masuk():
    return render_template("masuk.html")