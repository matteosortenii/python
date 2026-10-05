#**print("ciao")

#def divisione(n1, n2):
#    if n2 == 0:
#        return None, "divisione impossibile"
#    return n1 / n2, "divisione possibile"

#risultato, stato = divisione(10, 4)
#print(risultato, stato)

#risultato, stato = divisione(10, 0)
#print(risultato, stato)

#def celsius_a_fahrenheit(gradi):
#    return gradi * 9 / 5 + 32

#for c in [0, 25, 100]:
#   print(f"{c}°C corrispondono a {celsius_a_fahrenheit(c)}°F")

#def e_pari(n): 
    #return n % 2 == 0
        
#for n in range(1, 21): 
    #if e_pari(n):
        #print(n, end=" ")

def media(voti):
    if len(voti) == 0:
        return 0
    return sum(voti) / len(voti)

print(media([7, 8, 9]))  # 8.0
print(media([]))         # 0

def pullman_necessari(n):
    pieni = n // 53
    if n % 53 > 0:
        return pieni + 1
    return pieni

for n in [53, 54, 106]:
    print(n, "studenti →", pullman_necessari(n), "pullman")

def statistiche(voti):
    if len(voti) == 0:
        return None, None, None
    return min(voti), max(voti), sum(voti) / len(voti)

minimo, massimo, med = statistiche([6, 9, 7, 5])
print(f"min {minimo}, max {massimo}, media {med}")

print(statistiche([]))