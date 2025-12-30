import random

# Inceputul aplicatiei Quiz

print("Quiz app")
utilizator = input("""Cum te numesti?
""")
print("Bine ai venit " + utilizator + " instructiunile sunt urmatoarele:")
print(utilizator + ", te rog sa raspunzi cu 't'(True) sau 'F'(False) la urmatoarele intrebari")
print("Scorul final va fi afisat")

# Lista de intrebari care se adauga una dupa cealalta

lista_intrebari=[]
lista_intrebari.append(["Este adevarat ca o propozitie este un str?","T"])
lista_intrebari.append(["Este adevarat ca lista incepe de la 1?","F"])
lista_intrebari.append(["Este adevarat ca Pythonul este usor?","F"])
lista_intrebari.append(["Este adevarat ca vine anul nou?","T"])
lista_intrebari.append(["Este adevarat ca in Franta este diferit fusul orar?","T"])

scor = 0

# Afiseaza intrebarile utilizatorului si ii cere un raspins

for intrebare in lista_intrebari:
    print()
    print(intrebare[0])
    print()
    raspuns = input (":")
    if raspuns.upper() [0] == intrebare[1]:
        scor = scor + 1
        print("corect")
    else:
        print("incorect")
print (scor)

# nu am stiut cum sa folosesc random va trebui sa reincerc
# random.shuffle(lista_intrebari)
# print(lista_intrebari[0])
