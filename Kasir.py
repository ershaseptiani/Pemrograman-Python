class kasir(object):

    def __init__(self, gas12, gas5, selang, regulator, komporgas, total=0):
        self.gas12 = gas12
        self.gas5 = gas5
        self.selang = selang
        self.regulator = regulator
        self.komporgas = komporgas
        self.total = total

    def cetakMenu():
        print("\t--------------------------")
        print("\t\tPrasyomo Gas")
        print("\t--------------------------")
        print("\n\t1.Gas Ukuran 12 Kg  = Rp 225.000\t")
        print("\n\t2.Gas Ukuran 5 Kg   = Rp 115.000\t")
        print("\n\t3.Selang Gas        = Rp 100.000\t")
        print("\n\t4.Regulator         = Rp 200.000\t")
        print("\n\t5.Kompor Gas        = Rp 400.000\t")
    
    def hitungHarga(self):
        self.total = (self.gas12 * 225000)+(self.gas5*115000)+(self.selang*100000)+(self.regulator*200000)+(self.komporgas*400000)
        print("\n--------------------------------------------------------\t+")
        print("\nTotal Pesanan Anda : Rp ",self.total)
        kembalian = int(input("Uang bayar : Rp ")) - self.total
        print ("\nKembalian Anda sebesar : Rp ",kembalian)
    
    def bayar(self):
        kembalian = int(input("Uang bayar : Rp ")) - self.total
        print("\nKembalian Anda sebesar : Rp ",kembalian)
    
def main():
    kasir.cetakMenu()

    gas12=int(input("\nmasukkan banyaknya gas 12 kg yang dipesan   : "))
    gas5=int(input("masukkan banyaknya gas 5 kg yang dipesan    : "))
    selang=int(input("masukkan banyaknya selang yang dipesan      : "))
    regulator= int(input("masukkan banyaknya regulator yang dipesan   : "))
    komporgas= int(input("masukkan banyaknya kompor gas yang dipesan  : "))

    bayar = kasir(gas12,gas5,selang,regulator,komporgas)

    bayar.hitungHarga()
    

if __name__ == "__main__":
    main()
    