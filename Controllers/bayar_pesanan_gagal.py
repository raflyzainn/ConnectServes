from flask import Blueprint, render_template

# Blueprint untuk bayar_pesanan_gagal
bayar_pesanan_gagal_bp = Blueprint('bayar_pesanan_gagal', __name__)

@bayar_pesanan_gagal_bp.route('/bayar_pesanan_gagal', methods=['GET'])
def bayar_pesanan_gagal():
    return render_template("bayar_pesanan_gagal.html") 