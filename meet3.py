# Program Python untuk mendemonstrasikan Inheritance (Pewarisan)
# Berdasarkan data Dosen dan Mahasiswa yang diberikan.

# 1. Kelas Dasar (Parent Class)
class CivitasAkademika:
    """
    Kelas dasar yang menyimpan atribut umum untuk semua
    anggota civitas akademika (Dosen dan Mahasiswa).
    """
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def perkenalan(self):
        return f"Nama: {self.nama}\nUsia: {self.usia}"

# 2. Kelas Turunan Pertama (Child Class) - Dosen
class Dosen(CivitasAkademika):
    """
    Kelas turunan dari CivitasAkademika untuk entitas Dosen.
    Menambahkan atribut spesifik: NIDN dan Mata Kuliah.
    """
    def __init__(self, nama, usia, nidn, mata_kuliah):
        # Memanggil konstruktor kelas dasar
        super().__init__(nama, usia)
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def mengajar(self):
        """Metode spesifik untuk Dosen."""
        return f"{self.nama} sedang mengajar {self.mata_kuliah}."

    def tampilkan_data(self):
        """Menampilkan semua data Dosen."""
        print("=== Data Dosen ===")
        print(self.perkenalan())
        print(f"NIDN: {self.nidn}")
        print(f"Mata Kuliah: {self.mata_kuliah}")
        print(self.mengajar())
        print("-" * 20)


# 3. Kelas Turunan Kedua (Child Class) - Mahasiswa
class Mahasiswa(CivitasAkademika):
    """
    Kelas turunan dari CivitasAkademika untuk entitas Mahasiswa.
    Menambahkan atribut spesifik: NIM dan Jurusan.
    """
    def __init__(self, nama, usia, nim, jurusan):
        # Memanggil konstruktor kelas dasar
        super().__init__(nama, usia)
        self.nim = nim
        self.jurusan = jurusan

    def belajar(self):
        """Metode spesifik untuk Mahasiswa."""
        return f"{self.nama} sedang belajar di Jurusan {self.jurusan}."

    def tampilkan_data(self):
        """Menampilkan semua data Mahasiswa."""
        print("=== Data Mahasiswa ===")
        print(self.perkenalan())
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(self.belajar())
        print("-" * 20)


# --- Implementasi Program ---

# Membuat objek Dosen
dosen1 = Dosen(
    nama="edy",
    usia=21,
    nidn="105663",
    mata_kuliah="Pemrograman Berorientasi Objek"
)

# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa(
    nama="Afrizan hidayat",
    usia=19,
    nim="24241188",
    jurusan="pendidikan teknologi informasi"
)

# Menampilkan data sesuai output di gambar
dosen1.tampilkan_data()
mahasiswa1.tampilkan_data()