
def baca_nilai(nama_file):
    file = open(nama_file, "r")
    nilai = []

    for baris in file:
        nilai.append(int(baris))

    file.close()
    return nilai


print(baca_nilai("kasus/nilai.txt"))
