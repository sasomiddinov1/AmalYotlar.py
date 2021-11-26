# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:43:08 2021

@author: SAYFIDDIN
"""
## Yuqoridagi funksiyaga uchinchi, qadam deb nomlangan ixtiyoriy parameterni qo'sha olasizmi?
# def oraliq(min,max):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += 2
#     return sonlar

# print(oraliq(1,20, ))
# print(oraliq(10,21))

## Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
## Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.


# def malumot_info(ism, familiya, oismi, tyil, tjoy, email='', tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya """
#     mijoz ={
#         "ism": ism,
#         "familiya": familiya,
#         'oismi': oismi,
#         "tyil": tyil,
#         "yoshi": 2020 - tyil,
#         "tjoy": tjoy,
#         "email": email,
#         "telefon": tel,
#         }
#     return mijoz


# print("Mijoz haqida malumot kiriting.")

# mijozlar = []

# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     oismi = input("Otchisvo: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(malumot_info(ism, familiya, oismi, tyil, tjoy,  email, telefon))
#     javob = input("Davom etasizmi (ha/yoq)")
#     if javob != 'ha':
#         break


# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(
#         f"{mijoz['ism'].title()} {mijoz['familiya'].title()}  {mijoz['oismi'].title()} o'gli', "
#         f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
#         )


## №Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

# def kattasi(x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return 

# print(max( 5, 4, 3, 5165368))

## Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing


# def aylana_info(radius, pi=3.14159):
#     aylana = {
#         "radius": radius,
#         "diametr": 2 * radius,
#         "perimetr": 2 * radius * pi,
#         "yuza": pi * radius ** 2,
#     }
#     return aylana

# print(aylana_info(15))


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar
print(fibonacci(15))
# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

























    











































