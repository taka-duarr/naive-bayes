
data = [
    {"Pola Tidur": "Buruk", "Jenis Kelamin": "Laki-laki", "Aktivitas Fisik": "Tinggi", "Pola Makan": "Buruk", "Obesitas": "Ya"},
    {"Pola Tidur": "Buruk", "Jenis Kelamin": "Laki-laki", "Aktivitas Fisik": "Rendah", "Pola Makan": "Buruk", "Obesitas": "Ya"},
    {"Pola Tidur": "Buruk", "Jenis Kelamin": "Perempuan", "Aktivitas Fisik": "Rendah", "Pola Makan": "Baik", "Obesitas": "Tidak"},
    {"Pola Tidur": "Cukup", "Jenis Kelamin": "Laki-laki", "Aktivitas Fisik": "Tinggi", "Pola Makan": "Baik", "Obesitas": "Tidak"},
    {"Pola Tidur": "Cukup", "Jenis Kelamin": "Perempuan", "Aktivitas Fisik": "Tinggi", "Pola Makan": "Baik", "Obesitas": "Tidak"}
]


# Menghitung prior untuk kelas Obesitas
prior_obesitas_ya = len([baris for baris in data if baris['Obesitas'] == 'Ya']) / len(data)
prior_obesitas_tidak = len([baris for baris in data if baris['Obesitas'] == 'Tidak']) / len(data)

# Menghitung probabilitas likelihood untuk setiap fitur
def hitungProbabilitasLikelihood(data, kelas, atribut, nilai):
    jumlahKelas = len([baris for baris in data if baris['Obesitas'] == kelas])
    if jumlahKelas == 0:
        return 0
    jumlahAtributKelas = len([baris for baris in data if baris[atribut] == nilai and baris['Obesitas'] == kelas])
    return jumlahAtributKelas / jumlahKelas

# Menghitung probabilitas untuk setiap kelas (Obesitas Ya/Tidak)
def hitungProbabilitasKelas(data, dataInput):
    probabilitasYa = prior_obesitas_ya
    probabilitasTidak = prior_obesitas_tidak
    for atribut, nilai in dataInput.items():
        probabilitasYa *= hitungProbabilitasLikelihood(data, 'Ya', atribut, nilai)
        probabilitasTidak *= hitungProbabilitasLikelihood(data, 'Tidak', atribut, nilai)
    return {'Ya': probabilitasYa, 'Tidak': probabilitasTidak}

# Fungsi untuk melakukan prediksi
def prediksi(data, dataInput):
    probabilitas = hitungProbabilitasKelas(data, dataInput)
    if probabilitas['Ya'] > probabilitas['Tidak']:
        return 'Ya'
    else:
        return 'Tidak'

# Input data dari pengguna
dataBaru = {}
dataBaru['Pola Tidur'] = input('Masukkan Pola Tidur (Buruk/Cukup): ')
dataBaru['Jenis Kelamin'] = input('Masukkan Jenis Kelamin (Laki-laki/Perempuan): ')
dataBaru['Aktivitas Fisik'] = input('Masukkan Aktivitas Fisik (Rendah/Tinggi): ')
dataBaru['Pola Makan'] = input('Masukkan Pola Makan (Buruk/Baik): ')

# Prediksi berdasarkan data input
hasilPrediksi = prediksi(data, dataBaru)
nilaiPrediksi = hitungProbabilitasKelas(data, dataBaru)

# Menampilkan hasil prediksi
print(f"Prediksi Obesitas: {hasilPrediksi}")
print(f"Nilai Prediksi: {nilaiPrediksi}")