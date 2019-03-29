__author__ = "Damian Eric"
__version__ = "3.0 <09/01/19>"

from random import randint
import datetime
import os
import time
### Ora inizio ###
oraInizio = datetime.datetime.now().strftime('%H')
minutoInizio = datetime.datetime.now().strftime('%M')
secondoInizio = datetime.datetime.now().strftime('%S')


#### Creazione del file log ####
dataLog = str(datetime.datetime.now().strftime('%d-%m-%Y %H.%M.%S')) + str(".txt")
cartella = os.path.dirname(os.path.realpath(__file__))
subdir = "logs"
filepath = os.path.join(cartella, subdir, dataLog)
filepath2 = os.path.join(cartella, subdir)
try:
    os.makedirs(filepath2) #creazione cartella nel caso non esistesse
    createLog = open(filepath, "w")
    createLog.close()

    writeLog = open(filepath, "a")
    writeLog.write("Gioco avviato in data: " + str(dataLog.replace(".txt","")) + "\n")
    writeLog.close()
except:
    createLog = open(filepath, "w")
    createLog.close()

    writeLog = open(filepath, "a")
    writeLog.write("Gioco avviato in data: " + str(dataLog.replace(".txt","")) + "\n")
    writeLog.close()


#### Variabili e costanti globali ####
colonne = ["A","B","C","D","E","F","G","H","I"]
colonne_simboli = ["↓","↓","↓","↓","↓","↓","↓","↓","↓"]
righe_giocatore ={}
righe_giocatore2 = {}
righe_giocatore_inv ={}
righe_giocatore2_inv = {}
righe_PC_inv ={}
righe_PC ={}
contatore_PC = [0]
contatore_giocatore = [0]
colpito = [False]
contatore_colpo = [4]
pos_colpo = ["","","",""]
error = True
error2 = True
colpo = [""]
nome_giocatore = "Giocatore"
nome_giocatore1 = "Giocatore 1"
nome_giocatore2 = "Giocatore 2"
nome_computer = "Computer"
nome_computer1 = "Computer 1"
nome_computer2 = "Computer 2"
contatore_folle = 0
contatore_colpi1 = 0
contatore_colpi2 = 0

###########################################################################################################################


#### Generazione delle tre tabelle ####
for x in range(9):
    righe_giocatore[x] = [0,0,0,0,0,0,0,0,0]
for x in range(9):
    righe_giocatore2[x] = [0,0,0,0,0,0,0,0,0]
for x in range(9):
    righe_giocatore_inv[x] = [0,0,0,0,0,0,0,0,0]
for x in range(9):
    righe_giocatore2_inv[x] = [0,0,0,0,0,0,0,0,0]
for x in range(9):
    righe_PC[x] = [0,0,0,0,0,0,0,0,0]
for x in range(9):
    righe_PC_inv[x] = [0,0,0,0,0,0,0,0,0]


###########################################################################################################################


#### Metodo che pulisce lo schermo ####
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


###########################################################################################################################


#### Metodo che stampa la situazione delle due tabelle ####
def tabella_maker(righe_giocatore,righe_PC):

    #### Intestazione ####
    print("\n" + "\n" + "## SITUAZIONE ATTUALE DELLA TUA TABELLA ##", end=" ", flush=True)
    print( "                   ## SITUAZIONE ATTUALE DELLA TABELLA DEL PC ##" "\n" + "" )
    print("   ", end=" ", flush=True)

    #### Lettere ####
    for y in range(9):
        print("| " + str(colonne[y]), end=" ", flush=True)
    print("|                        ", end=" ", flush=True)
    for y in range(9):
        print("| " + str(colonne[y]), end=" ", flush=True)
    print("| \n")
    print("   ", end=" ", flush=True)

    #### Freccie superiori ####
    for y in range(9):
        print("  " + str(colonne_simboli[y]), end=" ", flush=True)
    print("                         ", end=" ", flush=True)
    for y in range(9):
        print("  " + str(colonne_simboli[y]), end=" ", flush=True)
    print("  \n")

    #### Stampa le righe dell'utente e le righe del PC (senza navi) ####
    for x in range(9):
        a = righe_giocatore.get(x)
        b = righe_PC.get(x)
        print(str(x+1), end=" → ", flush=True)
        for y in range(9):
            print("| " + str(a[y]), end=" ", flush=True)
        print("|                    ", end=" ", flush=True)
        print(str(x+1), end=" → ", flush=True)
        for y in range(9):
            print("| " + str(b[y]), end=" ", flush=True)
        print("| \n")


###########################################################################################################################


#### Metodo che richiede all'utente di inserire la nave da 5 unitÃ  ####
def piazza_nave5(righe_giocatore,nome):
    writeLog.write("UTENTE PIAZZA NAVE DA 5 UNITA': " + "\n")
    errore = True

    #### Ciclo ricorrente in caso di errore ####
    while errore:
        errore = False
        orientamento = input("Seleziona se mettere la prossima nave in orizzontale o verticale (O e V!): ")
        posizione = input("Inserisci la posizione della navi da 5 unitÃ  (esempio A2): ")
        posizione = posizione.upper()
        if not posizione or not orientamento:
            errore = True
            print("\n" + "### NON LASCIARE IL CAMPO VUOTO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "lascia il campo vuoto" + "\n")
            continue
        if len(posizione) != 2:
            errore = True
            print("\n" + "### INSERISCI UN DATO VALIDO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "  inserisce un  dato non valido  (" + posizione + ") \n")
            continue
        try:
            v = int(posizione[1])
            v += 1
            v -= 1
        except:
            errore = True
            print("\n" + "### INSERISCI UN DATO VALIDO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "  inserisce un  dato non valido  (" + posizione + ") \n")
            continue

        #### Calcolo delle posizioni verticali ####
        if posizione[0] == "A":
            b = 0
        elif posizione[0] == "B":
            b = 1
        elif posizione[0] == "C":
            b = 2
        elif posizione[0] == "D":
            b = 3
        elif posizione[0] == "E":
            b = 4
        elif posizione[0] == "F":
            b = 5
        elif posizione[0] == "G":
            b = 6
        elif posizione[0] == "H":
            b = 7
        elif posizione[0] == "I":
            b = 8
        else:
            errore = True
            print("\n" + "### ERRORE NELLA SELEZIONE DELLA COLONNA, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un a colonna non valida (" + posizione + ") \n")
            continue

        #### Inserimento della nave in orizzontale ####
        if orientamento.upper() == "O":
            if b >= 0 and b <=4:
                if int(posizione[1]) > 0 and int(posizione[1]) <= 9:
                    a = righe_giocatore.get(int(posizione[1])-1)
                else:
                    errore = True
                    print("\n" + "### ERRORE NELLA SELEZIONE DELLA RIGA, RIPROVA... ###" + "\n")
                    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un a riga non valida (" + posizione + ") \n")
                    continue
            else:
                errore = True
                print("\n" + "### ATTENZIONE AL BORDO, RIPROVA... ###" + "\n")
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "va oltre il bordo in orizzontale (" + posizione + ") \n")
                continue

            if not errore:
                for y in range(b,b+5):
                    a[y] = "="
                righe_giocatore[int(posizione[1])-1] = a
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "inserisce la nave in posizione " + posizione + " \n")

        ##### Inserimento della nave in verticale ####
        elif orientamento.upper() == "V":

            if int(posizione[1]) > 0 and int(posizione[1]) <= 5:
                for x in range(int(posizione[1])-1,int(posizione[1])+4):
                    a = righe_giocatore.get(x)
                    a[b] = "="
                    righe_giocatore[int(x)] = a
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "inserisce la nave in posizione " + posizione + " \n")
            else:
                errore = True
                print("\n" + "### ATTENZIONE AL BORDO, RIPROVA... ###" + "\n")
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "va oltre il bordo in verticale (" + posizione + ") \n")
                continue

        else:
            errore = True
            print("\n" + "### ERRORE NELLA SELEZIONE DELL'ORIENTAMENTO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un  orientamento non valido (" + orientamento + ") \n")
            continue


###########################################################################################################################


