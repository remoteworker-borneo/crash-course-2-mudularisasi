"""
program menghitung alas segitiga
luas_segitiga = alas * tinggi / 2
"""
print('\nmenghitung luas segi tiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nmenghitung luas segitiga 2 dengan copy paste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')


print('\nmembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
     luas_segitiga = alas * tinggi / 2
     return luas_segitiga

alas = 10
tinggi = 6
print(f'dengan fungsi,  segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {hitung_luas_segitiga(alas, tinggi)}')
print(f'menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20, 2)}')
print(f'menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(100, 2)}')
