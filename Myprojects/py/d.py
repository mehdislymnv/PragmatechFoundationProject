import start
print(dir(start))


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


""" 
mehsular = []
mehsullar=[]
class Mehsul():
    def __init__(self,_ad,_qiymet,_miqdar):
        self.ad=_ad
        self.qiymet=_qiymet
        self.miqdar=_miqdar
        mehsullar.append(self) 
    def melumatGoster(self):
        print(f'{self.ad} | {self.qiymet} | {self.miqdar}')

    # def elaveEt(self):
    #      mehsullar.append(self) 

def istehsalEt():
    ad=input('Mehsulun adi :')
    qiymet=int(input('Mehsulun qiymeti :'))
    miqdar=int(input('Mehsulun miqdari :'))
    mehsul=Mehsul(ad,qiymet,miqdar)

for say in range(2):
    istehsalEt()

def melumatlariGoster():
    for mehsul in mehsullar:
        mehsul.melumatGoster()
        

emr=input('Mehsullari gormek isteyirsiz mi? Yes/No');

if emr=='Yes':
    melumatlariGoster() """

""" 
marksheet =[]
scoresheet=[]
for i in range(int(input())):
    name=input()
    score=float(input())
    marksheet += [[name, score]]
    scoresheet += [score]

    x=sorted(set(scoresheet))

    for  n, s in sorted(marksheet):
        if s==x:
            print(n)
 """
"""

def print_full_name(first, last):
   if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

print_full_name("mirmehdi","Suleymanov")


class Person:
    def __init__ (self,name,firstname,job):
        self.name=name
        self.firstname=firstname
        self.job=job
        gosder()
        
        
        
    def gosder(self):
         print(f'{self.name} | {self.firstname} | {self.job}')

   
       



p1=Person("mehdi","ssad","IT")

"""
