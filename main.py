# Latihan List (Program List Buuku)

from operator import index


listBuku = []
while True:
    print("\nProgram List Data Buku")
    print("="*50)

    judul = input("\n\nMasukan Judul Buku\t: ")
    penulis = input("Masukan Penulis Buku\t: ")

    dataBuku = [judul,penulis]
    listBuku.append(dataBuku)

    print("\n\nList Data Buku")
    print("="*50)

    for index,buku in enumerate(listBuku):
        print(f"{index+1} | Judul = {buku[0]} | Penulis = {buku[1]}")

    print("\n\n","="*50)
    done = input("Apakah Anda Ingin Melanjutkan (y/n) : ")

    if done == "n":
        break;

print("\n\nPROGRAM SELESAI")
