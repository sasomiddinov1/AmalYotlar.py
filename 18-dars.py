# -*- 18-dars  -*-
"""
Created on Thu Oct 28 21:27:15 2021

@author: SAYFIDDIN
"""
## Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir
# # qabul qilib, yangi ro'yxatga joylang.


# savat =[]
# while True:
#     mahsulot = input("Savatga mahsulot qo'shing:")
#     savat.append(mahsulot)
#     javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
#     if javob != 'ha':
#         break
    
# #e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
 ## Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni
# # so'rang.

# mahsulotlar = {}
# while True:
#     mahsulot = input("Mahsulot nomini kiriting: ")
#     narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
#     mahsulotlar[mahsulot] = narh
#     javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
#     if javob != 'ha':
#         break
# #Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir 
# #mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz 
# #mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda 
# #"Bizda bu mahsulot yo'q" degan xabarni kor'sating.

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")