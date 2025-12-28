import random
utilizator = input("""Cum te numesti?
>""")
print("Buna " + utilizator + ", te rugam sa raspunzi cu 't'(True) sau 'F'(False) la urmatoarele intrebari:")
lista_intrebari=[
    ["Este adevarat ca o propozitie este un str?"],
    ["Este adevarat ca lista incepe de la 1?"],
    ["Este adevarat ca Pythonul este usor?"],
    ["Este adevarat ca vine anul nou?"],
    ["Este adevarat ca in Franta este diferit fusul orar?"]
]
for elemente in lista_intrebari[0][0]:
    print(elemente)
    if elemente [0][0] == "t":
        print("corect")

random.shuffle(lista_intrebari)
print(lista_intrebari[0])
