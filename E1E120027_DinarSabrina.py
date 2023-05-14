print("Nama: DINAR SABRINA")
print("NIM: E1E120027")
while True:
    print("1. Linear")
    print("2. Segitiga")
    print("3. Trapesium")
    print("4. Sigmoid")
    print("5. Beta")
    print("6. Gauss")
    print("0 = Pilihan Tidak Tersedia")
    pilihan = int(input("Masukan Pilihan Anda = "))

    #Linear#
    if pilihan == 1 :
            while True :
                print("1. Linear Naik")
                print("2. Linear Turun")
                linear = int(input("Masukan Pilihan = "))

                if linear == 1 :
                    print("LINEAR NAIK")
                    x = float(input("Masukkan nilai x: "))
                    a = float(input("Masukkan nilai a: "))
                    b = float(input("Masukkan nilai b: "))

                    if x < a:
                         m = 0
                    elif a < x < b: 
                        m = (x - a) / (b - a)
                    elif x > b:
                         m = 1
                    print("µ(m) = {:.2f}".format(m))

                elif linear == 2 :
                        print("LINEAR TURUN")
                        x = float(input("Masukkan nilai x: "))
                        a = float(input("Masukkan nilai a: "))
                        b = float(input("Masukkan nilai b: "))
                        
                        if a < x < b:
                            m = (b - x) / (b - a)
                        elif x > b:
                             m = 0

                        print("µ(m) = {:.2f}".format(m))
                else :
                    print("Pilihan tidak tersedia, silakan masukan kembali pilihan anda.")
                    continue
                break
    #segitiga#
    elif pilihan == 2:
        print("SEGITIGA")
        x = float(input("Masukkan nilai x: "))
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        c = float(input("Masukkan nilai c: "))

        if a < x < b:
            m = (x - a) / (b - a)
        elif b < x < c:
            m = (c - x) / (c - b)
        elif x < a or x > b:
             m = 0
        print("µ(m) = {:.2f}".format(m))
        

    #Trapesium#
    elif pilihan == 3:
        print("TRAPESIUM")
        x = float(input("Masukkan nilai x: "))
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        c = float(input("Masukkan nilai c: "))
        d = float(input("Masukkan nilai d: "))

        if a <= x < b:
            m = (x - a) / (b - a)
        elif b <= x < c:
            m = 1
        elif c <= x <= d:
            m = (d - x) / (d - c)
        print("µ(m) = {:.2f}".format(m))
    
    #Sigmoid#
    elif pilihan == 4:
        while True:
            print("1. Sigmoid Penyusutan")
            print("2. Sigmoid Pertumbuhan")
            sigmoid = int(input("Masukan Pilihan = "))

            if sigmoid == 1:
                print("SIGMOID PENYUSUTAN")
                x = float(input("Masukkan nilai x: "))
                a = float(input("Masukkan nilai a: "))
                y = float(input("Masukkan nilai y: "))

                b = ((y - a)) / 2 + a

                if x < a:
                    s = 1
                elif a < x < b:
                    s = 1 - 2 * ((x - a) / (y - a))**2
                elif b < x < y:
                    s = 2 * ((y - x) / (y - a))**2
                elif x > y:
                    s = 0
                print("µ(s) = {:.2f}".format(s))
                        
            elif sigmoid == 2:
                print("SIGMOID PERTUMBUHAN")
                x = float(input("Masukkan nilai x: "))
                a = float(input("Masukkan nilai a: "))
                y = float(input("Masukkan nilai y: "))

                b = ((y - a) / 2) + a

                if x < a:
                    s = 0
                elif a < x < b:
                    s = 2 * ((x - a) / (y - a))**2
                elif b < x < y:
                    s = 1 - 2 * ((y - x) / (y - a))**2
                elif x > y:
                    s = 1
                print("µ(s) = {:.2f}".format(s))


            else :
                print("Pilihan tidak ada, silakan masukan kembali pilihan anda.")
                continue
            break
    
    #beta#
    elif pilihan == 5:
        print("BETA")
        x = float(input("Masukkan nilai x: "))
        a = float(input("Masukkan nilai awal: "))
        z = float(input("Masukkan nilai akhir: "))

        b = ((a - z ) / 2) + a
        y = ((z - a) / z) + a

        m = 1 / 1 + ((x - y) / b)**2
        print("µ(m) = {:.2f}".format(m))

    #Gauss#
    elif pilihan == 6:
        print("GAUSS")
        x = float(input("Masukkan nilai x: "))
        a = float(input("Masukkan nilai awal: "))
        z = float(input("Masukkan nilai akhir: "))

        k = ((z - a) / 2)
        y = (a + k)
        e = 2.7182
        g = e*(-k(y - x)**2)
        print("µ(g) = {:.2f}".format(g))

    #opsi penutup#
    elif pilihan == 0 :
         break
    else:
        print("Pilihan tidak ada, silakan masukan kembali pilihan anda.")
        continue