#### Metodo che richiede all'utente di inserire la nave da 3 unitÃ  ####
def piazza_nave3(righe_giocatore,nome):
    writeLog.write("UTENTE PIAZZA NAVE DA 3 UNITA': " + "\n")
    errore = True

    #### Ciclo ricorrente in caso di errore ####
    while errore:
        errore = False
        orientamento = input("Seleziona se mettere la prossima nave in orizzontale o verticale (O e V!): ")
        posizione = input("Inserisci la posizione della navi da 3 unitÃ  (esempio A2): ")
        posizione = posizione.upper()
        if not posizione or not orientamento:
            errore = True
            print("\n" + "### NON LASCIARE IL CAMPO VUOTO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "lascia il campo vuoto" + "\n")
            continue
        if len(posizione) != 2:
            errore = True
            print("\n" + "### INSERISCI UN DATO VALIDO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "  inserisce un  dato non valido  (" + posizione + ") \n")
            continue
        try:
            v = int(posizione[1])
            v += 1
            v -= 1
        except:
            errore = True
            print("\n" + "### INSERISCI UN DATO VALIDO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "  inserisce un  dato non valido  (" + posizione + ") \n")
            continue

        #### Calcolo delle posizioni verticali ####
        if posizione[0] == "A":
            b = 0
        elif posizione[0] == "B":
            b = 1
        elif posizione[0] == "C":
            b = 2
        elif posizione[0] == "D":
            b = 3
        elif posizione[0] == "E":
            b = 4
        elif posizione[0] == "F":
            b = 5
        elif posizione[0] == "G":
            b = 6
        elif posizione[0] == "H":
            b = 7
        elif posizione[0] == "I":
            b = 8
        else:
            errore = True
            print("\n" + "### ERRORE NELLA SELEZIONE DELLA COLONNA, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un a colonna non valida (" + posizione + ") \n")
            continue

        #### Inserimento della nave in orizzontale ####
        if orientamento.upper() == "O":
            if b >= 0 and b <=6:
                if int(posizione[1]) > 0 and int(posizione[1]) <= 9:
                    a = righe_giocatore.get(int(posizione[1])-1)
                else:
                    errore = True
                    print("\n" + "### ERRORE NELLA SELEZIONE DELLA RIGA, RIPROVA... ###" + "\n")
                    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un a riga non valida (" + posizione + ") \n")
                    continue
            else:
                errore = True
                print("\n" + "### ATTENZIONE AL BORDO, RIPROVA... ###" + "\n")
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "va oltre il bordo in orizzontale (" + posizione + ") \n")
                continue

            if not errore:
                for y in range(b,b+3):
                    if a[y] == "=":
                        errore = True
                        print("\n" + "### ATTENZIONE A NON SOVRAPPORRE LE NAVI, RIPROVA... ###" + "\n")
                        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "sovrappone le navi \n")
                        continue
                if not errore:
                    for y in range(b,b+3):
                        a[y] = "="
                righe_giocatore[int(posizione[1])-1] = a
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "inserisce la nave in posizione " + posizione + " \n")

        ##### Inserimento della nave in verticale ####
        elif orientamento.upper() == "V":

            if int(posizione[1]) > 0 and int(posizione[1]) <= 7:
                for x in range(int(posizione[1])-1,int(posizione[1])+2):
                    a = righe_giocatore.get(x)
                    if a[b] == "=":
                        errore = True
                        print("\n" + "### ATTENZIONE A NON SOVRAPPORRE LE NAVI, RIPROVA... ###" + "\n")
                        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "sovrappone le navi \n")
                        continue
                if not errore:
                    for x in range(int(posizione[1])-1,int(posizione[1])+2):
                        a = righe_giocatore.get(x)
                        a[b] = "="
                        righe_giocatore[int(x)] = a
                    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "inserisce la nave in posizione " + posizione + " \n")
            else:
                errore = True
                print("\n" + "### ATTENZIONE AL BORDO, RIPROVA... ###" + "\n")
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "va oltre il bordo in verticale (" + posizione + ") \n")
                continue

        else:
            errore = True
            print("\n" + "### ERRORE NELLA SELEZIONE DELL'ORIENTAMENTO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un  orientamento non valido (" + orientamento + ") \n")
            continue


###########################################################################################################################


#### Metodo che richiede all'utente di inserire la nave da 3 unitÃ  ####
def piazza_nave2(righe_giocatore,nome):
    writeLog.write("UTENTE PIAZZA NAVE DA 2 UNITA': " + "\n")
    errore = True

    #### Ciclo ricorrente in caso di errore ####
    while errore:
        errore = False
        orientamento = input("Seleziona se mettere la prossima nave in orizzontale o verticale (O e V!): ")
        posizione = input("Inserisci la posizione della navi da 2 unitÃ  (esempio A2): ")
        posizione = posizione.upper()
        if not posizione or not orientamento:
            errore = True
            print("\n" + "### NON LASCIARE IL CAMPO VUOTO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "lascia il campo vuoto" + "\n")
            continue
        if len(posizione) != 2:
            errore = True
            print("\n" + "### INSERISCI UN DATO VALIDO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "  inserisce un  dato non valido  (" + posizione + ") \n")
            continue
        try:
            v = int(posizione[1])
            v += 1
            v -= 1
        except:
            errore = True
            print("\n" + "### INSERISCI UN DATO VALIDO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "inscerisce un dato non valido (" + posizione + ") \n")
            continue

        #### Calcolo delle posizioni verticali ####
        if posizione[0] == "A":
            b = 0
        elif posizione[0] == "B":
            b = 1
        elif posizione[0] == "C":
            b = 2
        elif posizione[0] == "D":
            b = 3
        elif posizione[0] == "E":
            b = 4
        elif posizione[0] == "F":
            b = 5
        elif posizione[0] == "G":
            b = 6
        elif posizione[0] == "H":
            b = 7
        elif posizione[0] == "I":
            b = 8
        else:
            errore = True
            print("\n" + "### ERRORE NELLA SELEZIONE DELLA COLONNA, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un a colonna non valida (" + posizione + ") \n")
            continue

        #### Inserimento della nave in orizzontale ####
        if orientamento.upper() == "O":
            if b >= 0 and b <=7:
                if int(posizione[1]) > 0 and int(posizione[1]) <= 9:
                    a = righe_giocatore.get(int(posizione[1])-1)
                else:
                    errore = True
                    print("\n" + "### ERRORE NELLA SELEZIONE DELLA RIGA, RIPROVA... ###" + "\n")
                    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un a riga non valida (" + posizione + ") \n")
                    continue
            else:
                errore = True
                print("\n" + "### ATTENZIONE AL BORDO, RIPROVA... ###" + "\n")
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "va oltre il bordo in orizzontale (" + posizione + ") \n")
                continue

            if not errore:
                for y in range(b,b+2):
                    if a[y] == "=":
                        errore = True
                        print("\n" + "### ATTENZIONE A NON SOVRAPPORRE LE NAVI, RIPROVA... ###" + "\n")
                        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "sovrappone le navi \n")
                        continue
                if not errore:
                    for y in range(b,b+2):
                        a[y] = "="
                righe_giocatore[int(posizione[1])-1] = a
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "inserisce la nave in posizione " + posizione + " \n")

        ##### Inserimento della nave in verticale ####
        elif orientamento.upper() == "V":

            if int(posizione[1]) > 0 and int(posizione[1]) <= 8:
                for x in range(int(posizione[1])-1,int(posizione[1])+1):
                    a = righe_giocatore.get(x)
                    if a[b] == "=":
                        errore = True
                        print("\n" + "### ATTENZIONE A NON SOVRAPPORRE LE NAVI, RIPROVA... ###" + "\n")
                        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "sovrappone le navi \n")
                        continue
                if not errore:
                    for x in range(int(posizione[1])-1,int(posizione[1])+1):
                        a = righe_giocatore.get(x)
                        a[b] = "="
                        righe_giocatore[int(x)] = a
                    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "inserisce la nave in posizione " + posizione + " \n")
            else:
                errore = True
                print("\n" + "### ATTENZIONE AL BORDO, RIPROVA... ###" + "\n")
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "va oltre il bordo in verticale (" + posizione + ") \n")
                continue

        else:
            errore = True
            print("\n" + "### ERRORE NELLA SELEZIONE DELL'ORIENTAMENTO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un  orientamento non valido (" + orientamento + ") \n")
            continue


