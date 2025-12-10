#Program Penerimaan dan Pengeluaran barang gudang di toko swalayan 
#I.S.: pengguna memasukkan menu yang diinginkan seperti barang yang diterima, barang yang keluar, menambahkan, menampilkan, 
# menghapus data, menghapus seluruh data, mengurutkan, dan mencari barang.
#F.S.: menampilkan hasil dari operasi menu yang dipilih.

import os

# Konstanta
MAKSBARANG = 10

# Subrutin untuk menampilkan menu utama
def MenuUtama(Menu):
    os.system('cls')
    print('\n<< MENU GUDANG >>')
    print('-------------------')
    print('1. Barang yang diterima')
    print('2. Penambahan Barang')
    print('3. Tampilkan Barang')
    print('4. Barang yang keluar')
    print('5. Urutkan Barang')
    print('6. Cari Barang')
    print('7. Menghapus seluruh Data Barang')
    print('0. Keluar')
    
    Menu = int(input('Pilihan Anda? '))
    while (Menu < 0) or (Menu > 7):
        print('Nomor Menu Tidak ada, Ulangi!!')
        os.system('pause')
        os.system('cls')
        print('\n<< MENU GUDANG >>')
        print('-------------------')
        print('1. Barang yang diterima')
        print('2. Penambahan Barang')
        print('3. Tampilkan Barang')
        print('4. Barang yang keluar')
        print('5. Urutkan Barang')
        print('6. Cari Barang')
        print('7. Menghapus seluruh Data Barang')
        print('0. Keluar')
        Menu = int(input('Pilihan Anda? '))
    
    return Menu

# Subrutin untuk penerimaan barang
def PenerimaanBarang(Kode, Nama, Jumlah, Satuan, N):
    i = 0
    print('<< PROSES PENERIMAAN BARANG >>')
    print()
    while (i < MAKSBARANG):
        print(f'Barang Ke-{i+1}')
        print(f'---------------')
        KodeInput = input('Kode Barang     : ').upper()
    
        if KodeInput == 'STOP':
            break
        
        Kode[i] = KodeInput    
        Nama[i] = input('Nama Barang     : ').upper()
        Jumlah[i] = int(input('Jumlah Barang   : '))
        Satuan[i] = input('Satuan Barang   : ').upper()
        
        print()
        i += 1
        
        if i >= MAKSBARANG:
            print("Gudang sudah melebihi kapasitas!! Tidak bisa menambah barang lagi.")
            os.system('pause')  
            
   
    N = i
    return N

# Subrutin penambahan barang 
def TambahBarang(Kode, Nama, Jumlah, Satuan, N, KodeBaru, NamaBaru, JumlahBaru, SatuanBaru):
    if (N < MAKSBARANG):
        Kode[N] = KodeBaru.upper()
        Nama[N] = NamaBaru.upper()
        Jumlah[N] = JumlahBaru
        Satuan[N] = SatuanBaru.upper()
        
        print("\nBarang berhasil ditambahkan!")
        os.system('pause')
        N += 1
    else:
        print('Kapasitas maksimum barang telah tercapai!')

    return N

        
# Subrutin menampilkan data barang
def TampilBarang(Kode, Nama, Jumlah, Satuan, N):
    
    if N == 0:
        print('\nTidak ada barang dalam gudang.')
    else:
        print('\n                  DATA BARANG ')
        print('--------------------------------------------------------------')
        print('| No  |    Kode    |    Nama Barang     | Jumlah    | Satuan |')
        print('----------------------------------------------------------')
        for i in range(N):
             print(f'| {i+1:>2}  | {Kode[i]:9} |   {Nama[i]:<16} | {Jumlah[i]:>5}    | {Satuan[i]:<5}  |')
        print('--------------------------------------------------------------')
        
    os.system('pause')

