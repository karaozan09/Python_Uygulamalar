# a 

sayi = int(input("Bir sayı giriniz: "))

for i in range(1, 11):
    print(sayi * i, end=" ")  

# b

sayi = int(input("Bir sayı giriniz: "))

sayi = abs(sayi)

basamak_sayisi = 0

while sayi > 0:
    sayi //= 10 
    basamak_sayisi += 1  

print("Girilen sayı", basamak_sayisi, "basamaklıdır.")

# c 

sayısalDeğerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for sayi in sayısalDeğerler:
    if sayi > 150:  
        break
    if sayi % 5 == 0:  
        print(sayi, end=", ")



# Listeyi while döngüsü ile kontrol etmek
sayısalDeğerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

i = 0

while i < len(sayısalDeğerler):  
    sayi = sayısalDeğerler[i]
    
    if sayi > 150: 
        break
    
    if sayi % 5 == 0: 
        print(sayi, end=", ")
    
    i += 1 

# d 

a = int(input("a değerini giriniz: "))
b = int(input("b değerini giriniz: "))
c = int(input("c değerini giriniz: "))

sayac = 0

for i in range(a, b + 1):
    if i % c == 0:
        sayac += 1  

print(f"{a} ile {b} arasında {c}’ye bölünebilen {sayac} sayı vardır.")

# e

for i in range(1, 100):
    print(f"{i} - {100 - i}")

# f

ip = input("IP adresini giriniz (örn: 192 168 255 252): ")

ip_parçaları = list(map(int, ip.split()))


for _ in range(5):
    ip_parçaları[3] += 1  

    for i in range(3, 0, -1):
        if ip_parçaları[i] > 255:
            ip_parçaları[i] = 0
            ip_parçaları[i - 1] += 1

    print(" ".join(map(str, ip_parçaları)))

