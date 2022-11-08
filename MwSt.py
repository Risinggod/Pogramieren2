userinput_saleri=input("pls input your nettosaleri:")
userinput_saleri=float(userinput_saleri)
#funktion mit defohlt funktionen
def netto_zu_brutto(np, mwst=1.19):
    return np*mwst

print(netto_zu_brutto(userinput_saleri, 1.20))









