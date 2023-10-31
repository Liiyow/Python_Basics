import os
x="y"
while x=="y" or x=="Y":
    promt=["aqirs hore ","aqris dambe"]
    n=[1.5,0]
    print("_________________________________________")
    for i in promt:
        n.append(float(input("Fadlan soo gali "+i+" : ")))
    if n[3]-n[2]>=30:
        n[1]=((((n[3]-n[2])*n[0])/100)*10)
    print("Waxaa isticmaashay : ",n[3]-n[2]," m3","\nwaxaan lagu dalacay : $"
,(n[3]-n[2])*n[0],"\nwaxaa laga rabaa : $ ",((n[3]-n[2])*n[0])-n[1],"\nDiscount : $",n[1])
    print("_______________________________________________")
    x=input("Ma wadnaa : ")
    os.system("clear")