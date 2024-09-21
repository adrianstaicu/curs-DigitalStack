nr_citit=int(input("Introduceti numarul\n"))

if nr_citit>0 and nr_citit<10:
    print("Numarul este pozitiv")
elif nr_citit == 0:
    print("Numarul este ", nr_citit)
else:
    print(nr_citit * -1)


