from flask import Blueprint, render_template, request

# Blueprint untuk bayar_pesanan
bayar_pesanan_bp = Blueprint('bayar_pesanan', __name__)

@bayar_pesanan_bp.route('/bayar_pesanan', methods=['GET'])
def bayar_pesanan():
    # Ambil harga dan id_jasa dari query string
    harga = request.args.get('harga')
    id_jasa = request.args.get('id_jasa')

    if not harga or not id_jasa:
        return "Error: Harga atau ID Jasa tidak ditemukan", 400

    # Render halaman bayar_pesanan dengan harga dan id_jasa
    return render_template("bayar_pesanan.html", harga=harga, id_jasa=id_jasa)
