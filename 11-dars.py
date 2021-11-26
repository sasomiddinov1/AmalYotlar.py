#                            11-dars Uyga Vazifa

# #Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa
## "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son = float(input("Juft son kiritin>>>"))
# if son%2:
#     print('Bu son juft emas.')
# else:
#     print('Rahmat.')
    

## Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

# yosh = int(input('Yoshingizni nechida?'))
# if yosh <=4 or yosh >= 60:
#     narh  = 0

# elif yosh <= 12:
#     narh = 5000
    
# elif yosh <=18:
#     narh = 10000
    
# else:
#     narh = 20000
# print(F"Chipta {narh} so'm ")

## Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng
# # yoki katta/kichikligi haqida xabarni chiqaring

# x = int(input("Brinchi soningizni kiriting? "))
# y = int(input("Ikkinchi soningizni kiriting? "))
# if x==y:
#     print(F'{x}={y}')
# elif x < y:
#     print(f"{x }<{y}")
# else:
#     print(f"{x} >{y}")
    
## mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi,
# # savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot 
# # kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring 
# # va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
# # "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.


# mahsulotlar = ['olma', 'anor', 'uzum', 'gilos', 'nok','tarvuz','qovun', 'anjir',\
#                'banan', 'kivi',]
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1} mahsulotni qoshing>>> '))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f'Dokonimizdan bunday {mahsulot} bor ')
# else:
#     print(f"Dokonimizdan bunday {mahsulot} yoq ")
    
## Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni
 ## so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar
# # degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.
 # # Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda
#  # bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
    

# mahsulotlar = ['olma', 'anor', 'uzum', 'gilos', 'nok','tarvuz','qovun', 'anjir',\
#                'banan', 'kivi',]
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1} mahsulotni qoshing>>> '))

# bor_mahsulotlar =[]
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
     
# if mavjud_emas:
#     print(f'Dokonimizda quydagi mahsulotlar yoq:')
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print('siz soragan barcha mahsulotlar bor')
    
## foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
 # #Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni
 ## foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda 
 ## bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda
# # "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

# users = ['sayfiddin', 'aziza', 'munisa']

# login= input("Yangi login tanlang>>> ")

# if login in users:
#     print("Bu login band")
    
# else:
#     print(f'Xush kelibsiz {login}')
    
##Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2
## da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")































































