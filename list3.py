postCodes = [13001, 13002, 13003, 13004, 13055, 13006, 13007, 13008, 13009, 75020]

#print(len(postCodes))

nbCodesParisiens = 0
nbCodesProvince = 0

for code in postCodes:
    if code <= 75999 and code >= 75000:
        nbCodesParisiens += 1
    else:
        nbCodesProvince +=1

print("Nombre de codes postaux parisiens: ", nbCodesParisiens, "/", len(postCodes))
print("Nombre de codes postaux de province: ", nbCodesProvince)