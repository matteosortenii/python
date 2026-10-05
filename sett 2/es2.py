capitali = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}

def capitale(paese):
    return capitali.get(paese, "non in elenco")

print(capitale("Francia"))
print(capitale("Portogallo"))