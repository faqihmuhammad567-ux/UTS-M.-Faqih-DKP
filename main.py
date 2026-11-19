"""UTS Dasar Komputer dan Pemrograman - Kelompok D (Kontrol)
Monitoring Error terhadap Setpoint.
"""

SETPOINT = 50

# 15 data inti dari soal + 5 data tambahan (lihat README)
data_output = [
    50, 49, 47, 45, 43, 52, 54, 57, 51, 48, 46, 44, 53, 55, 42,  # 15 data inti
    51.9, 47.9, 54.9, 44.9, 62,                                  # 5 data tambahan
]

STABIL = "STABIL"
WARNING = "WARNING"
TIDAK_STABIL = "TIDAK STABIL"


def hitung_error(setpoint, output):
    """Mengembalikan error absolut = |setpoint - output|."""
    return abs(setpoint - output)


def status_error(error):
    """Mengembalikan status berdasarkan error absolut."""
    if error <= 2:
        return STABIL
    elif error <= 5:
        return WARNING
    else:
        return TIDAK_STABIL


def rata_rata(data_error):
    """Mengembalikan nilai rata-rata dari list error."""
    return sum(data_error) / len(data_error)


def hitung_kategori(data_status):
    """Mengembalikan jumlah data pada tiap status."""
    jumlah = {STABIL: 0, WARNING: 0, TIDAK_STABIL: 0}
    for status in data_status:
        jumlah[status] += 1
    return jumlah


def main():
    data_error = []
    data_status = []

    print("===== MONITORING ERROR TERHADAP SETPOINT =====")
    print(f"Setpoint = {SETPOINT}")
    print(f"{'No':<3} {'Output':>7} {'Error':>7}   Status")

    for nomor, output in enumerate(data_output, start=1):
        error = hitung_error(SETPOINT, output)
        status = status_error(error)
        data_error.append(error)
        data_status.append(status)
        print(f"{nomor:02d}  {output:>7} {error:>7.2f}   -> {status}")

    jumlah = hitung_kategori(data_status)

    print("\n===== RINGKASAN =====")
    print(f"Total data    : {len(data_output)}")
    print(f"STABIL        : {jumlah[STABIL]}")
    print(f"WARNING       : {jumlah[WARNING]}")
    print(f"TIDAK STABIL  : {jumlah[TIDAK_STABIL]}")
    print(f"Rata-rata error : {rata_rata(data_error):.2f}")
    print(f"Maksimum error  : {max(data_error):.2f}")
    print(f"Minimum error   : {min(data_error):.2f}")


if __name__ == "__main__":
    main()
