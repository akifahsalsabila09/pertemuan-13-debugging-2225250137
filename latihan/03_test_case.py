
def cek_kelulusan(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


test_case = [
    (80, "Lulus"),
    (60, "Lulus"),
    (59, "Tidak lulus"),
    (0, "Tidak lulus"),
    (100, "Lulus")
]

for nomor, (nilai, harapan) in enumerate(test_case, start=1):
    hasil = cek_kelulusan(nilai)

    if hasil == harapan:
        status = "PASS"
    else:
        status = "FAIL"

    print(
        f"Test {nomor}: nilai={nilai}, "
        f"harapan={harapan}, hasil={hasil}, status={status}"
    )
