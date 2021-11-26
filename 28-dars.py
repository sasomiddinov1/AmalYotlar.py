# -*- 28-dars -*-
"""
Created on Sat Nov 13 12:26:34 2021

@author: SAYFIDDIN
"""

# #Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari 
## sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting 
# #(ism, foydalanuvchi ismi, email, va hokazo)


class user:
    def __init__(self, ism, familya, tyil, email, traqam):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
        self.email = email
        self.traqam = traqam
## Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
    def get_ism(self):
        return self.ism
    
    def get_familya(self):
        return self.familya
    def get_tyil(self,yil):
        return yil-self.tyil
    def get_email(self):
        return self.email
    def get_nomer(self):
        return self.traqam
## Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).        
    def get_info(self):
     
        print(f"Foydalanuvchi: Ismi {self.ism} Familyasi {self.familya} yoshi {self.tyil} email {self.email} telefon raqami {self.traqam}")


user1 = user("Sayfiddin", "Asomiddinov", 2004, "sayfiddina53@gmail.com", 998999207677)
print(user1.get_info())
print(user1.get_tyil(2021))
print(user1.get_familya())
print(user1.get_email())
print(user1.get_ism())
print(user1.get_nomer())        