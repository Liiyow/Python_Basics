# aqri hore  aqri dambe heer firqi la isticmaalay qaanta qof 30 0.1
import os
x="y"
while x=="y" or x=="Y":
    print("_______________________________________________")
    aqirh=float(input("Fadlan Soo gali aqris hore : "))
    aqrid=float(input("Fadlan Soo gali aqris dambe : "))
    Heer=1.5
    farqi=aqrid-aqirh
    discount=0
    if farqi>=30:
        discount=((farqi*Heer)/100)*10
    qaant=(farqi*Heer)
    print("Waxaa isticmaashay : ",farqi," m3","\nwaxaan lagu dalacay : $"
        ,qaant,"\nwaxaa laga rabaa : ",qaant-discount,"\nDiscount : $",discount)
    print("_______________________________________________")
    x=input("Ma sii wadana program ka : ")
    os.system("clear")
