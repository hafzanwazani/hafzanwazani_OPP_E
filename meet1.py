# class>motor
# object> surat2, kondisi_mesin, model, harga, CC, warna
#nama : M hafzan wazani(24241168)

class SepedaMotor:
    def __init__(self, surat2, kondisi_mesin, merk, model, harga, cc, warna):
        self.surat2 = surat2
        self.kondisi_mesin = kondisi_mesin
        self.merk = merk
        self.model = model
        self.harga = harga
        self.cc = cc
        self.warna = warna

    def tampilkan_info(self):
        print(f"Merk           : {self.merk}")
        print(f"Model          : {self.model}")
        print(f"Warna          : {self.warna}")
        print(f"Kapasitas Mesin: {self.cc} cc")
        print(f"Harga          : Rp{self.harga:,}")
        print(f"Kondisi Mesin  : {self.kondisi_mesin}")
        print(f"Surat-surat    : {self.surat2}")


# contoh pemakaian
motor1 = SepedaMotor(
    surat2="Lengkap (STNK & BPKB)",
    kondisi_mesin="Ba
    model="nmax",
    harga=28500000,ik",
    merk="Yamaha",
    cc=155,
    warna="hitam"
)

motor1.tampilkan_info()