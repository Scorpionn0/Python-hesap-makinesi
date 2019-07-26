print("1- Toplama")
print("2- Çıkarma")
print("3- Bölme")
print("4- Çarpma")

choes = int(input("Lütfen istediğiniz işlemi giriniz: "))

if choes == 1:
    sayi1 = int(input("Toplamak istediğiniz ilk sayıyı giriniz: "))
    sayi2 = int(input("Toplamak istediğiniz ikinci sayıyı giriniz: "))
    
    sonuc = sayi1 + sayi2
    print("Sonucunuz: ",sonuc)

elif choes == 2:
    sayi1 = int(input("Çıkan sayıyı giriniz: "))
    sayi2 = int(input("Çıkaran sayıyı giriniz: "))
    
    sonuc = sayi1 - sayi2
    print("Sonucunuz: ",sonuc)

elif choes == 3:
    sayi1 = int(input("Bölünen sayıyı giriniz: "))
    sayi2 = int(input("Bölen sayıyı giriniz: "))
    
    sonuc = sayi1 / sayi2
    print("Sonucunuz: ",sonuc)
    
elif choes == 4:
    sayi1 = int(input("İlk çarpanı giriniz: "))
    sayi2 = int(input("İkinci çarpanı giriniz: "))
    sonuc = sayi1 * sayi2
    print("Sonucunuz: ",sonuc)
    
else:
    print("Öyle bir işlem bulunmamaktadır!")
    
    #Python'da hesap makinesi yapmak için gerekli kaynak kodlar.

    
