import os,validate
obj=validate.valid()

dic={}
idga=0
def present():
    print("1.Register ")
    print("2. Finance")
    print("3. Attendance")
    x=int(input("Please select one of them : "))
    if x==1:
        School(["Registration","Name","Telphone","address","Age","P.Phone"])
    elif x==2:
        School(["Finance"])
    elif x==3:
        School(["Attendance"])
def id():
    global idga
    idga+=1
    return "xyz"+str(idga)
def try_till_true(reson):
   y=False
   while y!=True:
    if reson=="Telphone":
            y=obj.Phone(int(input("Please Enter ""Telphone"+" : ")))
    elif reson=="Age":
        y=obj.age(int(input("Please Enter ""Age"+" : ")))

def School(List):
    StInfo=[]
    print("_______________Welecome to "+List[0]+"______________")
    for i in range(1,len(List)-1):
        if List[i]=="Telphone" or List[i]=="Age":
            z=try_till_true(List[i])
        if List[i]=="Telphone":
            StInfo.append(z)
        else:
            StInfo.append(input("Please Enter "+List[i]+" : "))
    dic[id()]=StInfo
    print(dic)

x="Y"
while x=="Y" or x=="y":
    present()
    x=input("press y to back the system : ")
    os.system("clear")

