# Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlugu 3-dən kiçik 11-dən böyük
# ola bilməz.Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik,
# 15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin.
# Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. 
# Emailin uzunluğu 10 hərfdən qısa 22 hərfdən uzun olmasın, tərkibində @gmail.com olsun və
# bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. 
# Parol 6-13 simvol aralığında olmalıdır. Sonra parolu təsdiqləməyini tələb edin. 
# Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. Bütün bunlar düzgün daxil edilərsə,
# Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib
# istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin: 
# (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə,hər verdiyiniz
# şərtə uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə,
# mesaj verilsin ki 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin.
# ============================================= Ad: Murad Soyad: Əliyev Yaş: 22
# Email: muradaliyev1996@gmail.com Parol: 123456789 ============================================= 
# Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın


name =input("Adinizi daxil edin__")
if len(name) > 3 and len(name) < 11:
    surname=input("Soyadinizi daxil edin__")
    if len(surname) > 5 and len(surname) < 15:
       born_year=input("Dogum ilinizi daxil edin__")
       if int(born_year) >= 4:
            yas=2022-int(born_year)
            email=input("Email-inizi daxil edin__")
            if len(email) > 10 and len(email) < 22:
                password= input("Parolunuzu daxil edin__")
                if len(password) > 6 and len(password) < 13:
                    tekrar_password=input("Parolunuzu tekrar yazin__")
                    if tekrar_password == password:
                        print("Qeydiyyat tamamlandi! Qeydiyyatinizin detallari ile tanis olmaq isterdinizmi?")
                        user_answer=input("")
                        if user_answer=="He":
                           print(f"Ad: {name}\n Soyad:{surname}\n Yas: {yas}\n Yas: {born_year}\n Email: {email}\n Parol: {password}\n ")
                        else:
                            print(f"{name} {surname} ugurlar!")
                    else:
                        print("Parolun tekrari dogru olmadi!")
                else:
                    print("Parol 6 simvoldan kicik, 13 herfden uzun ola bilmez!")
            else:
                print("Email 10 simvoldan kicik, 22 simvoldan uzun ola bilmez!")
       else:
            print("Dogum ili 4 simvoldan kiçik ola bilmez!.") 
    else:
        print("Soyadın uzunlugu 5-dən kiçik, 15-dən böyük ola bilməz!") 
else:
    print("Adın uzunlugu 3-dən kiçik, 11-dən böyük ola bilməz!")