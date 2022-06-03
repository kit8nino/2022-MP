import random
import math

print("№", len('Капралова Мария Валерьевна')%5)

def new_a(): #рандомная левая граница
    return float(-random.random()*random.random()*100)

def new_b(): #рандомная правая граница
    return float(random.random()*random.random()*100)

#функция
#(2-x)*e^x=0
def F(x):
    return (2-x)*math.exp(x)



#Метод половинного деления (дихотомии)

def new_c(a, b):
    return float(b+a)/2
    

def find_an_answer(a, b):
    if (F(new_c(a,b))!=0):
        if(F(a)*F(new_c(a,b))<0):
            find_an_answer(a, new_c(a,b))
        else:
            find_an_answer(new_c(a,b), b)
    else:
        print("The answer is: ", new_c(a,b))




#Запуск
find_an_answer(new_a(), new_b())
