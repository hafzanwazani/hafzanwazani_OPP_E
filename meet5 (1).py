# Level 1
class Akademik:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def identitas(self):
        print(f"ID: {self.nama} ({self.nim})")

# Level 2 (Parent 1)
class MhsAktif(Akademik):
    def masuk(self):
        print(f"Mhs {self.nama} masuk 2025.")

# Level 2 (Parent 2)
class MhsAlumni(Akademik):
    def lulus(self):
        print(f"Mhs {self.nama} lulus dan dapat ijazah.")

# Level 3 (Child 1: Multilevel Inheritance)
class KTM(MhsAktif):
    # Method Overriding
    def masuk(self):
        print(f"KTM {self.nama} ({self.nim}) diterbitkan.")

# Level 3 (Child 2: Multiple Inheritance)
class Beasiswa(MhsAlumni, MhsAktif):
    def __init__(self, nama, nim, jenis):
        super().__init__(nama, nim) 
        self.jenis = jenis
    
    def cek_status(self):
        print(f"Status: {self.nama} penerima beasiswa {self.jenis}.")

# --- DEMO ---
print("--- KTM (Multilevel) ---")
ktm1 = KTM("isna", "2025001")
ktm1.identitas()
ktm1.masuk() # Output berubah karena Overriding

print("\n--- Beasiswa (Multiple) ---")
beasiswa1 = Beasiswa("Hafzan", "24241168", "PPA")
beasiswa1.identitas() 
beasiswa1.masuk() # Diwarisi dari MhsAktif
beasiswa1.lulus() # Diwarisi dari MhsAlumni
beasiswa1.cek_status()