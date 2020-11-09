import time

print("******************************************\n  Kullanıcı Kaydolma Programı\n******************************************")


isimsoyisim  = input("İsim Soyisim:")
kullanıcıadı  =input("Kullanıcı Adı:")
parola  =input("Parola:")

bilgiler = [isimsoyisim,kullanıcıadı,parola]

print("Bilgiler Kaydediliyor...")
time.sleep(3)


print("İsim Soyisim: {}\nKullanıcı Adı: {}\nParola: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))


print("Bilgiler Kaydedildi")
