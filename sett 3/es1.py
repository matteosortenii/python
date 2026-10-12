def salva_appunto(testo):
    with open("appunti.txt", "a", encoding="utf-8") as file:
        file.write(testo + "\n")

salva_appunto("Primo appunto")
salva_appunto("Secondo appunto")
salva_appunto("Terzo appunto")

with open("appunti.txt", "r", encoding="utf-8") as file:
    for numero, riga in enumerate(file, start=1):
        print(f"{numero}. {riga.rstrip()}")