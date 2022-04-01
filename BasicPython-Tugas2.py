def tambahkontak():
    nama = input(str("Masukan Nama Lengkap : "))
    nomor = input(str("Masukan Nomor Handphone :"))
    with open ('daftar_kontak.txt', 'a') as filex:
        filex.write("Nama :")
        filex.write(nama)
        filex.write('\n')
        filex.write("Nomor Handphone :")
        filex.write(nomor)
        filex.write("\n")
    print()
    print("Kontak Berhasil Ditambahkan")

print("Selamat Datang!")
print("")
print("")

print("---Menu---")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar") 

print("")
print("")
menu = input(str("Pilih Menu : "))

if menu == '1':
    print("\nDaftar Kontak")
    print("")
    with open ('daftar_kontak.txt', 'r') as filex:
      daftar_kontak = filex.read()
      print (daftar_kontak)

elif menu == '2':
    while True:
        if tambahkontak() == False:
            continue
        else:
            break

elif menu == '3':
    print("Program Selesai, Sampai Jumpa :)")
    
else:
    print("Menu Tidak Tersedia")    
    