# Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun.
# Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin 
# qiymətini yazdırın.(İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə,
# ekrana error mesajı verin.

fruits=["apple","cherry","ananas","pear","banana"]
price=["1 AZN", "4 AZN", "7 AZN", "5 AZN", "3 AZN"]
user_input=input("Bir meyve secin __")
for i in range(len(fruits)): 
    if user_input==fruits[i]:
       print(user_input ,price[i])
    break