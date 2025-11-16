import random

Meyveler = ["elma", "karpuz", "erik"]
Spor_Dalları = ["basketbol","futbol", "tenis"]



#harf tahmin sistemi
kategoriler = [Meyveler, Spor_Dalları]
Kelimeseç = random.choice(kategoriler)
Kelime = random.choice(Kelimeseç)


Harfler = list(Kelime) #kelimenin harflerini listeye atar
gizli_liste = ["_"] * len(Harfler) 



Kullanıcıpuan = 0
hatasayısı = 0
bonuspuan = 0
girilen_harfler = [] #girilen harflerin kaydını tutacak
Listedeğişim = 0 #gizli listedeki değişiklik sayısını tutuyor.
#Listedeki değişim sayısı seçilen kelimenin harf sayısına eşit olursa tüm harfler bulunmuş olur.



def iptal_kontrol(girdi): #hesap makinesinde herhangi bir basamakta 'iptal' yazınca iptal etmesi için yazdım
    if girdi.lower() == "iptal":
        print("İşlem iptal edildi.")
        return True
    return False

def cevap_karsilastirma(kullanici_cevap, gercek_cevap): #hesap makinesinde kullanıcı cevabı ile gerçek cevabı kıyaslamak için yazdım.
    global hatasayısı, bonuspuan, Listedeğişim, Kullanıcıpuan
    
    if abs(kullanici_cevap - gercek_cevap) < 0.0001:  # Float karşılaştırması için tolerans
        print("Doğru! ✓")
        bonuspuan += 1
        Kullanıcıpuan += 15
        print(f"Bonus puan: {bonuspuan}")

        # Rastgele harf açma kısmı
        kapali_indeksler = [i for i in range(len(gizli_liste)) if gizli_liste[i] == "_"]
        
        if kapali_indeksler:  # Eğer açılmamış harf varsa
            acilacak_indeks = random.choice(kapali_indeksler)
            gizli_liste[acilacak_indeks] = Harfler[acilacak_indeks]
            Listedeğişim += 1
            print(" Açılan harf:", Harfler[acilacak_indeks]) 
            print("Güncel kelime:", ' '.join(gizli_liste))
        else:
            print("Tüm harfler zaten açık!")


    else:
        print(f"Yanlış! Doğru cevap: {gercek_cevap}")
        hatasayısı += 1
        Kullanıcıpuan -= 10
        print(f"Hata sayısı: {hatasayısı}")

def hesaplama():
    global hatasayısı, bonuspuan
    
    # İşlem türü girişi
    islem_turu = input("İşlem türü (toplama/çıkarma/çarpma/bölme) ya da 'iptal': ")
    
    if iptal_kontrol(islem_turu):
        return
    
    # Birinci sayı girişi
    print("\nBirinci sayı (iptal için 'iptal'): ", end="")
    girdi = input()
    if iptal_kontrol(girdi):
        return
    
    try:
        x = float(girdi) #sayı girilmediyse uyarı versin diye
    except ValueError:
        print("Geçersiz sayı!")
        return
    
    # İkinci sayı girişi
    print("\nİkinci sayı (iptal için 'iptal'): ", end="")
    girdi = input()
    if iptal_kontrol(girdi):
        return
    
    try:
        y = float(girdi) #sayı girilmediyse uyarı versin diye
    except ValueError:
        print("Geçersiz sayı!")
        return
    
    # İşlem yapma ve cevap alma
    if islem_turu == "toplama":
        print(f"{x} + {y} = ? ", end="")
        girdi = input()
        if iptal_kontrol(girdi):
            return
        kullanici_cevap = float(girdi)
        gercek_cevap = x + y
        cevap_karsilastirma(kullanici_cevap, gercek_cevap)
        
    elif islem_turu == "çıkarma":
        print(f"{x} - {y} = ? ", end="")
        girdi = input()
        if iptal_kontrol(girdi):
            return
        kullanici_cevap = float(girdi)
        gercek_cevap = x - y
        cevap_karsilastirma(kullanici_cevap, gercek_cevap)
        
    elif islem_turu == "çarpma":
        print(f"{x} * {y} = ? ", end="")
        girdi = input()
        if iptal_kontrol(girdi):
            return
        kullanici_cevap = float(girdi)
        gercek_cevap = x * y
        cevap_karsilastirma(kullanici_cevap, gercek_cevap)
        
    elif islem_turu == "bölme":
        if y == 0:
            print("Hata: Sıfıra bölme yapılamaz!")
            hatasayısı += 1
            print(f"Hata sayısı: {hatasayısı}")
            return
        print(f"{x} / {y} = ? ", end="")
        girdi = input()
        if iptal_kontrol(girdi):
            return
        kullanici_cevap = float(girdi)
        gercek_cevap = x / y
        cevap_karsilastirma(kullanici_cevap, gercek_cevap)
        
    else:
        print("Geçersiz işlem türü!")


