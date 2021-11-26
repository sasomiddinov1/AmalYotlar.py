#                     8-dars Royhatlar bilan ishlash

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring!!

davlatlar = ['AQSH', 'Turkiya', 'Xitoy', 'UZB', 'Russiya', 'Kariya']

# Ro'yxatning uzunligini konsolga chiqaring

print(len(davlatlar))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

print(sorted(davlatlar, reverse=True))

# Asl ro'yxatni qaytadan konsolga chiqaring

print(davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring

davlatlar.reverse()
print(davlatlar)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.

davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

sonlar = list(range(120,1200,2))
print(sonlar)

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

print(sum(sonlar))

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring

print(max(sonlar), min(sonlar))

# Ro'yxatdagi elementlar sonini hisoblang

print(len(sonlar))

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

taomlar = ['osh', 'lavash', 'gamburgel', 'makaron', 'hot dog']

# nonushta degan yangi ro'yxatga taomlardan nusxa oling

nanushta = taomlar[:]

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing

nanushta.remove('osh')
nanushta.remove('makaron')
nanushta.remove('hot dog')
nanushta.append('cola')
nanushta.append('mayanez')

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring

print(taomlar)
print(nanushta)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.

nanushta = tuple(nanushta)
# nanushta[0] = "ketchub"



























