from flask import Blueprint, render_template

profil_bp = Blueprint('profil', __name__)

@profil_bp.route('/profil')
def profil():
    return render_template("profil.html")