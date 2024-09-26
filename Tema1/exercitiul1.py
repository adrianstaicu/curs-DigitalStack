nume = input("Introduceti numele vostru:")
text = input("Introduceti un text:")
if text.isalpha():
    print(f"Sirul de caractere a fost gasit de {nume}.")
elif text.isdigit():
    print("Este un sir de numere.")
else:
    print("Textul contine litere si cifre.")






