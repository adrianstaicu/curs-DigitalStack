meniu = """1 – Afisare lista de cumparaturi

2 – Adaugare element

3 – Stergere element

4 – Sterere lista de cumparaturi

5 - Cautare in lista de cumparaturi """

print(meniu)

nr_citit=int(input("Introduceti un numar pentru a selecta meniul dorit, si apasati ENTER\n"))

print("Ati selectat",nr_citit)

if nr_citit == 1:
    print("Afisare lista de cumparaturi")
elif nr_citit == 2:
    print("Adaugare element")
elif nr_citit == 3:
    print("Stergere element")
elif nr_citit == 4:
    print("Sterere lista de cumparaturi")
elif nr_citit == 5:
    print("Cautare in lista de cumparaturi")
else:
    print("Alegerea nu exista. Reincercati")
