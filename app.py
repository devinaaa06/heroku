from flask import Flask, request, jsonify
import random

app = Flask(__name__)

pesan_default = [
    "Makan patty itu SpongeBob.",
    "Berdansalah, Patrick.",
    # Tambahkan pesan-pesan default lainnya di sini
]

@app.route('/')
def home():
    return 'Selamat datang di halaman utama!'

@app.route('/puja-kerang-ajaib', methods=['GET', 'POST'])
def puja_kerang_ajaib():
    if request.method == 'GET':
        nama = request.args.get('nama')
        if nama:
            pesan = f"{nama}, {random.choice(pesan_default)}"
        else:
            pesan = random.choice(pesan_default)
        return jsonify({'pesan': pesan})
    elif request.method == 'POST':
        nama = request.form.get('nama')
        if nama:
            pesan = f"Selamat datang, {nama}, anda berhasil masuk ke Puja Kerang Ajaib"
            return jsonify({'pesan': pesan})
        else:
            return jsonify({'pesan': 'Parameter "nama" tidak ditemukan'})

if __name__ == '_main_':
    app.run(debug=True)