###########################################################################################################################


def ai_maker_veloce():
    errore = True

    #### Ciclo ricorrente in caso di errore ####
    #### Ciclo nel quale genero la nave da 5 unitÃ  ####
    while errore:
        errore = False
        orientamento = randint(0,1)
        if orientamento == 0:
            orientamento = "O"
        else:
            orientamento = "V"
        posizione = str(randint(0,8)) + str(randint(1,9))
        b = int(posizione[0])

        #### Inserimento della nave in orizzontale ####
        if orientamento.upper() == "O":
            if b >= 0 and b <=4:
                a = righe_PC_inv.get(int(posizione[1])-1)
            else:
                errore = True

            if not errore:
                for y in range(b,b+5):
                    a[y] = "="
                righe_PC_inv[int(posizione[1])-1] = a

        ##### Inserimento della nave in verticale ####
        elif orientamento.upper() == "V":

            if int(posizione[1]) > 0 and int(posizione[1]) <= 5:
                for x in range(int(posizione[1])-1,int(posizione[1])+4):
                    a = righe_PC_inv.get(x)
                    a[b] = "="
                    righe_PC_inv[int(x)] = a
            else:
                errore = True


###########################################################################################################################


def ai_maker(righe_PC_inv):

    for x in range(9):
        righe_PC[x] = [0,0,0,0,0,0,0,0,0]
    for x in range(9):
        righe_PC_inv[x] = [0,0,0,0,0,0,0,0,0]

    errore = True

    #### Ciclo ricorrente in caso di errore ####
    #### Ciclo nel quale genero la nave da 5 unitÃ  ####
    while errore:
        errore = False
        orientamento = randint(0,1)
        if orientamento == 0:
            orientamento = "O"
        else:
            orientamento = "V"
        posizione = str(randint(0,8)) + str(randint(1,9))
        b = int(posizione[0])

        #### Inserimento della nave in orizzontale ####
        if orientamento.upper() == "O":
            if b >= 0 and b <=4:
                a = righe_PC_inv.get(int(posizione[1])-1)
            else:
                errore = True

            if not errore:
                for y in range(b,b+5):
                    a[y] = "="
                righe_PC_inv[int(posizione[1])-1] = a

        ##### Inserimento della nave in verticale ####
        elif orientamento.upper() == "V":

            if int(posizione[1]) > 0 and int(posizione[1]) <= 5:
                for x in range(int(posizione[1])-1,int(posizione[1])+4):
                    a = righe_PC_inv.get(x)
                    a[b] = "="
                    righe_PC_inv[int(x)] = a
            else:
                errore = True

    #### Ciclo nel quale genero le 2 navi da 3 unitÃ  ####
    for h in range(2):
        errore = True

        #### Ciclo ricorrente in caso di errore ####
        while errore:
            errore = False
            orientamento = randint(0,1)
            if orientamento == 0:
                orientamento = "O"
            else:
                orientamento = "V"
            posizione = str(randint(0,8)) + str(randint(1,9))
            b = int(posizione[0])

            #### Inserimento della nave in orizzontale ####
            if orientamento.upper() == "O":
                if b >= 0 and b <=6:
                    a = righe_PC_inv.get(int(posizione[1])-1)
                else:
                    errore = True
                    continue

                if not errore:
                    for y in range(b,b+3):
                        if a[y] == "=":
                            errore = True
                            continue
                    if not errore:
                        for y in range(b,b+3):
                            a[y] = "="
                    righe_PC_inv[int(posizione[1])-1] = a
            ##### Inserimento della nave in verticale ####
            elif orientamento.upper() == "V":

                if int(posizione[1]) > 0 and int(posizione[1]) <= 7:
                    for x in range(int(posizione[1])-1,int(posizione[1])+2):
                        a = righe_PC_inv.get(x)
                        if a[b] == "=":
                            errore = True
                            continue

                    if not errore:
                        for x in range(int(posizione[1])-1,int(posizione[1])+2):
                            a = righe_PC_inv.get(x)
                            a[b] = "="
                            righe_PC_inv[int(x)] = a
                else:
                    errore = True
                    continue

        #### Ciclo nel quale genero le 3 navi da 2 unitÃ  ####
    for h in range(3):
        errore = True

        #### Ciclo ricorrente in caso di errore ####
        while errore:
            errore = False
            orientamento = randint(0,1)
            if orientamento == 0:
                orientamento = "O"
            else:
                orientamento = "V"
            posizione = str(randint(0,8)) + str(randint(1,9))
            b = int(posizione[0])

            #### Inserimento della nave in orizzontale ####
            if orientamento.upper() == "O":
                if b >= 0 and b <=7:
                    a = righe_PC_inv.get(int(posizione[1])-1)
                else:
                    errore = True
                    continue

                if not errore:
                    for y in range(b,b+2):
                        if a[y] == "=":
                            errore = True
                            continue

                    if not errore:
                        for y in range(b,b+2):
                            a[y] = "="
                    righe_PC_inv[int(posizione[1])-1] = a

            ##### Inserimento della nave in verticale ####
            elif orientamento.upper() == "V":

                if int(posizione[1]) > 0 and int(posizione[1]) <= 8:
                    for x in range(int(posizione[1])-1,int(posizione[1])+1):
                        a = righe_PC_inv.get(x)
                        if a[b] == "=":
                            errore = True
                            continue

                    if not errore:
                        for x in range(int(posizione[1])-1,int(posizione[1])+1):
                            a = righe_PC_inv.get(x)
                            a[b] = "="
                            righe_PC_inv[int(x)] = a
                else:
                    errore = True
                    continue


###########################################################################################################################


### Colpo generato dal computer ###


