from datetime import datetime
import os

class queue:
    def __init__(self):
        self.current_size = 0
        self.data = []
        self.front = None
        self.back = None
    
    def isempty(self):
        return self.data == []

    def enqueue(self, newdata):
        self.data.append(newdata)
        antrian = self.data
        self.current_size = len(antrian)

    def dequeue(self):
        if self.isempty():
            print("Belum ada antrian hari ini ^-^")
        else:
            f = open("data.txt","r")
            isi = f.readlines()
            if len(isi) == 0:
                print("Data masih kosong")
            else: 
                i = 1
                for x in isi:
                    banyak = x.split(".")
                    datakeluar = banyak.pop(0)
                    self.current_size = len(self.data)
                    print(self.data,"Telah selesai dilayani pada", datetime.now())
                    self.jumlah()
                    i += 1
            f.close()
            return self.data

    def jumlah(self):
        f = open("data.txt", "r")
        isi = f.readlines()
        if len(isi) == 0:
            print("Data masih kosong")
        else:
            i = 1
            for x in isi:
                banyak = x.split(",")
                print(str(i) +".", end=" ")
                print("Kendaraan yang berada dalam jalur tol yaitu", banyak[0], "dengan nomor transaksi", banyak[1], "seharga Rp", banyak[2], end="")
                i += 1
        f.close()
        print("\nTekan [ENTER] untuk kembali ke menu ...")
        input()
        self.menu()

    def keluar(self):
        import itertools
        import threading
        import time
        import sys

        done = False

        def animate():
            for c in itertools.cycle(['|','/','-','\\']):
                if done:
                    break

                sys.stdout.write('\rloading' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()
        time.sleep(5)
        done = True

        os.system("CLS")
        print("="*170)
        a = "ANDA TELAH KELUAR DARI PROGRAM ANTRIAN TOL"
        b = "TERIMA KASIH"
        print(a.center(170))
        print(b.center(170))
        print("="*170)

    def awal(self):
        print("\n")
        print("="*160)
        a = "PROJEK AKHIR"
        b = "PROGRAM ANTRIAN JALAN TOL"
        c = "MATA KULIAH STRUKTUR DATA"
        d = "INFORMATIKA UNEJ"
        e = "KELOMPOK 8"
        print(a.center(160))
        print(b.center(160))
        print(c.center(160))
        print(d.center(160))
        print(e.center(160))
        print("\n")
        print("-"*65)
        print("|                           KELOMPOK 8                          |")
        print("-"*65)
        print("|          NAMA                 |               NIM             |")
        print("-"*65)
        nama = ["Trinita Awani", "Mia Maulidya", "Resti Ika Pertiwi", "Audrey Akeyla F E"]
        NIM = ["212410103001", "212410103004", "212410103005", "212410103056"]
        for i in range(len(nama)):
            isi = str(nama[i])
            print("|  " + isi,end= " ")
            for y in range (25-len(isi)):
                print ('',end='')
            isi1 = str(NIM[i])
            print("\t\t|\t  " + isi1,end= " ")
            for y in range (20-5-len(isi1)):
                print ('',end='')
            print('\t\t|')
            print("-"*65)
        print("\n")
        print("=" * 160)
        input("\t\t\t\t\t\t\t\t Tekan [ENTER] untuk melanjutkan ...")
        self.menu()

    def info(self):
        import os
        os.system("CLS")
        print("\t---------------------------------------------------------------------")
        print("\t|                       INFO KENDARAAN                               | ")
        print("\t---------------------------------------------------------------------")
        print("\n\t---------------------------------------------------------------------")
        print("\t|           JENIS                |              HARGA TIKET          |")
        print("\t---------------------------------------------------------------------")
        print("\t|           MOBIL                |               Rp 50000            |")
        print("\t|            BUS                 |               Rp 100000           |")
        print("\t|           TRUCK                |               Rp 150000           |")
        print("\t---------------------------------------------------------------------")
        input("\n\tTekan [ENTER] untuk kembali ke menu ...")
        self.menu()

    def menu(self):
        import os
        os.system("CLS")
        print("="*160)
        a = "DAFTAR MENU ANTRIAN TOL"
        print(a.center(160))
        print("\n\t\t\t\t\t\t\t\t [1]  INFO KENDARAAN")
        print("\n\t\t\t\t\t\t\t\t [2]  MASUK SISTEM ANTREAN")
        print("\n\t\t\t\t\t\t\t\t [3]  KELUAR SISTEM ANTREAN")
        print("\n\t\t\t\t\t\t\t\t [4]  KENDARAAN DALAM TOL ")
        print("\n\t\t\t\t\t\t\t\t [0]  KELUAR ")
        print("\n")
        print("=" * 160)
        pilihan = int(input("\t\t\t\t\t\t\t\t Masukkan Pilihan Menu : " ))

        if pilihan == 1:
            self.info()

        if pilihan == 2:
            self.masuk()

        elif pilihan == 3:
            self.dequeue()
            input("")
            self.menu()

        elif pilihan == 4:
            self.jumlah ()

        elif pilihan == 0:
            self.keluar()

        else:
            print("Pilihan menu salah, silahkan pilih lagi")
            print("Tekan [ENTER] untuk kembali ke menu ...")
            input()
            self.menu()

    def masuk (self):
        os.system("CLS")
        mobil = 50000
        bus = 100000
        truck = 150000
        print("""
        Silahkan masukkan jenis kendaraan dengan mengetikkan nama kendaraan seperti yang tertera pada info [1]!
                                                terima kasih ^.^
        """)
        jenis = input("\nJenis Kendaraan            : ")
        notrans = str(id(jenis))
        if jenis.upper() == "MOBIL":
            banyak = int(input("Banyak kendaraan           : "))
            harga_tiket = str(mobil*banyak) 
            print("Tiket untuk mobil seharga  : Rp "+ harga_tiket)
            f = open ("data.txt","a")
            f.writelines([jenis + "," + notrans + "," + harga_tiket, "\n"])
            f.close()
            self.enqueue(jenis)
            print("\nData berhasil dimasukkan!")
            print("\nTekan [ENTER] untuk kembali ke menu ...") 
            input()
            self.menu()
        elif jenis.upper() == "BUS":
            banyak = int(input("Banyak kendaraan           : "))
            harga_tiket = str(bus*banyak)
            print("Tiket untuk bus seharga    : Rp "+ harga_tiket)
            f = open ("data.txt","a")
            f.writelines([jenis + "," + notrans + "," + harga_tiket, "\n"])
            f.close()
            self.enqueue(jenis)
            print("\nData berhasil dimasukkan!")
            print("\nTekan [ENTER] untuk kembali ke menu ...") 
            input()
            self.menu()
        elif jenis.upper() == "TRUCK":
            banyak = int(input("Banyak kendaraan           : "))
            harga_tiket = str(truck*banyak)
            print("Tiket untuk truck seharga  : Rp "+ harga_tiket)
            f = open ("data.txt","a")
            f.writelines([jenis + "," + notrans + "," + harga_tiket, "\n"])
            f.close()
            self.enqueue(jenis)
            print("\nData berhasil dimasukkan!")
            print("\nTekan [ENTER] untuk kembali ke menu ...") 
            input()
            self.menu()
        else : 
            print("\nJenis yang anda masukkan salah") 
            print("\nTekan [ENTER] untuk kembali ke menu ...") 
            input()
            self.menu()

q = queue()
q.awal()
