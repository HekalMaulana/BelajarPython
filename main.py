print(10*"=")
print("Latihan Perulangan Sederhana")
print(10*"=")

total = int(input("Masukan Jumlah Total Bintang = "))
print (f"Total Segitiga Adalah = {total}\n")


count = 1
space = int(total / 2)

while True:
    if (count % 2):
        print (" " *space,"*" *count)
        space -= 1
        count += 1
    
    else:
        count += 1
        continue

    

    if count > total:
        break
print("\nProgram Selesai")

