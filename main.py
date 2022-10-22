# Latihan Dictionary (Data Mahasiswa)
import datetime 
import os
import string
import random

# FromKeys

# Template Dict Mahasiswa
mahasiswaTemp = {
    'nama':'nama',
    'nim':'00000000',
    'sks':0,
    'lahir':datetime.datetime(1111,1,11),    
}
# Template Dict Mahasiswa End

dataMahasiswa = {}

while True:

    # CLear Screen Pada Terminal
    os.system("cls")
    # Clear Screen End

    print(f"{'Selamat Datang':^20}")
    print(f"{'Data Mahasiswa':^20}")
    print("="*20)

    mahasiswa = dict.fromkeys(mahasiswaTemp.keys())
    # print(mahasiswa)
    mahasiswa['nama'] = input("Nama Mahasiswa : ")
    mahasiswa['nim'] = input("Nim Mahasiswa : ")
    mahasiswa['sks'] = int(input("SKS Lulus Mahasiswa : "))
    TAHUN = int(input("Tahun Lahir (YYYY) : "))
    BULAN = int(input("Bulan Lahir (1-12) : "))
    TANGGAL = int(input("Tanggal Lahir (1-31) : "))
    mahasiswa ['lahir'] = datetime.datetime(TAHUN,BULAN,TANGGAL) 

    KEY = ''.join((random.choice(string.ascii_uppercase)for  i in range (6)))
    dataMahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':<6} {'NAMA' :<17} {'NIM' :<10} {'SKS' :^10} {'LAHIR' :^10} ")
    print("="*60) 
    for mahasiswa in dataMahasiswa:
        KEY = mahasiswa

        NAMA = dataMahasiswa[KEY]['nama']
        NIM = dataMahasiswa[KEY]['nim']
        SKS = dataMahasiswa[KEY]['sks']
        LAHIR = dataMahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA :<17} {NIM :<10} {SKS :^10} {LAHIR :^10} ") 

    print("\n")
    done = input("Apakah Ingin Melanjutkan (y/n) : ")

    if done == 'n':
        break

print("PROGRAM SELESAI")
