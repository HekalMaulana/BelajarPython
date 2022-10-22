# Date And Time (latihan)

import datetime as dt
from re import A

print("\nMasukan Tanggal, \nBulan, dan tahun lahir Anda\n")
tanggal = int(input("Tanggal Lahir Anda \t:"))
bulan   = int(input("Bulan Lahir Anda \t:"))
tahun   = int(input("Tahun Lahir Anda \t:"))

tanggalLahir = dt.date(tahun,bulan,tanggal)
print("\nTanggal Lahir Anda Ialah : ",tanggalLahir)

hariIni = dt.date.today()
print (f"\nHari ini tanggal : {hariIni}")
print (f"Hari ini adalah hari : {hariIni:%A}\n")
umurHari = hariIni - tanggalLahir
umurTahun = umurHari.days // 365
print (f"Umur Hari anda adalah : {umurHari}")
print (f"Umur Tahun anda adalah : {umurTahun} Tahun\n")