def colpo_ai_difficile(righe_giocatore,colpito, contatore_colpo, pos_colpo,contatore_PC,nome_computer):
    errore = True
    while errore:
        errore = False
        #colpo casuale
        posizione = str(randint(0,8)) + str(randint(0,8))
        if not colpito[0]:
            a = int(posizione[1])
            b = int(posizione[0])
            x = righe_giocatore.get(a)
            if x[b] == "X" or x[b] == "/":
                errore = True
                continue
            elif not errore:
                if x[b] == "=":
                    x[b] = "X"
                    colpito[0] = True
                    cont = contatore_PC[0]
                    cont = cont + 1
                    contatore_PC[0] = cont
                    pos_colpo[0] = str(a)
                    pos_colpo[1] = str(b)
                    pos_colpo[2] = str(a)
                    pos_colpo[3] = str(b)
                    contatore_colpo[0] = 4
                    colpo[0] = "Il computer ha colpito una tua nave!"
                else:
                    x[b] = "/"
                    colpo[0] = "Il computer non ti ha colpito!"
                righe_giocatore[a] = x
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome_computer) + " colpisce in posizione " + posizione + " \n")
        #colpo verso il basso dal punto colpito
        elif colpito[0] and contatore_colpo[0] == 4:
            a = int(pos_colpo[0])
            b = int(pos_colpo[1])
            if a == 8:
                a = int(pos_colpo[2]) - 1
            elif a <= 7:
                a = a + 1
            x = righe_giocatore.get(a)

            if x[b] == "X" or x[b] == "/" :
                errore = True
                contatore_colpo[0] = contatore_colpo[0] - 1
                continue
            elif not errore:
                if x[b] == "=":
                    x[b] = "X"
                    colpito[0] = True
                    cont = contatore_PC[0]
                    cont = cont + 1
                    contatore_PC[0] = cont
                    pos_colpo[0] = str(a)
                    pos_colpo[1] = str(b)
                    contatore_colpo[0] = 4
                    colpo[0] = "Il computer ha colpito una tua nave!"
                else:
                    x[b] = "/"
                    colpo[0] = "Il computer non ti ha colpito!"
                    contatore_colpo[0] = 3
                    pos_colpo[0] = pos_colpo[2]
                    pos_colpo[1] = pos_colpo[3]
                righe_giocatore[a] = x
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome_computer) + " colpisce in posizione " + posizione + " \n")
        #colpo verso l'alto dal punto colpito
        elif colpito[0] and contatore_colpo[0] == 3:
            a = int(pos_colpo[0])
            b = int(pos_colpo[1])
            if a == 0:
                a = int(pos_colpo[2]) + 1
            elif a >= 1:
                a = a - 1
            x = righe_giocatore.get(a)

            if x[b] == "X" or x[b] == "/":
                errore = True
                contatore_colpo[0] = contatore_colpo[0] - 1
                continue
            elif not errore:
                if x[b] == "=":
                    x[b] = "X"
                    colpito[0] = True
                    cont = contatore_PC[0]
                    cont = cont + 1
                    contatore_PC[0] = cont
                    pos_colpo[0] = str(a)
                    pos_colpo[1] = str(b)
                    contatore_colpo[0] = 3
                    colpo[0] = "Il computer ha colpito una tua nave!"
                else:
                    x[b] = "/"
                    colpo[0] = "Il computer non ti ha colpito!"
                    contatore_colpo[0] = 4
                    pos_colpo[0] = pos_colpo[2]
                    pos_colpo[1] = pos_colpo[3]
                righe_giocatore[a] = x
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome_computer) + " colpisce in posizione " + posizione + " \n")
        #colpo verso sinistra dal punto colpito
        elif colpito[0] and contatore_colpo[0] == 2:
            a = int(pos_colpo[0])
            b = int(pos_colpo[1])
            if b == 0:
                b = int(pos_colpo[3]) + 1
            elif b >= 1:
                b = b - 1
            x = righe_giocatore.get(a)

            if x[b] == "X" or x[b] == "/":
                errore = True
                contatore_colpo[0] = contatore_colpo[0] - 1
                continue
            elif not errore:
                if x[b] == "=":
                    x[b] = "X"
                    colpito[0] = True
                    cont = contatore_PC[0]
                    cont = cont + 1
                    contatore_PC[0] = cont
                    pos_colpo[0] = str(a)
                    pos_colpo[1] = str(b)
                    contatore_colpo[0] = 2
                    colpo[0] = "Il computer ha colpito una tua nave!"
                else:
                    x[b] = "/"
                    colpo[0] = "Il computer non ti ha colpito!"
                    contatore_colpo[0] = 1
                    pos_colpo[0] = pos_colpo[2]
                    pos_colpo[1] = pos_colpo[3]
                righe_giocatore[a] = x
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome_computer) + " colpisce in posizione " + posizione + " \n")
        #colpo verso destra dal punto colpito
        elif colpito[0] and contatore_colpo[0] == 1:
            a = int(pos_colpo[0])
            b = int(pos_colpo[1])
            if b == 8:
                b = int(pos_colpo[3]) - 1
            elif b <= 7:
                b = b + 1
            x = righe_giocatore.get(a)

            if x[b] == "X" or x[b] == "/":
                errore = True
                contatore_colpo[0] = contatore_colpo[0] - 1
                continue
            elif not errore:
                if x[b] == "=":
                    x[b] = "X"
                    colpito[0] = True
                    cont = contatore_PC[0]
                    cont = cont + 1
                    contatore_PC[0] = cont
                    pos_colpo[0] = str(a)
                    pos_colpo[1] = str(b)
                    contatore_colpo[0] = 1
                    colpo[0] = "Il computer ha colpito una tua nave!"
                else:
                    x[b] = "/"
                    colpo[0] = "Il computer non ti ha colpito!"
                    contatore_colpo[0] = 2
                    pos_colpo[0] = pos_colpo[2]
                    pos_colpo[1] = pos_colpo[3]
                righe_giocatore[a] = x
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome_computer) + " colpisce in posizione " + posizione + " \n")
        #reset del colpo
        elif colpito[0] and contatore_colpo[0] == 0:
            errore = True
            colpito[0] = False


###########################################################################################################################


### Colpo generato dal computer ###
def colpo_ai_facile():
    errore = True
    while errore:
        errore = False
        posizione = str(randint(0,8)) + str(randint(0,8))
        a = int(posizione[1])
        b = int(posizione[0])
        x = righe_giocatore.get(a)
        if x[b] == "X" or x[b] == "/":
            errore = True
            continue
        elif not errore:
            if x[b] == "=":
                x[b] = "X"
                cont = contatore_PC[0]
                cont = cont + 1
                contatore_PC[0] = cont
                colpo[0] = "Il computer ha colpito una tua nave!"
            else:
                x[b] = "/"
                colpo[0] = "Il computer non ti ha colpito!"
            righe_giocatore[a] = x
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome_computer) + " colpisce in posizione " + posizione + " \n")


###########################################################################################################################


### Colpo generato dal computer ###
def colpo_ai_impossibile():
    errore = False
    for z in range(0, 9):
        for l in range(0, 9):
            a = z
            b = l
            x = righe_giocatore.get(a)
            if x[b] == "=":
                x[b] = "X"
                cont = contatore_PC[0]
                cont = cont + 1
                contatore_PC[0] = cont
                errore = True
                writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Computer colpisce in posizione " + str(a) + str(b) + " \n")
                colpo[0] = "Il computer ha colpito una tua nave!"
                break
            righe_giocatore[a] = x
        if errore:
            break


###########################################################################################################################


