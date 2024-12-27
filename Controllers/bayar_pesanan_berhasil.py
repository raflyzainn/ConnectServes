from flask import Blueprint, render_template

# Blueprint untuk bayar_pesanan_berhasil
bayar_pesanan_berhasil_bp = Blueprint('bayar_pesanan_berhasil', __name__)

@bayar_pesanan_berhasil_bp.route('/bayar_pesanan_berhasil', methods=['GET'])
def bayar_pesanan_berhasil():
    return render_template("bayar_pesanan_berhasil.html") 