def ortalama_hesapla(x):
     x = x[:-1]  
     liste = x.split(':')

     ogrenciAdi = liste[0]

     notlar = liste[1].split(',')
     not1 = notlar[0]
     not2 = notlar[1]
     not3 = notlar[2]

     ortalama = (not1+not2+not3)/3

     if ortalama >= 90 and ortalama <=100 :
         harf = "A"
     elif ortalama >=85 and ortalama <=89 :
         harf = "B1"
     elif ortalama >=80 and ortalama <=84 :  
         harf = "B2" 
     elif ortalama >=75 and ortalama <=79 :  
         harf = "B3"
     elif ortalama >=70 and ortalama <=74 :  
         harf = "C1"
     elif ortalama >=65 and ortalama <=69 :  
         harf = "C2"
     elif ortalama >=60 :  
         harf = "C3"
     else :
         harf = "F1"
    
     return ogrenciAdi + ":" + harf + "\n"

def ortalamalari_oku():
      with open("notlar.txt", "r", encoding="utf-8") as file :
        for x in file :
           print(ortalama_hesapla(x))

def notlari_gir():
      ad = input('Ad: ')
      soyad = input('Soyad: ')
      not1 = input('Not 1: ')
      not2 = input('Not 2: ')
      not3 = input('Not 3: ')

      with open("notlar.txt", "a" , encoding="utf-8") as file :
           file.write(ad +' '+ soyad+ ':'+ not1 + ','+ not2 + ','+ not3 +'\n')
      


while True:
    islem1 = input('1- Notları Oku\n2- Notları Gir\n3- Çıkış\n')

    if islem1 == '1' :
        ortalamalari_oku()
    elif islem1 == '2':
        notlari_gir()
    else:
        break