# Subrutin untuk pengeluaran barang berdasaran Kode
def HapusBarang(Kode, Nama, Jumlah, Satuan, N, ElemenHapus):
    
    IndexHapus = -1

    # Cari indeks barang yang akan dihapus
    for i in range(N):
        if Kode[i] == ElemenHapus:
            IndexHapus = i

    if IndexHapus == -1:
        print('Barang tidak ditemukan!')
        os.system('pause')
        return N

    # Geser elemen-elemen setelahnya ke kiri
    for j in range(IndexHapus, N - 1):
        Temp = Kode[j + 1]
        Temp = Nama[j + 1]
        Temp = Jumlah[j + 1]
        Temp = Satuan[j + 1]

        Kode[j] = Temp
        Nama[j] = Temp
        Jumlah[j] = Temp
        Satuan[j] = Temp

    # Kosongkan elemen terakhir
    Kode[N - 1] = ''
    Nama[N - 1] = ''
    Jumlah[N - 1] = 0
    Satuan[N - 1] = ''

    N -= 1
    print('Barang berhasil dikeluarkan.')
    os.system('pause')
    return N


# Subrutin pengurutan nama barang secara ascending menggunakan metode Bubble Sort
def BarangNamaAsc(Kode, Nama, Jumlah, Satuan, N):
    for i in range(N-1):  
        for j in range(N-1, i, -1): 
            if Nama[j] < Nama[j-1]:
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp
                
                Temp = Kode[j]
                Kode[j] = Kode[j-1]
                Kode[j-1] = Temp
                
                Temp = Jumlah[j]
                Jumlah[j] = Jumlah[j-1]
                Jumlah[j-1] = Temp
                
                Temp = Satuan[j]
                Satuan[j] = Satuan[j-1]
                Satuan[j-1] = Temp
                
            j-=1

# Subrutin pengurutan kode barang secara descending menggunakan metode Selection Sort (minimum)
def BarangKodeDsc(Kode, Nama, Jumlah, Satuan, N):
    for i in range(N-1):
        max = i
        for j in range(i+1, N):
            if Kode[j] > Kode[max]: 
                max = j
        
        Temp = Kode[i]
        Kode[i] = Kode[max]
        Kode[max] = Temp
        
        Temp = Nama[i]
        Nama[i] = Nama[max]
        Nama[max] = Temp
        
        Temp = Jumlah[i]
        Jumlah[i] = Jumlah[max]
        Jumlah[max] = Temp
        
        Temp = Satuan[i]
        Satuan[i] = Satuan[max]
        Satuan[max] = Temp
    

                
# Validasi menu pengurutan
def MenuPengurutan(Menu2):
    print("Pilih metode pengurutan:")
    print("1. Berdasarkan Nama (Ascending)")
    print("2. Berdasarkan Kode (Descending)")
    print("0. Keluar")
    Menu2 = int(input("Masukkan Pilihan Anda: "))
    
    while (Menu2 < 0) or (Menu2 > 2):
        print('Nomor Menu Tidak ada, Ulangi!!')
        os.system('pause')
        os.system('cls')
        print("Pilih metode pengurutan:")
        print("1. Berdasarkan Nama (Descending)")
        print("2. Berdasarkan Kode (Ascending)")
        print("0. Keluar")
        Menu2 = int(input("Masukkan Pilihan Anda: "))
    
    return Menu2
              

# Subrutin pencarian barang dengan metode Sequantial dengan boolean
def SequentialSearch(Kode, Nama, Jumlah, Satuan, N):
    # Memasukkan kode barang yang dicari
    KodeCari = input('Masukkan kode barang yang dicari: ')
    
    # Proses pencarian
    i = 0
    Ketemu = False
    while (not Ketemu) and (i <= N):
        if Kode[i] == KodeCari:
            Ketemu = True
        else:
            i += 1
    
    # Menampilkan hasil pencarian
    if (Ketemu):
        print('\n                         DATA BARANG')
        print(f'Kode Barang: {KodeCari}')
        print('---------------------------------------------------------')
        print('| No |    Kode    |    Nama Barang     | Jumlah | Satuan |')
        print('---------------------------------------------------------')
        print(f'| {1:>2} | {Kode[i]:9}  | {Nama[i]:<16}   | {Jumlah[i]:>6} | {Satuan[i]:<6} |')
        print('---------------------------------------------------------')
    else:
        print(f'Barang dengan kode {KodeCari} tidak ditemukan!')

    
    os.system('pause')

