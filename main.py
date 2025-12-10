#Program Penerimaan dan Pengeluaran barang gudang di toko swalayan 
#I.S.: pengguna memasukkan menu yang diinginkan seperti barang yang diterima, barang yang keluar, menambahkan, menampilkan, 
# menghapus data, menghapus seluruh data, mengurutkan, dan mencari barang.
#F.S.: menampilkan hasil dari operasi menu yang dipilih.

import os

from gudang_utils.functions import *

class PengelolaanGudang:

    def main():    
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
                    print("     << PENCARIAN BARANG >>")
                    print("")
                    SequentialSearch(Kode, Nama, Jumlah, Satuan, N)
                    
                case 7 :
                    print("<< Penghancuran Data Barang >>")
                    MenghapusSemuaBarangData(Kode, Nama, Jumlah, Satuan, N, KodeBaru, NamaBaru, JumlahBaru, SatuanBaru)
                    
    
            Menu = MenuUtama(Menu)
    if __name__ == "__main__":
        main()
