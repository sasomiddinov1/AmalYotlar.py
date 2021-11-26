#                               7-dars List
# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

# ismlar = ['Lazizbek', 'Javohir', 'jasur']

## Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
    
# print('Bugun kochaga chiqadiganla bormi?', ismlar[1],'san chiqasanmi.')
# print(f'{ismlar[0]} San kecha chaqirding mani {ismlar[1]} ham bor chiq.' )
# print(ismlar[-1], "yaxshi bola")

## sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 

# sonlar = [10, 20.5, 2004, -56, -69.0, 123_654_987, 478.5,]


## Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. 
## Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.

# sonlar[0] = sonlar[0]+sonlar[2]
# sonlar[-2] = 0
# sonlar[-1] = 25+25
# del sonlar[-3]
# sonlar[-3] = 57.0
# print(sonlar)

# #t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat
## qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.

# t_shaxs = ['Amir Temur', 'Lev Talstoy', 'Suxrot']
# z_shaxs = ['Bil Geys', 'Ilon Mask', "Sayfiddin"]
# print(f'Men Tarix shaxslardan {t_shaxs.pop(-1)} bilan zamonaviy\nshaxslardan esa {z_shaxs.pop(1)} bilan suxbatlashgan bilardim')

## friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta
# # mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

dostlar = []
dostlar.append('Javlon')
dostlar.append('Said')
dostlar.append('Jonny')
dostlar.append('Lazizbek')
dostlar.append('Jasur')
dostlar.append("aziz")
print(dostlar)

## Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove()
# # metodi yordamida o'chrib tashlang

dostlar.remove('Jonny')
dostlar.remove('aziz')
print(dostlar)

# # Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

dostlar.append('akmal')
dostlar.insert(0, 'Hasan')
dostlar.insert(3, 'Xusan')
print(dostlar)

# # Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append()
# # metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan
# # sug'urib olib, mehmonlar ro'yxatiga qo'shing.

mehmonlar = []
mehmonlar.append(dostlar.pop(-1))
mehmonlar.append(dostlar.pop(3))
mehmonlar.append(dostlar.pop(1))
mehmonlar.append(dostlar.pop(-4))

print("Kelgan mehmonlar", mehmonlar)







