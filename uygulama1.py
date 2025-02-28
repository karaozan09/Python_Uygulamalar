import pandas as pd
import numpy as np
import random

#Uygulama 1 - a

veriler = {
    "Gün": ["G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","G11","G12","G13","G14"],
    "HavaDurumu": ["Güneşli","Güneşli","Kapalı","Yağmurlu","Yağmurlu","Yağmurlu","Kapalı","Güneşli","Güneşli","Yağmurlu","Güneşli","Kapalı","Kapalı","Yağmurlu"],
    "Sıcaklık": ["Sıcak","Sıcak","Sıcak", "Ilıman", "Soğuk","Soğuk","Soğuk","Ilıman","Soğuk","Ilıman","Ilıman","Ilıman","Sıcak","Ilıman"],
    "Nem": ["Yüksek","Yüksek","Yüksek","Yüksek", "Normal","Normal","Normal","Yüksek","Normal","Normal","Normal","Yüksek","Normal","Yüksek"],
    "Yağış": ["Seyrek","Aşırı","Seyrek","Seyrek","Seyrek","Aşırı","Aşırı","Seyrek","Seyrek","Seyrek","Aşırı","Aşırı","Seyrek","Aşırı"],
    "Oyun": ["Yok","Yok","Var","Var","Var","Yok","Var","Var","Yok","Var","Var","Yok","Var","Yok"]

}

dataframe = pd.DataFrame(veriler)

dataframe.to_csv("tablo.csv", index=False)

print("Başarılı aşkoo")

#Uygulama 1 - b

dataframe = dataframe.drop(columns=["Sıcaklık"])
dataframe = dataframe.drop(columns=["Nem"])

print(dataframe)

#Uygulama 1 - c
print(dataframe.describe())

#Uygulama 1 - d 

dizi = [[0 for _ in range(4)] for _ in range(3)] 
print(dizi)

dizi_düz = [eleman for satir in dizi for eleman in satir]
print("\nDizi (Tek Boyutlu Liste):", dizi_düz)

yeni_dizi = [dizi_düz[i:i+2] for i in range(0, len(dizi_düz), 2)]

print("\nYeniden Şekillendirilmiş Dizi (6x2):")
for row in yeni_dizi:
    print(row)

#Uygulama 1 - e
dizi1 = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

dizi2 = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

print("Dizi 1:")
for row in dizi1:
    print(row)

print("\nDizi 2:")
for row in dizi2:
    print(row)


dikey_istif = dizi1 + dizi2

print("\nDikey İstif:")
for row in dikey_istif:
    print(row)


yatay_istif = [dizi1[i] + dizi2[i] for i in range(3)]

print("\nYatay İstif:")
for row in yatay_istif:
    print(row)
