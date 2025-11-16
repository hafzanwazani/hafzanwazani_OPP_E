class MahasiswaAlumni:
    def __init__(self, nama, tahun_lulus=None):
        self.nama = nama
        self.tahun_lulus = tahun_lulus if tahun_lulus is not None else 0

    def info_alumni(self):
        print("=== Data Alumni ===")
        print(f"Nama: {self.nama}")
        print(f"Tahun Lulus: {self.tahun_lulus}")
        print("===================")


class MahasiswaAktif:
    def __init__(self, nama, nim=None, jurusan=None):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def info_aktif(self):
        print("=== Data Mahasiswa Aktif ===")
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim if self.nim is not None else '-'}")
        print(f"Jurusan: {self.jurusan if self.jurusan is not None else '-'}")
        print("============================")


class Mahasiswa(MahasiswaAlumni, MahasiswaAktif):
    def __init__(self, nama, nim=None, jurusan=None, tahun_lulus=0):
        MahasiswaAlumni.__init__(self, nama, tahun_lulus=tahun_lulus)
        MahasiswaAktif.__init__(self, nama, nim=nim, jurusan=jurusan)

    def tampilkan_info(self):
        print("=== Informasi Mahasiswa ===")
        if getattr(self, "tahun_lulus", 0) > 0:
            self.info_alumni()
        else:
            self.info_aktif()
        print("============================")


class KTM(Mahasiswa):
    def tampilkan_ktm(self):
        if getattr(self, "nim", None):
            print(f"KTM Mahasiswa: {self.nama} - {self.nim}")
        else:
            print(f"{self.nama} tidak memiliki KTM (sudah alumni).")


class Ijazah(Mahasiswa):
    def tampilkan_ijazah(self):
        if getattr(self, "tahun_lulus", 0) > 0:
            print(f"Ijazah atas nama {self.nama}, Lulus tahun {self.tahun_lulus}")
        else:
            print(f"{self.nama} belum lulus, ijazah belum tersedia.")


class Beasiswa(Mahasiswa):
    def __init__(self, nama, nim=None, jurusan=None, tahun_lulus=0, jenis_beasiswa=None):
        super().__init__(nama, nim=nim, jurusan=jurusan, tahun_lulus=tahun_lulus)
        self.jenis_beasiswa = jenis_beasiswa

    def tampilkan_beasiswa(self):
        if getattr(self, "tahun_lulus", 0) == 0 and self.jenis_beasiswa:
            print(f"{self.nama} menerima beasiswa {self.jenis_beasiswa}")
        elif getattr(self, "tahun_lulus", 0) > 0:
            print(f"{self.nama} sudah lulus, tidak lagi menerima beasiswa.")
        else:
            print(f"{self.nama} tidak menerima beasiswa.")


if __name__ == "__main__":
    alumni = Mahasiswa("Yusron Tsani", tahun_lulus=2023)
    aktif = Mahasiswa("Hafzan Wazani", nim="24241168", jurusan="Pendidikan Teknologi Informasi")
    ktm = KTM("Hafzan Wazani", nim="24241168", jurusan="Pendidikan Teknologi Informasi")
    ijazah = Ijazah("Yusron Tsani", tahun_lulus=2023)
    beasiswa = Beasiswa("Hafzan Wazani", nim="24241168", jurusan="Pendidikan Teknologi Informasi", tahun_lulus=0, jenis_beasiswa="Beasiswa Prestasi")

    alumni.tampilkan_info()
    aktif.tampilkan_info()
    ktm.tampilkan_ktm()
    ijazah.tampilkan_ijazah()
    beasiswa.tampilkan_beasiswa()