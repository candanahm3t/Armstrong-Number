
while True:
    sayi = int(input("Lütfen bir sayı girin:"))
    basamak= str(sayi)
    sonuc=0
    for x in basamak:
        toplam = int(x)**len(basamak)
        sonuc=sonuc+toplam

    if (sayi==sonuc):
        print("Girdiğiniz sayı Amstrong sayısıdır")
       

    else:
        print("Amstrong sayısı değildir")
      
    print("Programdan çıkmak için q'ya basın devam etmek için enter")
    kontrol=input()
    if (kontrol=="q"):
         break


