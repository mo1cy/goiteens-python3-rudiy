president_termin_limit = 4
print("Enter president termin in years: ")
president_termin = int(input())
if president_termin <= president_termin_limit*2:
    print("President termin ", president_termin, " years is valid")
else: print("President can't hold a position if the total position termin is more then 2 termins")
