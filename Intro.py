# nume = "Mihail"
# nume = "Maria"
# print(nume)

#mai sus am printat ceva
#Comentarile sunt bune pentru developeri pentru a documenta codul

# text1 = 'Aici pot scrie un "text" simplu'
# text2 ="Mihail's bike is blue"
# text3 = """aici
# putem
# scrie
# pe
# mai
# multe
# linii"""
# print(text1)
# print(text2)
# print(text3)

# Sa scriem o poezie cu Titlu, Autor si o strofa

# Eminescu = """Mihai Eminescu
#         Adio
#     De-acuma nu te-oi mai vedea,
#     Rămâi, rămâi, cu bine!
#     Mă voi feri în calea mea
#     De tine.
# """
# print(Eminescu)

# titlu = "               Adio        "
# autor = "Mihai Eminescu"
# strofa = """        De-acuma nu te-oi mai vedea,
#         Rămâi, rămâi, cu bine!
#         Mă voi feri în calea mea
#         De tine.
#            """
# print(titlu)
# print(autor)
# print(strofa)

# numar_intreg = 5 
# print(numar_intreg)
# numar_zecimal = 5.5
# print(numar_zecimal)

# print("Numele tau care este?")
# nume = input("Scrieti aici numele> ")
# print("Ma bucur sa te cunosc ")
# print(nume)

# text1 = "Mihai merge"
# text2 = "la mare"
# # print (text1 + " " + text2)
# text3 = text1 + " " + text2
# print(text3)

# text = """It School
# """
# print(text*10)

# #Adunarea
# print(7+8)

# #Scaderea
# print(10 - 3)

# #Inmultire
# print(5 * 2)

# #impartire
# print(5 / 2 )
# print(5 // 2)

# print('testing Python')
# print('itschool rooookc')

# text = 'Python'
# numar_intreg = 20
# numar_zecimal = 5.6

# print(type(text))
# print(type(numar_intreg))
# print(type(numar_zecimal))

# print(type(numar_intreg))
# # numar_intreg = str(numar_intreg)
# numar_intreg_convert_to_string = str(numar_intreg)
# print(type(numar_intreg_convert_to_string))

# varsta = 20
# nume = 'Mihail'
# print(nume + ' are ' + str(varsta) + ' ani ' )

# text = "30"
# print(int(text) + 10)

#cerem utilizatorului varsta
#calculam si anuntam cati ani mai are de trait pana la 100 de ani

#Varianta mea
# print("""Buna
#       Cum te numesti?""")
# nume = input("Nume :")
# print("Cati ani ai?")
# varsta = input ("Varsta :")

# varsta = int(varsta)
# # print(nume + " mai ai de trait")
# rezultat= 100 - varsta 
# rezultat_str = str(rezultat)
# print(nume + ' mai ai ' + rezultat_str + ' ani de trait ')

#Vrianta lui Bogdan

# nume = input("Nume : ")
# varsta_str = input('Varsta : ')
# varsta_int = int(varsta_str)
# rezultat = 100 - varsta_int
# rezultat_str = str(rezultat)

# print(' Salut ' + nume + ', mai ai de trait ' + rezultat_str + ' de ani pana la 100.')

# nume = "Mihail"
# #       012345
# print(nume[0])
# print(nume[1])
# print(nume[2])
# print(nume[3])
# print(nume[4])
# print(nume[5])

# nume= "Mihail"
# print(len(nume))

# list_cumparaturi = [ "mere" , "oua" , "lapte"]
# lista_cumparaturi = [
#     "mere",
#     "oua",
#     "lapte"
# ]
# lista_preturi=[
#     5,
#     6,
#     8
# ]
# # print(lista_cumparaturi[0])
# # print(lista_preturi[0])
# print(" Pretul pemtru " + lista_cumparaturi[0] + " este de " + str(lista_preturi[0]) + " lei.")
# print(" Pretul pemtru " + lista_cumparaturi[1] + " este de " + str(lista_preturi[1]) + " lei.")
# print(" Pretul pemtru " + lista_cumparaturi[2] + " este de " + str(lista_preturi[2]) + " lei.")

# lista_cu_liste = [
#     ["mere",5],
#     ["lapte",8],
#     ["oua",3]
# ]
# lista_cu_mere = lista_cu_liste[0]
# lista_cu_lapte = lista_cu_liste[1]
# lista_cu_oua = lista_cu_liste[2]
# print(lista_cu_mere)
# print(lista_cu_lapte)
# print(lista_cu_oua)
# print("Pretul pentru " + lista_cu_liste[0][0] + " este de " + str(lista_cu_liste[0] [1]) + " Ron.")
# print("Pretul pentru " + lista_cu_liste[1][0] + " este de " + str(lista_cu_liste[1] [1]) + " Ron.")
# print("Pretul pentru " + lista_cu_liste[2][0] + " este de " + str(lista_cu_liste[2] [1]) + " Ron.")

# adevarat = True
# fals = False 

# print(adevarat)
# print(type(adevarat))
# print(fals)
# print(type(fals))

# facut de mine extra
# mana_dreapta= 5
# mana_stanga = 5

# if mana_stanga == mana_dreapta :
#     print(True)
# else :
#     print(False)

# numar_1 = 5
# numar_2 = 5
# print(numar_1 == numar_2)

# numar_1 = 5
# numar_2 = 10
# if numar_1 == numar_2:
#     print("Numarul unu este egal cu numarul 2")
# else:
#     print("Numarul 1 nu este egal cu numarul 2")

print("Buna , cati ani ai?")
varsta=input("Varsat:")
print(type(varsta))
varsta_int = int(varsta)
if varsta_int >18:
    print("Poti intra in parcul de distractie")
else :
    print("Scuze dar nu poti intra in parcul de distractie")