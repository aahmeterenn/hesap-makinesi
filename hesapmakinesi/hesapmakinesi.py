
while True:
    
    try:
        print("Sayi giriniz(Çıkmak için boş bırakın): ")
        sayi1 = float(input())
        print("İkinci sayiyi giriniz(Çıkmak için boş bırakın): ")
        sayi2 = float(input())
        print("İşlemlerden birini seçiniz: +, -, *, /, **")
        islem = str(input())
    except ValueError:
            print("Sayi biçiminde giriş yapılmadı, program kapatılıyor")
            break
    
    if (islem == "+"):
        sonuc = sayi1 + sayi2
        print(f"Toplam: {sonuc}")

    elif(islem == "-"):
        sonuc = sayi1 - sayi2
        print(f"Kalan: {sonuc}")

    elif(islem == "*"):
        sonuc = sayi1 * sayi2
        print(f"Çarpım: {sonuc}")

    elif(islem == "/"):
        sonuc = sayi1 / sayi2
        print(f"Bölüm: {sonuc}")
        
    elif(islem == "**"):
        sonuc = sayi1 ** sayi2
        print(f"Sonuç: {sonuc}")  

    
    

   
        



