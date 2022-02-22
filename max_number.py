#Write a Python function to find the Max of three numbers. Go to the editor
number = 1
first = int(input("Birinci ededi daxil edin:"))
second = int(("Ikinci ededi daxil edin:"))
three = int(input("Ucuncu ededi daxil edin:"))

def find_max_number():
    if first > number:
        number = first
    elif second > number:
        number = second
    elif three > second:
        number = three
        print("Neticede en boyuk eded:")
    else:
        print("Melumat duzgun daxil edilmeyib!")
find_max_number()