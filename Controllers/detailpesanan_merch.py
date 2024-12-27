from flask import Blueprint, render_template

detailpesanan_merch_bp = Blueprint('detailpesanan_merch', __name__)

@detailpesanan_merch_bp.route('/detailpesanan_merch')
def profil():
    return render_template("detailpesanan_merch.html")