def MenghapusSemuaBarangData(Kode, Nama, Jumlah, Satuan, N, KodeBaru, NamaBaru, JumlahBaru, SatuanBaru):
    Confirm = input("Apakah Anda yakin ingin menghapus semua data barang? (Y/N): ").upper()
    if Confirm == 'Y':
        for i in range(N):
            Kode[i] = '/'     
            Nama[i] = '/'     
            Jumlah[i] = 0    
            Satuan[i] = '/'  

        N = 0
        print("Semua data barang di gudang telah dihapus.")
    else:
        print("Penghapusan dibatalkan.")

    os.system('pause')
    return N
    

# Badan Program Utama
os.system('cls')
# Penciptaan array Kode Barang, Nama Barang, Jumlah Barang, dan Satuan Barang
Kode = ['/'] * MAKSBARANG
Nama = ['/'] * MAKSBARANG
Jumlah = [0] * MAKSBARANG
Satuan = ['/'] * MAKSBARANG

KodeBaru = ['/'] * MAKSBARANG
NamaBaru = ['/'] * MAKSBARANG
JumlahBaru = [0] * MAKSBARANG
SatuanBaru = ['/'] * MAKSBARANG

N = 0
Menu = 0
Menu = MenuUtama(Menu)
while (Menu != 0):
    os.system('cls')
    match (Menu):
        case 1:
            N = PenerimaanBarang(Kode, Nama, Jumlah, Satuan, N)

        case 2:
            if N < MAKSBARANG :
                print("<< PENAMBAHAN BARANG >>")
                print ()
                KodeBaru = input('Kode Barang   : ').upper()
                NamaBaru = input('Nama Barang   : ').upper()
                JumlahBaru = int(input('Jumlah Barang : '))
                SatuanBaru = input('Satuan Barang : ').upper()
            N = TambahBarang(Kode, Nama, Jumlah, Satuan, N, KodeBaru, NamaBaru, JumlahBaru, SatuanBaru)
            
        case 3:
            print("          << MENAMPILKAN BARANG >>")
            TampilBarang(Kode, Nama, Jumlah, Satuan, N)
            
        case 4:
                if (N == 0):
                    print("Gudang kosong, tidak ada barang dapat dikeluarkan.")
                    os.system('pause')
                else:
                    print("<< BARANG YANG KELUAR >>")
                    print()
                    ElemenHapus = input('Masukkan kode barang yang akan dikeluarkan: ').upper()
                    N = HapusBarang(Kode, Nama, Jumlah, Satuan, N, ElemenHapus)
            
        case 5:
            Menu2 = 0
            Menu2 = MenuPengurutan(Menu2)
            while (Menu2 != 0):
                os.system('cls')
                match (Menu2):
                    case 1 :
                        print('<< PENGURUTAN NAMA SECARA ASCENDING >>')
                        BarangNamaAsc(Kode, Nama, Jumlah, Satuan, N)
                        os.system('cls')
                        TampilBarang(Kode, Nama, Jumlah, Satuan, N)
                    case 2 :
                        print('<< PENGURUTAN KODE SECARA DESCENDING >>')
                        BarangKodeDsc(Kode, Nama, Jumlah, Satuan, N)
                        os.system('cls')
                        TampilBarang(Kode, Nama, Jumlah, Satuan, N)
                        
                
                os.system('cls')
                Menu2 = MenuPengurutan(Menu2) 
                
        case 6:
            print("<< PENCARIAN BARANG >>")
            SequentialSearch(Kode, Nama, Jumlah, Satuan, N)
            
        case 7 :
            print("<< Penghancuran Data Barang >>")
            MenghapusSemuaBarangData(Kode, Nama, Jumlah, Satuan, N, KodeBaru, NamaBaru, JumlahBaru, SatuanBaru)
            

    Menu = MenuUtama(Menu)
