from flask import Blueprint, render_template

bantuan_penyedia_jasa_bp = Blueprint('bantuan_penyedia_jasa', __name__)

@bantuan_penyedia_jasa_bp.route('/bantuan_penyedia_jasa')
def bantuan_penyedia_jasa():
    return render_template("bantuan_penyedia_jasa.html")