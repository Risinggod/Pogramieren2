user_input_brutto=input("ride_down_your_bruttosaleri")
user_input_brutto=float(user_input_brutto)
def brutto_to_netto(brutto, Mwst=1.19):
    return brutto/Mwst

print(round(brutto_to_netto(user_input_brutto),2))

