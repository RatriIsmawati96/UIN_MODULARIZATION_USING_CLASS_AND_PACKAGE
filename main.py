nama = 'Ratri Ismawati'
program = 'Mekanika Fluida'

print(f'program {program} oleh {nama}')

def hitung_tekanan(gaya, penampang):
    tekanan = gaya / penampang
    print(f'gaya = {gaya/1000}Newton dalam penampang = {penampang/10}m persegi')
    print(f'Sehingga tekanan = {tekanan} Newton')
    return tekanan

# tekanan = 1000
# penampang = 10 * 50
tekanan = hitung_tekanan(1000, 10 * 50)
tekanan = hitung_tekanan(200, 50 * 50)


def hitung_tekanan_hidrostatis(berat_jenis, jarak):
    tekanan_hidrostatis = berat_jenis * jarak
    print(f'berat jenis = {berat_jenis / 1000}N/m kubik dalam jarak = {jarak}meter')
    print(f'Sehinagga tekanan_hidrostatis = {tekanan_hidrostatis} N/m kubik')
    return tekanan_hidrostatis

# berat_jenis = 1000
# jarak = 5
kecepatan = hitung_tekanan_hidrostatis(1000, 5)
kecepatan = hitung_tekanan_hidrostatis(3000, 7)


def hitung_gaya_apung(massa_zat, gravitasi):
    gaya_apung = massa_zat * gravitasi
    print(f'massa_zat = {massa_zat / 200}N dalam gravitasi = {gravitasi / 10}m/s_persegi')
    print(f'Sehingga gaya_apung = {gaya_apung} N')
    return gaya_apung

# massa_zat = 200
# gravitasi = 10
kecepatan = hitung_gaya_apung(200, 10)
kecepatan = hitung_gaya_apung(400, 10)

