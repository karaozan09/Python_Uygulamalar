#a

a = int(input("1. Açıyı gir: "))
b = int(input("2. Açıyı gir: "))
c = int(input("3. Açıyı gir: "))


if a + b + c != 180:
    print("Geçersiz üçgen! Açıların toplamı 180° olmalıdır.")
else:
    if 90 in (a, b, c):
        print("Bu bir DİK üçgendir.")
    elif a > 90 or b > 90 or c > 90:
        print("Bu bir GENİŞ üçgendir.")
    else:
        print("Bu bir DAR üçgendir.")

# b

uzayli_rengi = input("Uzaylının rengini giriniz (kırmızı, yeşil, sarı): ")


if uzayli_rengi.lower() == "yeşil":
    print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız.")
else:
   
    print("Tebrikler, yeşil olmayan uzaylıya ateş ettiğiniz için 10 puan kazandınız.")

# c

uzayli_rengi = input("Uzaylının rengini giriniz (kırmızı, yeşil, sarı): ")


if uzayli_rengi.lower() == "yeşil":
    print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız.")
elif uzayli_rengi.lower() == "sarı":
    print("Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız.")
elif uzayli_rengi.lower() == "kırmızı":
    print("Tebrikler, kırmızı uzaylıya ateş ettiğiniz için 15 puan kazandınız.")
else:
    print("Geçersiz renk! Lütfen kırmızı, yeşil veya sarı renklerinden birini giriniz.")

# d 


yas = int(input("Yaşınızı giriniz: "))


if yas < 2:
    print("Bu kişi bebektir.")
elif 2 <= yas < 4:
    print("Bu kişi yeni yürümeye başlayan çocuktur.")
elif 4 <= yas < 13:
    print("Bu kişi çocuktur.")
elif 13 <= yas < 20:
    print("Bu kişi ergendir.")
elif 20 <= yas < 65:
    print("Bu kişi yetişkindir.")
else:
    print("Bu kişi yaşlıdır.")


# e 

favori_meyveler = ["elma", "armut", "kavun", "muz", "çilek"]

meyve = input("Bir meyve giriniz: ").lower()

if meyve in favori_meyveler:
    print(f"{meyve.capitalize()} favori meyvelerimden biridir!")
else:
    print(f"{meyve.capitalize()} favori meyvelerim arasında yer almıyor.")

