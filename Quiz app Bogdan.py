import random

# Instructiuni + Welcome

print("QUIZ APP")
nume= input("Numele tau:")
print("Bine ai venit " + nume + ", instructiunile sunt urmatoarele:")
print("Raspunzi cu 't'(True) sau 'F'(False) la urmatoarele intrebari")
print("Scorul final va fi afisat")

# Intrebarile sunt pe pozitia 0 ,raspunsul corect este pe pozitia 1

lista_intrebari=[]
lista_intrebari.append(["Cerul este albastru","T"])
lista_intrebari.append(["Modulul actual este Intro in Testare","F"])
lista_intrebari.append(["Python este un limbaj de programare","T"])
lista_intrebari.append(["Itschool.ro este site'ul IT school","T"])
lista_intrebari.append(["Bogdan este programator","T"])

# Amestecam lista de intrebari 
random.shuffle(lista_intrebari)
print("Sunt " + str(len(lista_intrebari))+ " intrebari in Quiz.")

# numaram intrebarile
# numar_intrebari = 0
# for intr in lista_intrebari:
#     numar_intrebari +=1
# print(numar_intrebari)

# aici setam scorul initial
scor = 0

for intrebare in lista_intrebari:
    print()
    print("="*30)
    print(intrebare[0])
    raspuns = input (">")
    if raspuns.upper() [0] == intrebare[1]:
        scor = scor + 1
        print("corect")
    else:
        print("incorect")

print()
# if scor == 0:
#     print("Scorul tau este 0 ,ne pare rau, te rugam sa mai incerci")

# else:
    # if scor == 5:
    #     print("Felicitari , ai atins punctajul maxim")
    # else:
    #     print("Scorul tau este " + str(scor) + ". Felicitari.")
if scor == 0:
    print("Scorul tau este 0 ,ne pare rau, te rugam sa mai incerci")
elif scor<=4:
    print("Scorul tau este " + str(scor) + ". Felicitari.")
else:
    print("Felicitari , ai atins punctajul tau maxim")