
# Online Python - IDE, Editor, Compiler, Interpreter
class IcecreamStore:
    def __init__(self,IcecreamStoreName,IcecreamList):
        self.IcecreamStoreName=IcecreamStoreName
        self.IcecreamList=IcecreamList
        
    def findMinimunIcecreamByPrice(self):
        if(self.IcecreamList is None or self is None):
            return "No Data Found"
        m=self.IcecreamList[0]
        for i in self.IcecreamList:
            if (i.price <m.price):
                m=i
        return m
            
    def sortIcecreamByid(self):
        if(self.IcecreamList is None or self is None):
            return "No Data Found"
        
class Icecream:
    def __init__(self,id,price,name,quantityInGms,category):
        self.id=id
        self.price=price
        self.name=name
        self.quantityInGms=quantityInGms
        self.category=category
     

IcecreamList=[]
noOfIcecream=int(input())
for i in range(n):
    id=int(input())
    price=int(input())
    name=input()
    quantityInGms=int(input())
    category=input()
    IcecreamList.append(Icecream(id,price,name,quantityInGms,category))
IcecreamStoreName=''
icecreamStore=icecreamStore(IcecreamStoreName,IcecreamList)
print(icecreamStore.findMinimunIcecreamByPrice())
print(icecreamStore.sortIcecreamByid())
    

