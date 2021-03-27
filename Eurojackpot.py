# Eurojackpot Zahlengenerator
"""
Dieses kleine Programm erzeug für eine selbst gewählte Anzahl an Tippfeldern
für den Eurojackpot die notwendigen Tips und gibt anschließend noch die Spielscheinnummer aus
"""

# Importieren von Modulen
import random
random.seed()

# Initialisierung von Variablen

# Definitionen
def main():
    """ Generieren der Tippfelder """
    count_a = 0
    count_b = 0
    i = 0
    n = 0
    list_a=[]
    list_b=[]
    list_c=[]

    n = int(input ("Geben Sie die Anzahl der gewünschten Tippfelder ein: "))

    while i < n:
        i += 1
        list_a=[]
        list_b=[]
        count_a = 0
        count_b = 0

        print ("Ihr Spielschein Nr.", i, "ist: ")
        while count_a < 5:
            count_a += 1
            a = random.randint(1,50)
            if a not in list_a:
                list_a.append(a)
                list_a.sort()
            else:
                count_a -= 1
        print ("Tippfeld 5 aus 50: ", list_a)

        while count_b < 2:
            count_b += 1
            b = random.randint(1,10)
            if b not in list_b:
                list_b.append(b)
                list_b.sort()
            else:
                count_b -= 1
        print ("Tippfeld 2 aus 10: ", list_b, "\n")
    

    for i in range (0,7):
        c = random.randint(0,9)
        list_c.append(c)
    print ("Spielscheinnummer: ", list_c)
    
    print("\n#######################\n# *** Viel Glück! *** #\n#######################")

# Hauptprogramm
main()