def adamasmacagörsel(): #adamasmacanın aşamaları ve hatasayısına göre hangi durumda olması gerektiği
    if hatasayısı == 0:
        print("""
              
        ---- YENİ TUR----     
    +---+
    |   |
    |
    |
    |
    |
==========""")

    elif hatasayısı == 1:
        print("""
              
        ---- YENİ TUR---- 
    +---+
    |   |
    |   O
    |
    |
    |
    ==========""")

    elif hatasayısı == 2:
        print("""
              
        ---- YENİ TUR---- 
    +---+
    |   |
    |   O
    |   |
    |
    |
    ==========""")

    elif hatasayısı == 3:
        print("""
              
        ---- YENİ TUR---- 
    +---+
    |   |
    |   O
    |  /|
    |
    |
    ==========""")

    elif hatasayısı == 4:
        print("""
              
        ---- YENİ TUR---- 
    +---+
    |   |
    |   O
    |  /|\\
    |
    |
    ==========""")

    elif hatasayısı == 5:
        print("""
              
        ---- YENİ TUR---- 
    +---+
    |   |
    |   O
    |  /|\\
    |  /
    |
    ==========""")

    elif hatasayısı == 6:
        print("""
              

        ---- YENİ TUR---- 
    +---+
    |   |
    |   O
    |  /|\\
    |  / \\
    |
    ==========""")


    
while hatasayısı < 6 and Listedeğişim < len(gizli_liste): #listedeğişim, gizli harflerin olduğu listedeki değişim sayısını tutuyor, seçilen kelimenin harf sayısı kadar değişiklik olursa kullanıcı kelimeyi bilmiş olur
    
    adamasmacagörsel()
    print(' '.join(gizli_liste)) #' '.join()listeyi birleştirip aralara boşluk koyuyor
    print("Girilen harfler: ", girilen_harfler)
    print("Bonus puan:", bonuspuan)
    print("hatasayısı:",hatasayısı)

    Seçilen_İşlem = input("Seçenekler: [H]arf tahmini , [S]oru çöz , [İ]pucu , [Ç]ıkış : ")
    
    if Seçilen_İşlem.upper() == "H":

        #Klasik harf tahmini
        Girilen_harf = input("Seçiminiz: ").lower()
        
    
        if len(' '.join(Girilen_harf)) != 1: #harfin bir tane olup olmadığını anlıyor
            print("Lütfen sadece bir harf giriniz.")
            continue

        if Girilen_harf in girilen_harfler: #harf önceden girildiyse uyarır
            print("Bu harfi zaten girdiniz.")
            continue
        girilen_harfler.append(Girilen_harf) 

        for x in range(len(Harfler)): #girilen harfin kelimenin kaçıncı harfi olduğunu bulup gizli listede yerine koyuyoruz
            if Harfler[x] == Girilen_harf:
                gizli_liste[x] = Girilen_harf
                Listedeğişim += 1
                Kullanıcıpuan += 10
                
        
        if Girilen_harf not in Harfler: #yanlış harf hata sayısı arttırır
            hatasayısı += 1
            Kullanıcıpuan -= 5
      
        print( ' '.join(gizli_liste))
       


        

    elif Seçilen_İşlem.upper() == "S":
        hesaplama()
   

    elif Seçilen_İşlem.lower() == "i" or Seçilen_İşlem == "İ": #ipucu alma kısmı
        if bonuspuan > 0:
            if Kelimeseç == Meyveler:
                print("Kategori : Meyveler")
            elif Kelimeseç == Spor_Dalları:
                print("Kategori: Spor Dalları")
            bonuspuan -= 1
        else:
            print("Yetersiz bonus puan")                
            
 
    
    elif Seçilen_İşlem.upper() == "Ç": #bütün işlemi sonlandırıyor
        print("Puanınız", Kullanıcıpuan)
        print("Çıkış yapılıyor.")
        exit()
    
    else:
        print("Lütfen geçerli bir değer giriniz.")


if Listedeğişim == len(gizli_liste): #oyunu kazanınca terminalde yazılması gerekenler
    adamasmacagörsel()
    Kullanıcıpuan += 50
    print("Tebrikler! Kelime:", Kelime)
    print("Puanınız:", Kullanıcıpuan)
  
elif hatasayısı >= 6: #oyunu kaybedince terminalde yazılması gerekenler
    adamasmacagörsel()
    Kullanıcıpuan -= 20
    print("Kaybettiniz! Doğru kelime:", Kelime)
    print("Puanınız:", Kullanıcıpuan)

