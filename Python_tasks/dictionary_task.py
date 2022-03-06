dict={
"name": "Plato",
"country": "Ancient Greece",
"born": -427,
"teacher": "Socrates",
"student": "Aristotle"}
# Verilen dictionary-e esasen asgidaki suallari cavablandirmaq ucun ekrana sualin cavabiniz yazdirin.
# Bunun ucun userden input alin. Eger user “born”, “when” sozlerini daxil etse program texmin etsin ki
# user ne sorushmaq isteyir. Meselen born ve when sozleri varsa cumlede user cox guman ki 
# “When was Plato born?” sualina cavab axtarir. Proqram o sozleri gorub sorushsun ki,
# “Maybe did you mean “When was Plato born?” “. Bu suali sorushduqda yes ve no secimleri verin.
# Eger yes yazsa dictionarydeki datadan istifade ederek Platonun doguldugu ili usere gosterin.
# Meselen country daxil etse proqram texmin etsin ki user platonun doguldugu yeri axtarir ve siz de
# ele proqram yazin ki ona uygun cavab qaytarin. Eger mentiqsiz soz daxil edilse not found verin ekrana.
user_input=input("")
x=dict["born"]
y=dict["country"]
z=dict["name"]
v=dict["teacher"]
w=dict["student"]

if user_input ==x:
    print("Maybe did you mean “When was Plato born?")
elif user_input ==y:
    print("Maybe did you mean “Which country did he live?")
elif user_input ==z:
    print("Maybe did you mean “What is his name?")
elif user_input ==v:
    print("Maybe did you mean “Who is his teacher?")
elif user_input ==w:
    print("Maybe did you mean “Who is his student?")
    user_answer=input("Yes")
    if user_answer ==True:
        print(x)
    else:
        print("NOT FOUND")