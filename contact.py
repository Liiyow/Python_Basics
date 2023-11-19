import os
class con:
    def __init__(self):
        self.dic={}
        self.show(["1. Add New Phone","2. Edit Phone ","3. Delete Phone","4. show All"])
    def show(self,M):
        x="y"
        while x=="y" or "Y":
            for i in M:
                print(i)
            try:
                y=int(input("Please choose one of them : "))
            except:
                y=int(input("Please choose one of them : "))
            if y==1:
                self.Add(["Add New Phone","Name","Tell"])
            if y==2:
                self.Edit(["Edit the Phone","Name","Tell"])
            elif y==4:
                self.prin()
            elif y==3:
                self.delete()
            x=input("press y to contuinue : ")
            os.system("clear")
    def Add(self,List):
        detials=[]
        print("______welecome here to "+List[0]+"____________________")
        for i in range(1,len(List)):
            detials.append(input("Enter the "+List[i]+" : "))
        try:
            if self.dic[detials[1]]=="":
                pass
            print("This number already existed")
        except:
            self.dic[detials[1]]=detials[0]
            print("New Phone is added")
    def delete(self):
        phone=input("Enter the phone : ")
        del self.dic[phone]
        print("this phone " +phone+" was deleted ")
    def Edit(self,List):
        self.prin()
        detials=[]
        print("______welecome here to "+List[0]+"____________________")
        for i in range(1,len(List)):
            detials.append(input("Enter the "+List[i]+" : "))
        for i in self.dic.keys():
            if i==detials[1]:
                self.dic[detials[1]]=detials[0]
                print("The phone updated")
            else:
                print("This number is not exisit")
        
            
    def prin(self):
        print("Name       \t \t \t"+" Telphone")
        for i in self.dic:
            print(self.dic[i]+"\t \t \t"+i)

# x=con()