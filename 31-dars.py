# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 20:04:52 2021

@author: SAYFIDDIN
"""

from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")

# avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# print(f"ID: {avto1.get_id()}")
# avto1.add_km(1500)
# print(avto1.get_km())