# Nama: Muhammad Helmi Yaya
# NPM: 21330014

class Komputasi :
    # menu
    def menu (self) :
        menu = """
Menghitung Cepat Rambat Gelombang Bunyi:
1. Medium Padat
2. Medium Cair
3. Medium Gas
"""
        return menu
    # medium padat
    def padat (self, E, ρ) :
        hasil = (E / ρ) ** 0.5
        return hasil
    
    # medium cair
    def cair (self, β, ρ) :
        hasil = (β / ρ) ** 0.5
        return hasil
    
    # medium gas
    def gas (self, γ, R, T, Mr) :
        hasil = (γ * R * T / Mr) ** 0.5
        return hasil
        
while True :
        print (Komputasi().menu())
        kode = int(input("masukkan pilihan anda: "))
        print ("###################################################")
        
        if kode == 1 :
            print ("Menghitung Cepat Rambat Bunyi di Medium Benda Padat")
            print ("E adalah Modulus Young")
            print ("ρ adalah massa jenis benda")
            E = float(input("masukan nilai E: "))
            ρ = float(input("masukan nilai ρ: "))
            hasil = (Komputasi().padat(E, ρ))
            print (f"hasil = {hasil:.1f}")
            
        elif kode == 2 :
            print ("Menghitung Cepat Rambat Bunyi di Medium Benda Cair")
            print ("β adalah Modulus Bulk dalam N/m^2")
            print ("ρ adalah massa jenis zat cair dalam kg/m^3")
            β = float(input("masukan nilai β : "))
            ρ = float(input("masukan nilai ρ : "))
            hasil = (Komputasi().cair(β,ρ))
            print (f"hasil = {hasil:.1f}")       
            
        elif kode == 3 :
            print ("Menghitung Cepat Rambat Bunyi di Medium Gas")
            print ("γ adalah Konstanta Laplace")
            print ("R adalah Konstanta Gas Umum")
            print ("T adalah Suhu Gas")
            print ("Mr adalah Massa Molekul Gas Relatif")
            γ = float(input("masukan nilai γ : "))
            R = float(input("masukan nilai R : "))
            T = float(input("masukan nilai T : "))
            Mr = float(input("masukan nilai Mr : "))
            hasil = (Komputasi().gas(γ, R, T, Mr))
            print (f"hasil = {hasil:.1f}") 
            
        else :
            print ("Inputan Salah")

        lagi = input("hitung lagi : (ya/tidak) ")
         
        if lagi == "ya" :
            continue
        if lagi == "tidak" :
            print ("Program Berakhir")
            break
        else :
            print ("Inputan Salah")
            
            
            
            
            
        