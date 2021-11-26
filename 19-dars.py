# -*- 19-dars funksiya -*-
"""
Created on Sat Oct 30 16:30:23 2021

@author: SAYFIDDIN
"""

# #Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan 
# #funksiya yozing.

def i_y_t_yil(ism, t_yil=2021):
    print(F"{ism.title()} {2021-t_yil} yilda tugilgan")

i_y_t_yil('khadiya', 16)

# #Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya 
## yozing.

def kv_kub(son):
    print(f"{son} ning kvadrati {son**2} kubi, {son**3} ga teng")
kv_kub(4)

## Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

def juftmi(son):
    """Son juft yoki toq ekanligini tekshiradigan funksiya"""
    if son %2:
        print(f'bu {son} bu toq')
    else:
        print(f'bu {son} juft')
juftmi(546565454245786)
juftmi(4)

# # Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya
# # yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def k_k(k, q):
    if q < k:
        print(f"{k} katta {q} dan {k}>{q}")
    elif q>k:
        print(f'{q} katta {k}dan {k}<{q} ')
    else:
        print(f'{k} bilan {q} teng {k}={q}')
k_k(k=15, q=15) 


## Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing.

def daraja(x, y=2):
    print(f"{x} ning {y}-darajasi {x**y} ga teng")


daraja(5, 2)
daraja(3, 3)
daraja(94, 4)
daraja(6)

# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.

def daraja(x, y=2):
    print(f"{x} ning {y}-darajasi {x**y} ga teng")


daraja(5, 2)
daraja(3, 3)
daraja(94, 4)
daraja(6)


# #Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga 
# # bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.


def bolinish_alomatlari(son):
    for n in range(2, 11):
        if not son % n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")


bolinish_alomatlari(20)



























