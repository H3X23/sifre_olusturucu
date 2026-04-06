import random
import string

# Sayıları rastgele seçiyoruz
sayi1 = random.randint(1, 100)
sayi2 = random.randint(1, 100)

# 8 karakterli rastgele harf dizileri oluşturuyoruz
harf1 = "".join(random.choice(string.ascii_letters) for _ in range(8))
harf2 = "".join(random.choice(string.ascii_letters) for _ in range(8))

sifre = f"{sayi1}{harf1}{sayi2}{harf2}"

print("İşte şifren:")
print(sifre)
dosya_ismi =input("şifrenin kaydedileceği dosya ismi (sonuna .txt yaz) : ")
# Şifreyi bir dosyaya kaydetme
with open("dosya_ismi", "a", encoding="utf-8") as dosya:
    dosya.write(f"Yeni Şifre: {sifre}\n")

print("\nŞifre başarıyla kaydedildi!")

