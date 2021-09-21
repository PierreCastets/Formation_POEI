'''
*** Exo 3 ***
Ecrire un script python, qui calculera et affichera pour 
chacun des prix le prix TTC
'''
print("*** EXO 3 ***")

prices = [14,100,30,10,8] # prix HT
vat = 20 # 20%
prices_TTC = []

def vatAdding (price, vat):
    return price*(1+vat/100)

for p in prices:
    prices_TTC.append(vatAdding(p, vat))

print(prices_TTC)