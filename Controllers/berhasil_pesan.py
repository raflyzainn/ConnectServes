from flask import Blueprint, request

berhasil_pesan_bp = Blueprint('berhasil_pesan', __name__)

@berhasil_pesan_bp.route('/berhasil_pesan', methods=['POST', 'GET'])  # Mendukung POST dan GET
def berhasil_pesan():
    if request.method == 'POST':
        # Ambil data dari form
        id_jasa = request.form.get('id_jasa')
        id_cust = request.form.get('id_cust')
        harga = request.form.get('harga')
        alamat = request.form.get('alamat')
        id_merch = request.form.get('id_merch')
        metode_pembayaran = request.form.get('metode_pembayaran')

        # Debugging
        print(f"Data POST diterima: id_jasa={id_jasa}, metode_pembayaran={metode_pembayaran}")

        return f"Pesanan berhasil untuk ID Jasa: {id_jasa}, dengan metode pembayaran: {metode_pembayaran}"
    return "Halaman Berhasil Pesan"
