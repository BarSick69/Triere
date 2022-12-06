x=int(input("Dati primul numar: "))
y=int(input("Dati al doilea numar: "))
check=True
check1=True
x_s=str(x)
y_s=str(y)
for chars in x_s:
    if chars not in y_s:
        check=False
        break
for chars in y_s:
    if chars not in x_s:
        check1=False
        break
if(check1 and check):
    print("Prietene")
else:
    print("Nu sunt prietene")


