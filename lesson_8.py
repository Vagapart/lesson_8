# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 10:37:13 2021

@author: ИнтелАв
"""

#задание 1
class Data:
    def __init__(self, day):
        self.day =day
        
    @classmethod
    def day_to_int(cls, day):
        list1_2 = day.split("-")
        if cls.ValidDay(list1_2): 
            list1_2 = [int(x) for x in list1_2]
            print("Вы ввели день: {0} месяц: {1} год: {2}".format(list1_2[0], list1_2[1], list1_2[2]))
        
    @staticmethod
    def ValidDay(list1_2):
       
        if len(list1_2) != 3:
            print("Дата не верная, введены не все даныне")
        try:
            if int(list1_2[0]) > 31:
               print("Дата не верная, день не может быть больше 31")
               return False
        except:
            print("Дата не верная, День не правильно заполнен")
            return False
        
        try:
            if int(list1_2[1]) > 12:
               print("Дата не верная, месяц не может быть больше 12")
               return False
        except:
             print("Дата не верная, месяц не правильно заполнен")
             return False
        try:
             int(list1_2[2])
        except:
             print("Дата не верная, год не правильно заполнен")
             return False
        return True

day = input("введите дату в формате dd-mm-yyyy: ")
dat = Data(day)
dat.day_to_int(day)
    

#задание 2
class MDiv:
    @staticmethod
    def div(delimoe, delitel):        
        try:
            return delimoe/delitel
        except ZeroDivisionError:
            print("Попытка деления на 0")
            return 0
  
delimoe = int(input("Введите делимое: "))
delitel = int(input("Введите делитель: "))
print("результат: " + str(MDiv.div(delimoe, delitel)))
   
#задание 3
class str_to_chislo:
    @staticmethod
    def is_int(str1):        
        try:
            i = int(str1)
        except:             
            print("Не удалось преобразовать в число")  
            return False
        return True
    
str1 = "" 
list3 = []   
while str1 != "stop":
    str1 = input("Введите чило, для прекращения введите stop: ")
    if str1 == "stop":
        break
    if str_to_chislo.is_int(str1):
        list3.append(int(str1))    
print("результат: " + str(list3)) 

#задание 4, 5, 6
class Sklad:
    name = ""
    Technika = {}
    def __init__(self, name):
        self.name = name
    
    def Prinyat(self, tech, count):
        kol = self.Technika.get(tech)
        if kol == None:
            self.Technika[tech] = count
        else:
            self.Technika[tech] = count + kol
        print("На склад {0} приняли {1} в количестве {2} штуки".format(self.name, tech.name, count))
    
    def Peredat(self, tech, count, podr):
        kol = self.Technika.get(tech)
        if kol == None:
            print("Техники на складе нет")
        else:
            self.Technika[tech] = kol - count
        print("C склада {0} списали {1} в количестве {2} штуки в подразделение {3}".format(self.name, tech.name, count, podr))
    
    def Ostatok(self):
        print("Остатки")
        for key in self.Technika.keys():
            print("{0} - {1}".format(key.name, str(self.Technika[key])))
        
class OrgTech:
    weight = 0
    lenght = 0
    height = 0
    name = ""
    def __init__(self, *args):
       self.name = args[0]
       self.lenght = args[1]
       self.height = args[2]
       self.weight = args[3]
    def __str__(self):
        print(self.name)
       
class Printer(OrgTech):
    speedOfPrint = 0
    def __init__(self, *args):
       OrgTech.__init__(self, args[0], args[1], args[2], args[3])
       self.speedOfPrint = args[0]
    
class Scaner(OrgTech):
    speedOfScan = 0
    def __init__(self, *args):
        OrgTech.__init__(self, args[0], args[1], args[2], args[3])
        self.speedOfScan = args[0]
     
class Xerox(OrgTech):
    speedOfScan = 0  
    speedOfPrint = 0
    def __init__(self, *args):
       OrgTech.__init__(self, args[0], args[1], args[2], args[3])
       self.speedOfScan = args[0]
       self.speedOfPrint = args[1]
   
skladObuhovo = Sklad("Обухово")

prHP = Printer("lazrJet", 1, 1, 1, 10)
prSumsung = Printer("Samsung", 1, 1, 1, 20)

scHP = Scaner("scan bst", 1, 1, 1, 10)

xerHP = Xerox("Xer 123", 1, 1, 1, 20, 10)

skladObuhovo.Prinyat(prHP, 5)
skladObuhovo.Ostatok()
skladObuhovo.Peredat(prHP, 2, "Ш. Энтузиастов")
skladObuhovo.Ostatok()
skladObuhovo.Prinyat(prSumsung, 5)
skladObuhovo.Ostatok()
skladObuhovo.Prinyat(prSumsung, 3)
skladObuhovo.Ostatok()
skladObuhovo.Peredat(prSumsung, 2, "Ш. Энтузиастов")
skladObuhovo.Ostatok()
skladObuhovo.Prinyat(scHP, 3)
skladObuhovo.Ostatok()
skladObuhovo.Prinyat(scHP, 1)
skladObuhovo.Ostatok()
skladObuhovo.Prinyat(xerHP, 6)
skladObuhovo.Ostatok()
skladObuhovo.Peredat(xerHP, 3, "Марьино")
skladObuhovo.Ostatok()
skladObuhovo.Peredat(scHP, 2, "Кузьминки")
skladObuhovo.Ostatok()



# Задание 7
class ComplNum:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, sum2):
        return ComplNum(self.real + sum2.real, self.imaginary + sum2.imaginary)    
        
    def __mul__(self, umn2):
        return ComplNum(self.real * umn2.real - self.imaginary * umn2.imaginary, self.real * umn2.imaginary + self.imaginary * umn2.real)    
        
    def __str__(self):
        znak = "-" if self.imaginary < 0 else "+" 
        return (f"{str(self.real)} {znak} {str(abs(self.imaginary))}i")
        
k1 = ComplNum(1, 3)
print(k1)       
k2 = ComplNum(2, -3) 
print(k2)       
print(k2 + k1) 
print(k2 * k1) 
#проверил. все правильно


























    
    
    
    
    
    
    
    
    
    