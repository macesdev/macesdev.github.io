# Listeyi Alfabetik Olarak Sıralamak

liste1 = ["B","I", "L", "I", "S", "I", "M"]
liste1.sort() # listeyi veri tipine göre (string, int, bool, double, float, char, byte..) sıralar.
# int ve float veri tipinde küçükten büyüğe sıralama yapar
print(liste1)

# Listeyi Tersten Yazdırmak

liste2 = ["B","I", "L", "I", "S", "I", "M"]
liste2.reverse() # listeyi terse döndürür
print(liste2)

# Listede Kaç Tane I Elemeanı Olduğunu Bulunuz

liste3 = ["B","I", "L", "I", "S", "I", "M"]
print(liste3.count("I")) # I verilerini silerek yazdırır.

# Gerekli Harfleri Silerek B,I,L,I,M haline getiriniz.

liste4 = ["B","I", "L", "I", "S", "I", "M"]
liste4.pop(4) # 4. indeksteki elemanı siler.
liste4.pop(4) # 5. indeksteki elemanı tekrar siler (önceki 5. index yani).
print(liste4)

# liste Listesini Alan Listesine Kopyalayarak Ekrana Alan Listesini Yazdırınız.

liste4 = ["B","I", "L", "I", "S", "I", "M"]
listex = liste4.copy() # liste4 verisini listex verisine kopyalar.
print(listex)

# Listenin tüm elemanlarını siliniz

liste5 = ["B","I", "L", "I", "S", "I", "M"]
liste5.clear() # liste elemanlarını siler.
print(liste5)

# L Elemanının Index Numarasını Bulunuz

liste6 = ["B","I", "L", "I", "S", "I", "M"]
print(liste6.index("L")) # verinin index numarasını sorgular (query eder).

# Listeyi Büyükten Küçüğe Sıralayınız

sayilar1 = [35, 26, 81, 64]
sayilar1.sort() # listeyi veri tipine göre (string, int, bool, double, float, char, byte..) sıralar.
# int ve float veri tipinde küçükten büyüğe sıralama yapar
print(sayilar1)

# Listeyi tersten yazdırınız.

sayilar2 = [35, 26, 81, 64]
sayilar2.reverse() # int ve float veri tipinde küçükten büyüğe sıralama yapar
print(sayilar2)

# Listede kaç tane 26 elemanı olduğunu bulunuz.

sayilar3 = [35, 26, 81, 64]
print(sayilar3.count(26)) # liste içindeki 26 verisini sayar

# Listedeki 81 sayısını siliniz.

sayilar4 = [35, 26, 81, 64]
sayilar4.pop(2) # 2 indeksindeki elemanı (81) siler.
print(sayilar4)

# Listenin tüm elemanlarını siliniz.

sayilar5 = [35, 26, 81, 64]
sayilar5.clear() # listedeki tüm elemanları siler
print(sayilar5)

# 64 elemanının indeksini bulunuz.

sayilar6 = [35, 26, 81, 64]
print(sayilar6.index(64)) # 64 elemanının indeksini bulur.

# Listeyi ondalikli_sayilar isimli, elemanları 1.4, 6.8 olan liste ile birleştiriniz.

sayilar7 = [35, 26, 81, 64]
ondalikli_sayilar = [1.4, 6.8]
sayilar7.extend(ondalikli_sayilar) # sayilar7 listesinin içine ondalikli_sayilar listesini ekler.
# ondalikli_sayilar.extend(sayilar7) # ondalikli_sayilar listesinin içine sayilar7 listesini ekler.
print(sayilar7)


#                   MuhammedBFM
#         © 2022 macesdev foundation, Inc.
#               All Rights Reserved


