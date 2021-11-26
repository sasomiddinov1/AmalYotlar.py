a = int(input("a: "))
b = int(input("b: "))
print("""
1 - qo'shish
2 - ayirish
3 - ko'paytirish
4 - bo'lish
""")

option = input("Sizning tanlovingiz: ")

if option == "1":
    print(a+b)

elif option == "2":
    print(a-b)

elif option == "3":
    print(a*b)
elif option == "4":
    print(a/b)
else:
    print("Notog'ri tanlov") 
    