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
if len(name) > 11 and len(name) < 3:
    surname=input("Soyadinizi daxil edin__")
    if len(surname) > 5 and len(surname) < 15:
        email=input("Email-inizi daxil edin__")
        if len(email) > 10 and len(email) < 22:

    else:
        print("Soyad 5 hərfdən kiçik,15 hərfdən uzun olmasın.") 
else:
    print("Adın uzunlugu 3-dən kiçik, 11-dən böyük ola bilməz.")