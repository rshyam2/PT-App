#!/usr/bin/env python3
# Calculation Module for PT_App/main

class Calc():
    def __init__(self, age, skinfolds):
        self.age = age
        self.skinfolds = skinfolds
    def male_fatp(self):
        b_den = (1.10938) - (0.0008267*self.skinfolds)+ (0.0000016*(self.skinfolds**2))
        b_density = b_den - (0.0002574*self.age)
        _bf = (4.570/b_density) - 4.142
        self.body_fat = _bf * 100
        return self.body_fat
    
    def female_fatp(self):
        bden = (1.0994921) - (0.0009929*self.skinfolds)+ (0.0000023*(self.skinfolds**2))
        bdensity = bden - (0.0001392*self.age)
        bf = (4.570/bdensity) - 4.142
        self.bfat = bf * 100
        return self.bfat
        
    def lean_bmass(self, weight, bfp):
        mass = round((weight*(bfp/100)),2)
        lean = weight - mass
        return (lean, mass)

def bmi(weight, height):
    base = ((703*weight)/(height**2))
    _bmi = round(base, 2)
    return _bmi

# usr_a = int(input("Age: "))
# usr_s = int(input("Skinfolds in mm: "))
# c = Calc(usr_a, usr_s)
# print(c.male_fatp())

# usr_w = int(input("Weight: "))
# usr_b = float(input("Body fat: "))
# print(c.lean_bmass(usr_w, usr_b))