def colpo_giocatore(righe_PC,righe_PC_inv,contatore_giocatore,nome):
    errore = True

    #### Ciclo ricorrente in caso di errore ####
    while errore:
        errore = False
        posizione = input("Inserisci la posizione di dove vuoi lanciare la bomba (per esempio A5): ")
        posizione = posizione.upper()
        if not posizione:
            errore = True
            print("\n" + "### NON LASCIARE IL CAMPO VUOTO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "lascia il campo vuoto" + "\n")
            continue
        if len(posizione) != 2:
            errore = True
            print("\n" + "### INSERISCI UN DATO VALIDO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "  inserisce un  dato non valido  (" + posizione + ") \n")
            continue

        #### Calcolo delle posizioni verticali ####
        if posizione[0] == "A":
            b = 0
        elif posizione[0] == "B":
            b = 1
        elif posizione[0] == "C":
            b = 2
        elif posizione[0] == "D":
            b = 3
        elif posizione[0] == "E":
            b = 4
        elif posizione[0] == "F":
            b = 5
        elif posizione[0] == "G":
            b = 6
        elif posizione[0] == "H":
            b = 7
        elif posizione[0] == "I":
            b = 8
        else:
            errore = True
            print("\n" + "### ERRORE NELLA SELEZIONE DELLA COLONNA, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un a colonna non valida (" + posizione + ") \n")
            continue
        try:
            v = int(posizione[1])
            v += 1
            v -= 1
        except:
            errore = True
            print("\n" + "### INSERISCI UN DATO VALIDO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + "  inserisce un  dato non valido  (" + posizione + ") \n")
            continue

        if int(posizione[1]) > 0 and int(posizione[1]) <= 9:
            a = righe_PC_inv.get(int(posizione[1])-1)
            k = righe_PC.get(int(posizione[1])-1)
        else:
            errore = True
            print("\n" + "### ERRORE NELLA SELEZIONE DELLA RIGA, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un a riga non valida (" + posizione + ") \n")
            continue

        if k[b] == "X" or k[b] == "/":
            errore = True
            print("\n" + "### HAI GIA COLPITO QUEL PUNTO, RIPROVA... ###" + "\n")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " inserisce un a posizione già colpita (" + posizione + ") \n")
            continue
        elif not errore:
            if a[b] == "=":
                k[b] = "X"
                cont = contatore_giocatore[0]
                cont = cont + 1
                contatore_giocatore[0] = cont
                colpo[0] = "Hai colpito la nave del computer!"
            else:
                k[b] = "/"
                colpo[0] = "Il tuo colpo è andato a vuoto!"
            righe_PC[int(posizione[1])-1] = k
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": " + str(nome) + " colpisce in posizione " + posizione + " \n")


###########################################################################################################################

''' inizio programma '''
cls()

print("#######################################################################################################")
print("###  GIOCO SVILUPPATO TRAMITE PYTHON DA ERIC DAMIAN                                                 ###")
print("###  BENVENUTO SU BATTAGLIA NAVALE V 3.0!                                                           ###")
print("###  IN QUESTO GIOCO TI TROVERAI CONTRO IL COMPUTER.                                                ###")
print("###  LE REGOLE SONO:                                                                                ###")
print("###  -VINCE CHI ARRIVA A 17 PUNTI PER PRIMO;                                                        ###")
print("###  -LE NAVI DA POSIZIONARE SONO 6 (1 NAVE LUNGA 5, 2 NAVI LUNGHE 3, 3 NAVI LUNGHE 2);             ###")
print("###  -DOVRAI DISPORRE LE TUE NAVI IN MODO DA NON ANDARE OLTRE IL BORDO E SENZA SOVRAPPORRE LE NAVI; ###")
print("###  NEL CASO DI UN ERRORE IL PROGRAMMA TI AVVISERA' E POTRAI ESEGUIRE DI NUOVO QUELLA MOSSA.       ###")
print("#######################################################################################################" + "\n")
print("###  PUOI SCEGLIERE LA MODALITA' DI PARTITA TRA DIFFICILE, FACILE, VELOCE, PREGENERATO, AMICI, FOLLE, COMPUTER   ###")
print("###  E IMPOSSIBILE:                                                                                              ###" + "\n")
print("###  LA DIFFERENZA TRA MODALITA' FACILE E DIFFICILE STA NEL TIPO DI LOGICA USATA DAL COMPUTER DURANTE LA FASE    ###" )
print("###  DEI COLPI.                                                                                                  ###" + "\n")
print("###  LA MODALITA' VELOCE CONSISTE NEL POSIZIONAMENTO DI UNA SOLA NAVE DA 5. (COMPUTER E' IN MODALITA' DIFFICILE).###" + "\n")
print("###  LA MODALITA' PREGENERATO GENERA LA TUA TABELLA IN AUTOMATICO (COMPUTER E' IN MODALITA DIFFICILE).           ###" + "\n")
print("###  LA MODALITA' AMICI CONSENTE DI GIOCARE UNA PARTITA 1 VS 1.                                                  ###" + "\n")
print("###  LA MODALITA' COMPUTER MOSTRA UNA PARTITA IN CUI IL COMPUTER GIOCA CONTRO SE STESSO (DELAY A SCELTA).        ###" + "\n")
print("###  LA MODALITA' FOLLE CONSISTE IN UNA PARTITA CONTRO IL COMPUTER CHE AGGIORNA LE SUE POSIZIONI OGNI 5 MOSSE    ###")
print("###  E PER VINCERE BISOGNA RAGGIUNGERE I 25 PUNTI ( IL COMPUTER E' IN MODALITA' DIFFICILE).                      ###" + "\n")
print("###  LA MODALITA' IMPOSSIBILE CONSISTE NEL GENERARE UNA TABELLA AL GIOCATORE E DARE 5 SECONDI IN CUI OSSERVARE   ###" + "\n")
print("###  QUELLA NEMICA, DOPO DI CHE IL COMPUTER AVRA' UNA POSSIBILITA' DI COLPIRTI DEL 100%. (INIZII PER PRIMO)      ###")
print("###  IL SIMBOLO '/' INDICA COLPO A VUOTO, IL SIMBOLO 'X' INDICA COLPO A SEGNO, IL SIMBOLO '0' INDICA IL MARE.    ###" + "\n")


### Selezione modalità ###
while error:
    writeLog = open(filepath, "a")
    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": INSERIMENTO MODALITA' DI GIOCO: \n")
    x = input("Inserisci la modalità desiderata (F o D o V o P o A o C o FOLLE o I): ")
    x = x.upper()
    if x == "D" or x == "F" or x == "V" or x == "A" or x == "P" or x == "C" or x == "FOLLE" or x == "I":
        error = False
        modalita = x
    else:
        errore = True
        print("###  INSERISCI UN DATO VALIDO  ###" + "\n" + "\n")
        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente   inserisce un  dato non valido  \n")
        continue

modalita = modalita.upper()
cls() #pulisce lo schermo

### Inizio partita ###
writeLog = open(filepath, "a")
if modalita == "F":
    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente avvia la partita in modalità facile \n")
elif modalita == "D":
    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente avvia la partita in modalità difficile \n")
elif modalita == "A":
    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente avvia la partita in modalità amici \n")
elif modalita == "FOLLE":
    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente avvia la partita in modalità folle \n")
elif modalita == "C":
    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente avvia la partita in modalità computer \n")
elif modalita == "P":
    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente avvia la partita in modalità pregenerato \n")
elif modalita == "I":
    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente avvia la partita in modalità impossibile \n")
else:
    writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente avvia la partita in modalità veloce \n")
writeLog.close()

### MODALITA' VELOCE ###
if modalita == "V":
    print("###                                         MODALITA' VELOCE                                         ###" + "\n" + "\n")
    ai_maker_veloce()
    tabella_maker(righe_giocatore,righe_PC)
    print("\n" + "Hai a disposizione 1 nave, posizionala con cura e attento a non superare i bordi!" + "\n")
    writeLog = open(filepath, "a")
    piazza_nave5(righe_giocatore,nome_giocatore)
    writeLog.close()


### MODALITA' COMPUTER ###
elif modalita == "C":
    print("###                                         MODALITA' COMPUTER                                          ###" + "\n" + "\n")
    ai_maker(righe_giocatore_inv)
    ai_maker(righe_giocatore2_inv)
    tabella_maker(righe_giocatore2_inv,righe_giocatore_inv)
    while error2:
        delaytime = input("Inserisci il tempo che deve trascorrere tra ogni mossa (Secondi): ")
        try:
            delaytime = float(delaytime)
            error2 = 0
        except:
            print("Inserisci un tempo valido!")
            writeLog = open(filepath, "a")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente  inserisce un  tempo non valido \n")
            writeLog.close()
            error2 = 1
    input("Premi invio per cominciare a vedere la partita!")


### MODALITA' PREGENERATO ###
elif modalita == "P":
    ai_maker(righe_PC_inv)
    while error2:
        print("###                                      MODALITA' PREGENETATO                                       ###" + "\n" + "\n")
        ai_maker(righe_giocatore)
        tabella_maker(righe_giocatore,righe_PC)
        approvamento = input("Vuoi generare una nuova tabella? (S o N) : ")
        if approvamento.upper() == "S":
            error2 = 1
            writeLog = open(filepath, "a")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente accetta la tabella \n")
            writeLog.close()
        elif approvamento.upper() == "N":
            error2 = 0
            writeLog = open(filepath, "a")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente declina la tabella \n")
            writeLog.close()
        else:
            error2 = 1
            print("Inserisci un dato valido!")
            writeLog = open(filepath, "a")
            writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente   inserisce un  dato non valido  (" + str(approvamento) +") \n" )
            writeLog.close()
    input("Premi invio per cominciare la partita!")
    cls()


### MODALITA' IMPOSSIBILE ###
elif modalita == "I":
    ai_maker(righe_PC_inv)
    print("###                                         MODALITA' IMPOSSIBILE                                          ###" + "\n" + "\n")
    ai_maker(righe_giocatore)
    tabella_maker(righe_giocatore,righe_PC)
    input("Premi invio per cominciare la partita. (PS: Preparati a guardare la tabella del computer prima che scompaia!)")
    cls()
    for k in range(5):
        print("###                                         MODALITA' IMPOSSIBILE                                          ###" + "\n" + "\n")
        tabella_maker(righe_giocatore,righe_PC_inv)
        print("Mancano " + str(5 - k) + " secondi...")
        time.sleep(1)
        cls()

