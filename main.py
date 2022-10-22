# Latihan Fungsi

# Import Statement
import os

# Header
def header():
    '''Header'''
    os.system("cls")
    print("\n\n")
    print("="*50)
    print(f"{'Program Menghitung':^50}")
    print(f"{'Keliling Dan Luas Persegi Panjang':^50}")
    print("="*50)

# Input Dari User
def inputUser():
    '''Input Dari User'''
    lebar = int(input("Masukan Lebar Persegi Panjang\t: "))
    panjang = int(input("Masukan Panjang Persegi Panjang\t: "))

    return lebar,panjang

# Hitung Luas Dan Keliling Persegi Panjang
def hitungLuas(lebar,panjang):
    '''Hitung Luas Persegi Panjang'''
    return lebar * panjang

def hitungKeliling(lebar,panjang):
    '''Hitung Keliling Persegi Panjang'''
    return 2 * (panjang + lebar)

# Tampilkan Hasil
def hasilLuas():
    '''Hasil luas dan keliling Persegi Panjang'''
    print("="*50)
    print (f"Hasil Dari LUAS = {LUAS}")

def hasilKeliling():
    '''Hasil luas dan keliling Persegi Panjang'''
    print("="*50)
    print (f"Hasil Dari KELILING = {KELILING}")

def hasilLuasDanKeliling():
    print("="*50)
    print (f"Hasil Dari LUAS\t\t= {LUAS}")
    print (f"Hasil Dari KELILING\t= {KELILING}")

while True:
    # Panggil Function Header
    header()

    # Input User
    LEBAR,PANJANG = inputUser()
    # Input User End

    print("="*50)
    luasAtauKeliling = input("Pilih 1 untuk Luas\nPilih 2 untuk Keliling\nPilih 3 untuk Luas Dan Keliling : ")
    # Hitung Luas
    if luasAtauKeliling ==  '1':
        LUAS = hitungLuas(LEBAR,PANJANG)
        hasilLuas()

    # Hitung Keliling
    elif luasAtauKeliling == '2':
        KELILING = hitungKeliling(LEBAR,PANJANG)
        hasilKeliling()

    # Hitung Luas Dan Keliling
    else:
        # Panggil Function hitungLuas dan hitungKeliling
        LUAS = hitungLuas(LEBAR,PANJANG)
        KELILING = hitungKeliling(LEBAR,PANJANG)

        # Panggil Keliling
        hasilLuasDanKeliling()

    print("="*50)
    done = input("Apakah Ingin Lanjut (y/n) : ")
    if done == 'n' :
        break
    if done == 'N' :
        break

print("\n\nPROGRAN SELESAI")
