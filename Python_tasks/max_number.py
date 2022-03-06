#Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.
first = int(input("Birinci ededi daxil edin:"))
second = int(input("Ikinci ededi daxil edin:"))
three = int(input("Ucuncu ededi daxil edin:"))
fourth=int(input("Dorduncu ededi daxil edin:"))

if (first >=second ) and (first >= three ):
    max_number= first
elif (second >= first) and (second >= three):
    max_number= second
elif (three >= first) and (three >= second):
    max_number= second
else:
    max_number= fourth
print(max_number ,"is a biggest number")  

