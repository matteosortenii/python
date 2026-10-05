def senza_duplicati(elementi):
    visti = set()
    risultato = []
    for i in elementi:
        if i not in visti:
            visti.add(i)
            risultato.append(i)
    return risultato

nomi = ["Sara", "Luca", "Sara", "Marco", "Luca", "Giulia"]
print(senza_duplicati(nomi))