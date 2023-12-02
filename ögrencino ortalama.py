import pickle
def öğrenci():
    dic = {}
    devammı = "yes"
    
    dosya=open("veriler.dat","wb")
    while devammı== "yes":
        öğrenci_isim = input("Öğrencinin ismini giriniz: ")
        öğrenci_numara = input("Öğrencinin numarasını giriniz: ")
        öğrenci_not_ortalama = input("Not ortalamasını giriniz: ")

        dic[öğrenci_numara] = {"isim": öğrenci_isim, "not_ortalama": öğrenci_not_ortalama}

        devammı = input("Devam etmek istiyor musunuz? (yes/no): ")
    pickle.dump(dic, dosya)
    print(dic)

öğrenci()