### MODALITA' AMICI ###
elif modalita == "A":
    print("###                                         MODALITA' AMICI                                          ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2,righe_giocatore_inv)
    print("\n" + "Hai a disposizione 6 navi, posizionale con cura e attento a non superare i bordi!" + "\n")
    writeLog = open(filepath, "a")
    piazza_nave5(righe_giocatore2,nome_giocatore1)
    writeLog.close()
    cls() #pulisce lo schermo
    print("###                                         MODALITA' AMICI                                         ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2,righe_giocatore_inv)
    writeLog = open(filepath, "a")
    piazza_nave3(righe_giocatore2,nome_giocatore1)
    writeLog.close()
    cls() #pulisce lo schermo
    print("###                                         MODALITA' AMICI                                          ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2,righe_giocatore_inv)
    writeLog = open(filepath, "a")
    piazza_nave3(righe_giocatore2,nome_giocatore1)
    writeLog.close()
    cls() #pulisce lo schermo
    print("###                                         MODALITA' AMICI                                        ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2,righe_giocatore_inv)
    writeLog = open(filepath, "a")
    piazza_nave2(righe_giocatore2,nome_giocatore1)
    writeLog.close()
    cls() #pulisce lo schermo
    print("###                                         MODALITA' AMICI                                          ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2,righe_giocatore_inv)
    writeLog = open(filepath, "a")
    piazza_nave2(righe_giocatore2,nome_giocatore1)
    writeLog.close()
    cls() #pulisce lo schermo
    print("###                                         MODALITA' AMICI                                          ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2,righe_giocatore_inv)
    writeLog = open(filepath, "a")
    piazza_nave2(righe_giocatore2,nome_giocatore1)
    writeLog.close()
    input("Premi invio per passare al giocatore 2 (P.S: Attento che non ti abbia spiato!)")
    cls()
    print("###                                         MODALITA' AMICI                                          ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2_inv,righe_giocatore)
    print("\n" + "Hai a disposizione 6 navi, posizionale con cura e attento a non superare i bordi!" + "\n")
    writeLog = open(filepath, "a")
    piazza_nave5(righe_giocatore,nome_giocatore2)
    writeLog.close()
    cls() #pulisce lo schermo
    print("###                                         MODALITA' AMICI                                         ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2_inv,righe_giocatore)
    writeLog = open(filepath, "a")
    piazza_nave3(righe_giocatore,nome_giocatore2)
    writeLog.close()
    cls() #pulisce lo schermo
    print("###                                         MODALITA' AMICI                                          ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2_inv,righe_giocatore)
    writeLog = open(filepath, "a")
    piazza_nave3(righe_giocatore,nome_giocatore2)
    writeLog.close()
    cls() #pulisce lo schermo
    print("###                                         MODALITA' AMICI                                        ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2_inv,righe_giocatore)
    writeLog = open(filepath, "a")
    piazza_nave2(righe_giocatore,nome_giocatore2)
    writeLog.close()
    cls() #pulisce lo schermo
    print("###                                         MODALITA' AMICI                                          ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2_inv,righe_giocatore)
    writeLog = open(filepath, "a")
    piazza_nave2(righe_giocatore,nome_giocatore2)
    writeLog.close()
    cls() #pulisce lo schermo
    print("###                                         MODALITA' AMICI                                          ###" + "\n" + "\n")
    tabella_maker(righe_giocatore2_inv,righe_giocatore)
    writeLog = open(filepath, "a")
    piazza_nave2(righe_giocatore,nome_giocatore2)
    writeLog.close()
    input("Premi invio per cominciare, divertitevi!")

### MODALITA' FACILE E DIFFICILE E FOLLE ###
else:
    if modalita == "F":
        print("###                                         MODALITA' FACILE                                         ###" + "\n" + "\n")
    elif modalita == "FOLLE":
        print("###                                          MODALITA' FOLLE                                         ###" + "\n" + "\n")
    else:
        print("###                                       MODALITA' DIFFICILE                                        ###" + "\n" + "\n")
    ai_maker(righe_PC_inv)
    tabella_maker(righe_giocatore,righe_PC)
    print("\n" + "Hai a disposizione 6 navi, posizionale con cura e attento a non superare i bordi!" + "\n")
    writeLog = open(filepath, "a")
    piazza_nave5(righe_giocatore,nome_giocatore)
    writeLog.close()
    cls() #pulisce lo schermo
    if modalita == "F":
        print("###                                         MODALITA' FACILE                                         ###" + "\n" + "\n")
    elif modalita == "FOLLE":
        print("###                                          MODALITA' FOLLE                                         ###" + "\n" + "\n")
    else:
        print("###                                       MODALITA' DIFFICILE                                        ###" + "\n" + "\n")
    tabella_maker(righe_giocatore,righe_PC)
    writeLog = open(filepath, "a")
    piazza_nave3(righe_giocatore,nome_giocatore)
    writeLog.close()
    cls() #pulisce lo schermo
    if modalita == "F":
        print("###                                         MODALITA' FACILE                                         ###" + "\n" + "\n")
    elif modalita == "FOLLE":
        print("###                                          MODALITA' FOLLE                                         ###" + "\n" + "\n")
    else:
        print("###                                       MODALITA' DIFFICILE                                        ###" + "\n" + "\n")
    tabella_maker(righe_giocatore,righe_PC)
    writeLog = open(filepath, "a")
    piazza_nave3(righe_giocatore,nome_giocatore)
    writeLog.close()
    cls() #pulisce lo schermo
    if modalita == "F":
        print("###                                         MODALITA' FACILE                                         ###" + "\n" + "\n")
    elif modalita == "FOLLE":
        print("###                                          MODALITA' FOLLE                                         ###" + "\n" + "\n")
    else:
        print("###                                       MODALITA' DIFFICILE                                        ###" + "\n" + "\n")
    tabella_maker(righe_giocatore,righe_PC)
    writeLog = open(filepath, "a")
    piazza_nave2(righe_giocatore,nome_giocatore)
    writeLog.close()
    cls() #pulisce lo schermo
    if modalita == "F":
        print("###                                         MODALITA' FACILE                                         ###" + "\n" + "\n")
    elif modalita == "FOLLE":
        print("###                                          MODALITA' FOLLE                                         ###" + "\n" + "\n")
    else:
        print("###                                       MODALITA' DIFFICILE                                        ###" + "\n" + "\n")
    tabella_maker(righe_giocatore,righe_PC)
    writeLog = open(filepath, "a")
    piazza_nave2(righe_giocatore,nome_giocatore)
    writeLog.close()
    cls() #pulisce lo schermo
    if modalita == "F":
        print("###                                         MODALITA' FACILE                                         ###" + "\n" + "\n")
    elif modalita == "FOLLE":
        print("###                                          MODALITA' FOLLE                                         ###" + "\n" + "\n")
    else:
        print("###                                       MODALITA' DIFFICILE                                        ###" + "\n" + "\n")
    tabella_maker(righe_giocatore,righe_PC)
    writeLog = open(filepath, "a")
    piazza_nave2(righe_giocatore,nome_giocatore)
    writeLog.close()
print("\n" + "Inizia la partita!" + "\n")


### PARTITA AMICI ###
while modalita.upper() == "A" and contatore_PC[0] != 17 and contatore_giocatore[0] != 17:
    cls() #pulisce lo schermo
    print("###                                         MODALITA' AMICI                                         ###" + "\n" + "\n")
    print("\n" + "          GIOCATORE 1: " + str(contatore_giocatore), end="", flush=True)
    print("                  <---- PUNTEGGIO ---->                GIOCATORE 2: " + str(contatore_PC) + "\n")
    tabella_maker(righe_giocatore_inv,righe_giocatore2_inv)
    print("Colpi saprati dal primo giocatore: " + str(contatore_colpi1))
    print("\n" + "E' turno del primo giocatore:" + "\n")
    writeLog = open(filepath, "a")
    colpo_giocatore(righe_giocatore2_inv,righe_giocatore2,contatore_giocatore,nome_giocatore1)
    writeLog.close()
    contatore_colpi1 += 1
    cls() #pulisce lo schermo
    if contatore_PC[0] != 17 and contatore_giocatore[0] != 17:
        print("###                                         MODALITA' AMICI                                         ###" + "\n" + "\n")
        print("\n" + "          GIOCATORE 1: " + str(contatore_giocatore), end="", flush=True)
        print("                  <---- PUNTEGGIO ---->                GIOCATORE 2: " + str(contatore_PC) + "\n")
        tabella_maker(righe_giocatore_inv,righe_giocatore2_inv)
        print("Colpi saprati dal secondo giocatore: " + str(contatore_colpi2))
        print("\n" + "E' turno del secondo giocatore:" + "\n")
        writeLog = open(filepath, "a")
        colpo_giocatore(righe_giocatore_inv,righe_giocatore,contatore_PC,nome_giocatore1)
        writeLog.close()
        contatore_colpi2 += 1


### PARTITA COMPUTER ###
while modalita.upper() == "C" and contatore_PC[0] != 17 and contatore_giocatore[0] != 17:
    cls() #pulisce lo schermo
    print("###                                         MODALITA' COMPUTER                                          ###" + "\n" + "\n")
    print("\n" + "          COMPUTER 1: " + str(contatore_giocatore), end="", flush=True)
    print("                  <---- PUNTEGGIO ---->                COMPUTER 2: " + str(contatore_PC) + "\n")
    tabella_maker(righe_giocatore_inv,righe_giocatore2_inv)
    print("Colpi saprati dal primo computer: " + str(contatore_colpi1))
    print("\n" + "E' turno del Computer 1:" + "\n")
    writeLog = open(filepath, "a")
    colpo_ai_difficile(righe_giocatore2_inv,colpito, contatore_colpo, pos_colpo,contatore_giocatore,nome_computer1)
    writeLog.close()
    contatore_colpi1 += 1
    time.sleep(delaytime)
    cls() #pulisce lo schermo
    if contatore_PC[0] != 17 and contatore_giocatore[0] != 17:
        print("###                                         MODALITA' COMPUTER                                          ###" + "\n" + "\n")
        print("\n" + "          COMPUTER 1: " + str(contatore_giocatore), end="", flush=True)
        print("                  <---- PUNTEGGIO ---->                COMPUTER 2: " + str(contatore_PC) + "\n")
        tabella_maker(righe_giocatore_inv,righe_giocatore2_inv)
        print("Colpi saprati dal secondo computer: " + str(contatore_colpi2))
        print("\n" + "E' turno del Computer 2:" + "\n")
        writeLog = open(filepath, "a")
        colpo_ai_difficile(righe_giocatore_inv,colpito, contatore_colpo, pos_colpo,contatore_PC,nome_computer2)
        writeLog.close()
        contatore_colpi2 += 1
        time.sleep(delaytime)



### PARTITA FOLLE ###
while (modalita.upper() == "FOLLE")and contatore_PC[0] != 17 and contatore_giocatore[0] != 25:
    if contatore_folle == 5:
        contatore_folle = 0
        ai_maker(righe_PC_inv)
    cls() #pulisce lo schermo
    print("###                                          MODALITA' FOLLE                                         ###" + "\n" + "\n")
    print("\n" + "          GIOCATORE: " + str(contatore_giocatore), end="", flush=True)
    print("                  <---- PUNTEGGIO ---->                PC: " + str(contatore_PC) + "\n")
    tabella_maker(righe_giocatore,righe_PC)
    print("Colpi saprati da parte tua: " + str(contatore_colpi1))
    print("\n" + "E' il tuo turno:" + "\n")
    if contatore_folle == 4:
        print("\n" + "Ti rimane " + str(5 - contatore_folle) + " mossa prima del Reset!\n")
    else:
        print("\n" + "Ti rimangono " + str(5 - contatore_folle) + " mosse prima del Reset!\n")
    writeLog = open(filepath, "a")
    colpo_giocatore(righe_PC,righe_PC_inv,contatore_giocatore,nome_giocatore)
    writeLog.close()
    contatore_colpi1 += 1
    if modalita == "V":
        if contatore_giocatore[0] == 5:
            break
    cls() #pulisce lo schermo
    print("###                                          MODALITA' FOLLE                                         ###" + "\n" + "\n")
    print("\n" + "          GIOCATORE: " + str(contatore_giocatore), end="", flush=True)
    print("                  <---- PUNTEGGIO ---->                PC: " + str(contatore_PC) + "\n")
    tabella_maker(righe_giocatore,righe_PC)
    print(colpo[0] + "\n")
    input("Premi invio per continuare...")
    cls()
    print("###                                          MODALITA' FOLLE                                         ###" + "\n" + "\n")
    print("\n" + "          GIOCATORE: " + str(contatore_giocatore), end="", flush=True)
    print("                  <---- PUNTEGGIO ---->                PC: " + str(contatore_PC) + "\n")
    writeLog = open(filepath, "a")
    colpo_ai_difficile(righe_giocatore,colpito, contatore_colpo, pos_colpo,contatore_PC,nome_computer)
    writeLog.close()
    tabella_maker(righe_giocatore,righe_PC)
    print("Colpi saprati dal computer tua: " + str(contatore_colpi2))
    print("\n" + "Il PC ha fatto la sua mossa:" + "\n")
    print(colpo[0] + "\n")
    contatore_colpi2 += 1
    input("Premi invio per continuare...")
    contatore_folle += 1


### PARTITA FACILE ###
while modalita.upper() == "F" and contatore_PC[0] != 17 and contatore_giocatore[0] != 17:
    cls() #pulisce lo schermo
    print("###                                         MODALITA' FACILE                                        ###" + "\n" + "\n")
    print("\n" + "          GIOCATORE: " + str(contatore_giocatore), end="", flush=True)
    print("                  <---- PUNTEGGIO ---->                PC: " + str(contatore_PC) + "\n")
    tabella_maker(righe_giocatore,righe_PC)
    print("Colpi saprati da parte tua: " + str(contatore_colpi1))
    print("\n" + "E' il tuo turno:" + "\n")
    writeLog = open(filepath, "a")
    colpo_giocatore(righe_PC,righe_PC_inv,contatore_giocatore,nome_giocatore)
    writeLog.close()
    contatore_colpi1 += 1
    cls() #pulisce lo schermo
    print("###                                         MODALITA' FACILE                                        ###" + "\n" + "\n")
    print("\n" + "          GIOCATORE: " + str(contatore_giocatore), end="", flush=True)
    print("                  <---- PUNTEGGIO ---->                PC: " + str(contatore_PC) + "\n")
    tabella_maker(righe_giocatore,righe_PC)
    print(colpo[0] + "\n")
    input("Premi invio per continuare...")
    cls()
    print("###                                         MODALITA' FACILE                                        ###" + "\n" + "\n")
    print("\n" + "          GIOCATORE: " + str(contatore_giocatore), end="", flush=True)
    print("                  <---- PUNTEGGIO ---->                PC: " + str(contatore_PC) + "\n")
    writeLog = open(filepath, "a")
    colpo_ai_facile()
    contatore_colpi2 += 1
    writeLog.close()
    tabella_maker(righe_giocatore,righe_PC)
    print("Colpi saprati dal computer: " + str(contatore_colpi2))
    print("\n" + "Il PC ha fatto la sua mossa:" + "\n")
    print(colpo[0] + "\n")
    input("Premi invio per continuare...")


### PARTITA DIFFICILE O VELOCE O PREGENERATO O IMPOSSIBILE###
while modalita.upper() == "D" or "V" or "P" or "I" and contatore_PC[0] != 17 and contatore_giocatore[0] != 17:
    cls() #pulisce lo schermo
    if modalita == "V":
        print("###                                         MODALITA' VELOCE                                         ###" + "\n" + "\n")
    elif modalita == "P":
        print("###                                      MODALITA' PREGENETATO                                       ###" + "\n" + "\n")
    elif modalita == "I":
        print("###                                       MODALITA' IMPOSSIBILE                                      ###" + "\n" + "\n")
    else:
        print("###                                       MODALITA' DIFFICILE                                        ###" + "\n" + "\n")
    print("\n" + "          GIOCATORE: " + str(contatore_giocatore), end="", flush=True)
    print("                  <---- PUNTEGGIO ---->                PC: " + str(contatore_PC) + "\n")
    tabella_maker(righe_giocatore,righe_PC)
    print("Colpi saprati da parte tua: " + str(contatore_colpi1))
    print("\n" + "E' il tuo turno:" + "\n")
    writeLog = open(filepath, "a")
    colpo_giocatore(righe_PC,righe_PC_inv,contatore_giocatore,nome_giocatore)
    writeLog.close()
    contatore_colpi1 += 1
    if modalita == "V":
        if contatore_giocatore[0] == 5:
            break
    cls() #pulisce lo schermo
    if modalita == "V":
        print("###                                         MODALITA' VELOCE                                         ###" + "\n" + "\n")
    elif modalita == "P":
        print("###                                      MODALITA' PREGENETATO                                       ###" + "\n" + "\n")
    elif modalita == "I":
        print("###                                       MODALITA' IMPOSSIBILE                                      ###" + "\n" + "\n")
    else:
        print("###                                       MODALITA' DIFFICILE                                        ###" + "\n" + "\n")
    print("\n" + "          GIOCATORE: " + str(contatore_giocatore), end="", flush=True)
    print("                  <---- PUNTEGGIO ---->                PC: " + str(contatore_PC) + "\n")
    tabella_maker(righe_giocatore,righe_PC)
    print(colpo[0] + "\n")
    input("Premi invio per continuare...")
    cls()
    if modalita == "V":
        print("###                                         MODALITA' VELOCE                                         ###" + "\n" + "\n")
    elif modalita == "P":
        print("###                                      MODALITA' PREGENETATO                                       ###" + "\n" + "\n")
    elif modalita == "I":
        print("###                                       MODALITA' IMPOSSIBILE                                      ###" + "\n" + "\n")
    else:
        print("###                                       MODALITA' DIFFICILE                                        ###" + "\n" + "\n")
    print("\n" + "          GIOCATORE: " + str(contatore_giocatore), end="", flush=True)
    print("                  <---- PUNTEGGIO ---->                PC: " + str(contatore_PC) + "\n")
    if modalita == "I":
        writeLog = open(filepath, "a")
        colpo_ai_impossibile()
        contatore_colpi2 += 1
        writeLog.close()
    else:
        writeLog = open(filepath, "a")
        colpo_ai_difficile(righe_giocatore,colpito, contatore_colpo, pos_colpo,contatore_PC,nome_computer)
        contatore_colpi2 += 1
        writeLog.close()
    tabella_maker(righe_giocatore,righe_PC)
    print("Colpi saprati dal computer: " + str(contatore_colpi2))
    print("\n" + "Il PC ha fatto la sua mossa:" + "\n")
    print(colpo[0] + "\n")
    input("Premi invio per continuare...")
    if modalita == "V":
        if contatore_PC[0] == 5:
            break
cls()


### Calcolo durata della partita ###
oraFine = datetime.datetime.now().strftime('%H')
minutoFine = datetime.datetime.now().strftime('%M')
secondoFine = datetime.datetime.now().strftime('%S')
if int(oraFine) < int(oraInizio):
    ore = (24) - int(oraInizio) + int(oraFine)
else:
    ore = int(oraFine) - int(oraInizio)
if int(minutoFine) < int(minutoInizio):
    minuti = (60) - int(minutoInizio) + int(minutoFine)
    ore -= 1
else:
    minuti = int(minutoFine) - int(minutoInizio)
if int(secondoFine) < int(secondoInizio):
    secondi = (60) - int(secondoInizio) + int(secondoFine)
    minuti -= 1
else:
    secondi = int(secondoFine) - int(secondoInizio)


### Controllo vincita ###
writeLog = open(filepath, "a")
if modalita == "V":
    if contatore_giocatore[0] == 5:
        print("###                                         MODALITA' VELOCE                                        ###" )
        print("\n" + "                                #########################################")
        print("                                ###                                   ###")
        print("                                ###             HAI VINTO!            ###")
        print("                                ###                                   ###")
        print("                                #########################################" + "\n")
        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente vince la partita \n")
    else:
        print("###                                         MODALITA' VELOCE                                        ###" )
        print("\n" + "                                #########################################")
        print("                                ###                                   ###")
        print("                                ###           HAI PERSO :(            ###")
        print("                                ###                                   ###")
        print("                                #########################################" + "\n")
        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente perde la partita \n")
elif modalita == "A":
    if contatore_giocatore[0] == 5:
        print("###                                         MODALITA' AMICI                                         ###" )
        print("\n" + "                                #########################################")
        print("                                ###                                   ###")
        print("                                ###        GIOCATORE 2 VINCE!         ###")
        print("                                ###                                   ###")
        print("                                #########################################" + "\n")
        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Giocatore 2 vince la partita \n")
    else:
        print("###                                         MODALITA' AMICI                                         ###" )
        print("\n" + "                                #########################################")
        print("                                ###                                   ###")
        print("                                ###        GIOCATORE 1 VINCE!         ###")
        print("                                ###                                   ###")
        print("                                #########################################" + "\n")
        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Giocatore 1 vince la partita \n")
elif modalita == "C":
    if contatore_giocatore[0] == 5:
        print("###                                         MODALITA' COMPUTER                                      ###" )
        print("\n" + "                                #########################################")
        print("                                ###                                   ###")
        print("                                ###         COMPUTER 2 VINCE!         ###")
        print("                                ###                                   ###")
        print("                                #########################################" + "\n")
        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Computer 2 vince la partita \n")
    else:
        print("###                                         MODALITA' COMPUTER                                      ###" )
        print("\n" + "                                #########################################")
        print("                                ###                                   ###")
        print("                                ###         COMPUTER 1 VINCE!         ###")
        print("                                ###                                   ###")
        print("                                #########################################" + "\n")
        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Computer 1 vince la partita \n")
else:
    if contatore_giocatore[0] == 17:
        if modalita == "F":
            print("###                                         MODALITA' FACILE                                         ###")
        elif modalita == "FOLLE":
            print("###                                          MODALITA' FOLLE                                         ###")
        elif modalita == "P":
            print("###                                       MODALITA' PREGENERATO                                      ###")
        elif modalita == "I":
            print("###                                       MODALITA' IMPOSSIBILE                                      ###")
        else:
            print("###                                       MODALITA' DIFFICILE                                        ###")
        print("\n" + "                                #########################################")
        print("                                ###                                   ###")
        print("                                ###             HAI VINTO!            ###")
        print("                                ###                                   ###")
        print("                                #########################################" + "\n")
        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente vince la partita \n")
    else:
        if modalita == "F":
            print("###                                         MODALITA' FACILE                                         ###")
        elif modalita == "FOLLE":
            print("###                                          MODALITA' FOLLE                                         ###")
        elif modalita == "P":
            print("###                                       MODALITA' PREGENERATO                                      ###")
        elif modalita == "I":
            print("###                                       MODALITA' IMPOSSIBILE                                      ###")
        else:
            print("###                                       MODALITA' DIFFICILE                                        ###")
        print("\n" + "                                #########################################")
        print("                                ###                                   ###")
        print("                                ###           HAI PERSO :(            ###")
        print("                                ###                                   ###")
        print("                                #########################################" + "\n")
        writeLog.write(str(datetime.datetime.now().strftime('%H:%M:%S')) + ": Utente perde la partita \n")

### Fine partita ###
if modalita == "A":
    print("###                                      LE DUE TABELLE ERANO:                                       ###")
    tabella_maker(righe_giocatore,righe_giocatore2)
elif modalita == "C":
    print("###                                      LE DUE TABELLE SONO:                                       ###")
    tabella_maker(righe_giocatore_inv,righe_giocatore2_inv)
else:
    print("###                                   LA TABELLA DEL COMPUTER ERA:                                   ###")
    tabella_maker(righe_PC_inv,righe_PC_inv)
print("\n" + "###                                 COMPLIMENTI HAI FINITO LA PARTITA...                             ###" + "\n")
print("\n" + "###                               LA PARTITA E' DURATA: " + str(int(ore)) + " ore, " + str(int(minuti)) + " minuti, " + str(int(secondi)) + " secondi." + "                 ###\n")
writeLog.write(str("Durata partita:" + str(int(ore)) + " ore, " + str(int(minuti)) + " minuti, " + str(int(secondi)) + " secondi." + " \n"))
writeLog.close()
input("Premi invio per terminare l'esecuzione...")
