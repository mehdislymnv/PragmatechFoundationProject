""" 
for i in range(101):
    if i%2==1:
        print(i)
     """
#cem=0

#2
# for i in range(101):
    
#    if i%2==1:
#        cem+=i
# print (cem)
#3     
"""
cumle="Javascript ne vaxtdan proqramlasdirma dili olub?"

a=cumle.split()
cem=0
for i in a:
    cem+=len(i)
print(cem)

#5

soyad="Suleymanov"[::-1]
print(soyad)
"""
#4
""" 
cumle="Javascript ne vaxtdan proqramlasdirma dili olub?"
a=cumle.split()
print(len(a))
 """

#6
"""
sait=["a","e","i","o","u"]
cumle="Javascript ne vaxtdan proqramlasdirma dili olub?"

say=""
for i in sait:
    for j in cumle:
        if i==j:
            say += i
print(say)"""

""" a=input("Adinizi girin : ")

print("salam {}  ".format(a)) """


""" s=[50,35,"a"]
cem=0
for i in s:
    if type(i)==str:
        print("prablem var")
    else:
      cem+=i
print(cem) 


"""



""" a=[25,33,0,40,30]
b=[10,25,33,5,10]

def tap():
    for i in a:
        if i in b:
            return True
        else:
            return False
               
    
     

print(tap()) """

""" a=45321
c=str(a)
cem=0
for i in c:
    cem+=int(i)
print(cem)


num = 45342
sum=0
while num>0:
    qaliq = num%10 
    num = num//10 
    sum+=qaliq 
print(sum)
 """
""" 
import random
lista=["Mehdi","Fikret","Emin","Nicat"]

random.shuffle(lista)
  



print(lista)
list = ['Red', 'Blue', 'Green', 'White', 'Black']

print(random.choice(list)) """

N = int(input(" : "))
arr= [] 
arr.insert(0,N)
print(arr)
