def magic():
    print("MAGIC BALL OYUNUNA HOŞ GELDİNİZ.\nBu oyunda amacınız evet hayır soruları sorup rastegele bir cevap almanızdır.\nBOL ŞANS")
    
    dosya = open("8_ball_responses.txt", "r")
    cevaplar = dosya.read()
    cevaplar=cevaplar.splitlines()
    dosya.close()

    import random
    devammı = "evet"

    while devammı.lower() == "evet":
        soru = input("Evet hayır sorusu giriniz: ")
        cevap = random.choice(cevaplar)
        print(f"Hmm, düşüneyim... {cevap}")
        devammı = input("Devam etmek istiyorsanız 'evet' yazın, aksi halde 'hayır' yazın: ")

magic()
