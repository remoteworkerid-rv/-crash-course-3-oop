from geometri.bangun_ruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('Menggunakan OOP')

p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s2 = Segitiga(4, 2)
print(s2.info())
print(s2.hitung_luas())

print('\nMencoba Membuat Objek')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

print('\nPolymorphism')
# Polymorphism adalah kemampuan suatu objek untuk merespon berbeda terhadap pemanggilan method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s2)

for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())



