
def hitung_total(daftar_harga):
    total = 0

    for harga in daftar_harga:
        total = total + harga

    return total


harga_barang = [10000, 15000, 20000]
hasil = hitung_total(harga_barang)

print("Daftar harga:", harga_barang)
print("Total belanja:", hasil)
