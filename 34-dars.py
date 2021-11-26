# -*- 34-dars-*-
"""
Created on Tue Nov 23 13:18:50 2021

@author: SAYFIDDIN
"""

import json


# Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring: 
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

json_data = json.dumps(data, indent=4)
print(json_data)
print(type(json_data))

# Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring: 
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
talaba = json.dumps(talaba_json)

talaba = json.loads(talaba_json)
print(f"{talaba['ism']} {talaba['familiya']}")

# Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang

with open('PYTHON/33-dras','w') as f:
    json.dump(data,f)
 