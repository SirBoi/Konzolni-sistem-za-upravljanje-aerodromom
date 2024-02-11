from sys import exit
from os import system
from datetime import datetime, timedelta
from math import floor, ceil



from common import konstante
from korisnici import korisnici
from izvestaji import izvestaji
from karte import karte
from konkretni_letovi import konkretni_letovi
from letovi import letovi
from model_aviona import model_aviona
from aerodromi import aerodromi

aerodromi_fajl = "C:\\Users\\Administrator\\Documents\\FTN\\Semestar 1\\Osnove programiranja\\projekat_sa_konzolom\\projekat-2022-main\\fajlovi\\aerodromi.csv"
avioni_fajl = "C:\\Users\\Administrator\\Documents\\FTN\\Semestar 1\\Osnove programiranja\\projekat_sa_konzolom\\projekat-2022-main\\fajlovi\\avioni.csv"
karte_fajl = "C:\\Users\\Administrator\\Documents\\FTN\\Semestar 1\\Osnove programiranja\\projekat_sa_konzolom\\projekat-2022-main\\fajlovi\\karte.csv"
konkretni_letovi_fajl = "C:\\Users\\Administrator\\Documents\\FTN\\Semestar 1\\Osnove programiranja\\projekat_sa_konzolom\\projekat-2022-main\\fajlovi\\konkretni_letovi.csv"
korisnici_fajl = "C:\\Users\\Administrator\\Documents\\FTN\\Semestar 1\\Osnove programiranja\\projekat_sa_konzolom\\projekat-2022-main\\fajlovi\\korisnici.csv"
letovi_fajl = "C:\\Users\\Administrator\\Documents\\FTN\\Semestar 1\\Osnove programiranja\\projekat_sa_konzolom\\projekat-2022-main\\fajlovi\\letovi.csv"
konkretni_let = None
korisnik = None
korisnik2 = None

svi_aerodromi = {}
svi_avioni = {}
sve_karte = {}
svi_konkretni_letovi = {}
svi_korisnici = {}
svi_letovi = {}



def clear():
    system("cls")

def pocetni_meni():
    clear()
    print('''
--------------------

[1] Prijava
[2] Registracija
[3] Pregled nerealizovanih letova

[4] Izlaz

--------------------
    
    ''', end="")
    
    unos = None
    while unos not in ["1","2","3","4"]:
        unos = str(input())
    
    if unos == "1": return "prijava"
    if unos == "2": return "registracija_kupca"
    if unos == "3": return "pregled_nerealizovanih_letova"
    if unos == "4": return "izlaz"

def kupac_meni():
    clear()
    print('''
--------------------

[1] Kupovina karata
[2] Pregled nerealizovanih karata
[3] Prijava na let

[4] Izloguj se

--------------------
    
    ''', end="")

    unos = None
    while unos not in ["1","2","3","4"]:
        unos = str(input())
    if unos == "1": return "kupovina_karata_meni"
    if unos == "2": return "pregled_nerealizovanih_karata"
    if unos == "3": return "prijava_na_let_kupac"
    if unos == "4": return "pocetni_meni"

def prodavac_meni():
    clear()
    print('''
--------------------

[1] Prodaja karata
[2] Prijava na let
[3] Izmjena karte
[4] Brisanje karte
[5] Pretraga prodatih karata

[6] Izloguj se

--------------------
    
    ''', end="")

    unos = None
    while unos not in ["1","2","3","4","5","6"]:
        unos = str(input())
    if unos == "1": return "prodaja_karata_meni"
    if unos == "2": return "prijava_na_let_prodavac"
    if unos == "3": return "izmjena_karte"
    if unos == "4": return "brisanje_karte"
    if unos == "5": return "pretraga_prodatih_karata"
    if unos == "6": return "pocetni_meni"

def menadzer_meni():
    clear()
    print('''
--------------------

[1] Pretraga prodatih karata
[2] Registrovanje novih prodavaca
[3] Kreiranje letova
[4] Izmjena letova
[5] Brisanje karte
[6] Izvjestavanje
[7] Pretraga konkretnih letova
[8] Pretraga letova

[9] Izloguj se

--------------------
    
    ''', end="")

    unos = None
    while unos not in ["1","2","3","4","5","6","7","8","9"]:
        unos = str(input())
    if unos == "1": return "pretraga_prodatih_karata"
    if unos == "2": return "registrovanje_novih_prodavaca"
    if unos == "3": return "kreiranje_letova"
    if unos == "4": return "izmjena_letova"
    if unos == "5": return "brisanje_karte"
    if unos == "6": return "izvjestavanje_meni"
    if unos == "7": return "pretraga_konkretnih_letova_iz_menadzer_meni"
    if unos == "8": return "pretraga_letova"
    if unos == "9": return "pocetni_meni"

def kupovina_karata_meni():
    clear()
    print('''
--------------------

[1] Pretraga konkretnih letova
[2] Kupi kartu

[3] Nazad

--------------------
    
    ''', end="")

    unos = None
    while unos not in ["1","2","3"]:
        unos = str(input())
    if unos == "1": return "pretraga_konkretnih_letova_iz_kupovina_karata_meni"
    if unos == "2": return "kupi_kartu"
    if unos == "3": return "kupac_meni"

def kupi_kartu():
    global sve_karte, svi_konkretni_letovi, konkretni_let

    clear()
    print('''
--------------------

Sifra konkretnog leta: ''', end="")
    sifra = str(input())
    
    konkretni_let = svi_konkretni_letovi[int(sifra)]

    ima_mjesta = False
    for red in konkretni_let["zauzetost"]:
        if True in red:
            ima_mjesta = True
    
    if ima_mjesta:
        clear()
        print('''
--------------------

[1] Kupi kartu za sebe
[2] Kupi kartu za drugu osobu

--------------------
''', end="")
        unos = None
        while unos not in ["1","2"]:
            unos = str(input())
        if unos == "1": return "kupi_kartu_za_sebe"
        if unos == "2": return "kupi_kartu_za_drugu_osobu"

    else:
        clear()
        print('''
--------------------

Na izabranom letu nema slobodnih mjesta.

--------------------

''', end="")
    
        input()
        return "kupovina_karata_meni"

def kupi_kartu_za_sebe():
    global sve_karte, svi_konkretni_letovi, konkretni_let, korisnik

    zauzeto = False
    for red in konkretni_let["zauzetost"]:
        for i in range(len(red)):
            if red[i] == True:
                zauzeto = True
                break
        if zauzeto:
            break

    sifra = konkretni_let["sifra"]
    karte.kupovina_karte(sve_karte, svi_konkretni_letovi, konkretni_let["sifra"], [korisnik], konkretni_let["zauzetost"], korisnik, datum_prodaje=datetime.now())
    karte.sacuvaj_karte(sve_karte, karte_fajl, "|")
    konkretni_letovi.sacuvaj_kokretan_let(konkretni_letovi_fajl, "|", svi_konkretni_letovi)
    ucitaj_podatke()
    konkretni_let = svi_konkretni_letovi[sifra]

    return "nastavi_kupovinu_karata"

def kupi_kartu_za_drugu_osobu():
    global sve_karte, svi_konkretni_letovi, konkretni_let, korisnik

    clear()
    print('''
--------------------

Ime putnika: ''', end="")
    ime = str(input())
    clear()
    print('''
--------------------

Prezime putnika: ''', end="")
    prezime = str(input())

    temp_korisnik = None
    for korisnik_ in svi_korisnici:
        if svi_korisnici[korisnik_]["ime"] == ime and svi_korisnici[korisnik_]["prezime"] == prezime:
            temp_korisnik = svi_korisnici[korisnik_]
    if temp_korisnik == None:
        clear()
        print('''
--------------------

Korisnik nije registrovan.
    
--------------------''', end="")
        input()
        return "kupovina_karata_meni"

    sifra = konkretni_let["sifra"]
    karte.kupovina_karte(sve_karte, svi_konkretni_letovi, konkretni_let["sifra"], [temp_korisnik], konkretni_let["zauzetost"], korisnik, datum_prodaje=datetime.now())
    karte.sacuvaj_karte(sve_karte, karte_fajl, "|")
    konkretni_letovi.sacuvaj_kokretan_let(konkretni_letovi_fajl, "|", svi_konkretni_letovi)
    ucitaj_podatke()
    konkretni_let = svi_konkretni_letovi[sifra]

    return "nastavi_kupovinu_karata"

def nastavi_kupovinu_karata():
    clear()
    print('''
--------------------

Nastaviti kupovinu karata?

[1] Kupi kartu za povezani let
[2] Kupi kartu za saputnika

[3] Nazad

--------------------
    
''', end="")

    unos = None
    while unos not in ["1","2","3"]:
        unos = str(input())
    if unos == "1": return "kupi_kartu_za_povezani_let"
    if unos == "2": return "kupi_kartu_za_saputnika"
    if unos == "3": return "kupovina_karata_meni"

def kupi_kartu_za_povezani_let():
    global svi_letovi, konkretni_let

    polaziste = svi_letovi[konkretni_let["broj_leta"]]["sifra_odredisnog_aerodorma"]
    min_datum_i_vreme = konkretni_let["datum_i_vreme_dolaska"]
    max_datum_i_vreme = min_datum_i_vreme + timedelta(hours=2)

    pronadjeni_letovi = []
    for let in svi_letovi:
        if svi_letovi[let]["sifra_polazisnog_aerodroma"] == polaziste:
            pronadjeni_letovi.append(svi_letovi[let]["broj_leta"])

    pronadjeni_konkretni_letovi = []
    for let in svi_konkretni_letovi:
        if svi_konkretni_letovi[let]["datum_i_vreme_polaska"] >= min_datum_i_vreme and svi_konkretni_letovi[let]["datum_i_vreme_polaska"] <= max_datum_i_vreme:
            if svi_konkretni_letovi[let]["broj_leta"] in pronadjeni_letovi:
                pronadjeni_konkretni_letovi.append(svi_konkretni_letovi[let])

    clear()
    if pronadjeni_konkretni_letovi == []:
        print('''
--------------------
    
Ne postoje letovi povezani sa kupljenim.
    
--------------------

''', end="")

    else:
        print('''
--------------------

Dostupni konkretni letovi:

          Broj           |          Sifra          |         Polazak         |         Dolazak         

''', end="")

        for konkretni_let in pronadjeni_konkretni_letovi:
            for i in ["broj_leta", "sifra", "datum_i_vreme_polaska", "datum_i_vreme_dolaska"]:
                word = str(konkretni_let[i])
                n = 25 - len(word)

                print(" " * floor(n/2.0) + word + " " * ceil(n/2.0), end="")
                if i != "datum_i_vreme_dolaska": print("|", end="")
                if i == "datum_i_vreme_dolaska": print("")

    input()
    return "kupovina_karata_meni"

def kupi_kartu_za_saputnika():
    return "kupi_kartu_za_drugu_osobu"

def pregled_nerealizovanih_karata():
    global sve_karte, svi_konkretni_letovi, korisnik
    
    pronadjene_karte = []
    for karta in sve_karte:
        if sve_karte[karta]["status"] == konstante.STATUS_NEREALIZOVANA_KARTA:
            if sve_karte[karta]["kupac"] == korisnik or korisnik in sve_karte[karta]["putnici"]:
                pronadjene_karte.append(sve_karte[karta])
    
    clear()
    print('''
       Broj karte        |  Sifra konkretnog leta  |         Polazak         |         Putnik          

''', end="")

    for karta in pronadjene_karte:
        data1 = str(karta["broj_karte"])
        data2 = str(karta["sifra_konkretnog_leta"])
        data3 = str(svi_konkretni_letovi[karta["sifra_konkretnog_leta"]]["datum_i_vreme_polaska"])
        data4 = str(karta["putnici"][0]["ime"]) + " " + str(karta["putnici"][0]["prezime"])

        for i in [data1, data2, data3, data4]:
            n = 25 - len(i)

            print(" " * floor(n/2.0) + i + " " * ceil(n/2.0), end="")
            if i != data4: print("|", end="")
            if i == data4: print("")
    input()

    return "kupac_meni"

def prijava_na_let_kupac():
    global korisnik, sve_karte, svi_konkretni_letovi, konkretni_let

    clear()
    print('''
--------------------

Broj karte: ''', end="")
    broj_karte = str(input())

    if int(broj_karte) not in sve_karte:
        clear()
        print('''
--------------------

Ta karta ne postoji.

--------------------''', end="")
        input()
        return "kupac_meni"
    if sve_karte[int(broj_karte)]["status"] == konstante.STATUS_REALIZOVANA_KARTA:
        clear()
        print('''
--------------------

Karta je vec realizovana.

--------------------''', end="")
        input()
        return "kupac_meni"
    if korisnik not in sve_karte[int(broj_karte)]["putnici"]:
        clear()
        print('''
--------------------

To nije vasa karta.

--------------------''', end="")
        input()
        return "kupac_meni"
    
    sjedista = svi_konkretni_letovi[sve_karte[int(broj_karte)]["sifra_konkretnog_leta"]]["zauzetost"]
    konkretni_let = svi_konkretni_letovi[sve_karte[int(broj_karte)]["sifra_konkretnog_leta"]]

    clear()
    print('''
--------------------

Sjedista:

''')

    for i in range(len(sjedista)):
        print(f"Red {i+1}:\t\t", end="")
        for sjediste in sjedista[i]:
            if sjediste == True: print("O ", end="")
            else: print("X ", end="")
        print()
    print('''
Format: 0 0

Red i broj sjedista: ''', end="")
    sjediste = str(input())
    izbor = sjediste.split(" ")

    if sjedista[int(izbor[0])-1][int(izbor[1])-1] == False:
        clear()
        print('''
--------------------

To sjediste je vec zauzeto.

--------------------''')
        input()
    else:
        svi_konkretni_letovi[sve_karte[int(broj_karte)]["sifra_konkretnog_leta"]]["zauzetost"][int(izbor[0])-1][int(izbor[1])-1] = False
        sve_karte[int(broj_karte)]["status"] = konstante.STATUS_REALIZOVANA_KARTA

        sifra = konkretni_let["sifra"]
        karte.sacuvaj_karte(sve_karte, karte_fajl, "|")
        konkretni_letovi.sacuvaj_kokretan_let(konkretni_letovi_fajl, "|", svi_konkretni_letovi)
        ucitaj_podatke()
        konkretni_let = svi_konkretni_letovi[sifra]
    
    return "kupac_meni"

def prodaja_karata_meni():
    clear()
    print('''
--------------------

[1] Pretraga konkretnih letova
[2] Prodaj kartu

[3] Nazad

--------------------
    
    ''', end="")

    unos = None
    while unos not in ["1","2","3"]:
        unos = str(input())
    if unos == "1": return "pretraga_konkretnih_letova_iz_prodaja_karata_meni"
    if unos == "2": return "prodaj_kartu"
    if unos == "3": return "prodavac_meni"

def prodaj_kartu():
    global sve_karte, svi_konkretni_letovi, konkretni_let, korisnik, korisnik2

    clear()
    print('''
--------------------

Sifra konkretnog leta: ''', end="")
    sifra = str(input())
    konkretni_let = svi_konkretni_letovi[int(sifra)]

    ima_mjesta = False
    for red in konkretni_let["zauzetost"]:
        if True in red:
            ima_mjesta = True
    
    if ima_mjesta:
        clear()
        print('''
--------------------

Korisnicko ime kupca: ''', end="")
        korisnicko_ime = str(input())
        
        if korisnicko_ime in svi_korisnici:
            korisnik2 = svi_korisnici[korisnicko_ime]
            return "prodaj_kartu_registrovanom"
        else:
            clear()
            print('''
--------------------

Korisnik nije registrovan.

--------------------''', end="")
            input()
            return "prodaj_kartu_neregistrovanom"
    else:
        clear()
        print('''
--------------------

Na izabranom letu nema slobodnih mjesta.

--------------------

''', end="")
    
        input()
        return "kupovina_karata_meni"

def prodaj_kartu_registrovanom():
    global korisnik, sve_karte, konkretni_let

    sifra = konkretni_let["sifra"]
    karte.kupovina_karte(sve_karte, svi_konkretni_letovi, konkretni_let["sifra"], [korisnik2], konkretni_let["zauzetost"], korisnik, datum_prodaje=datetime.now())
    karte.sacuvaj_karte(sve_karte, karte_fajl, "|")
    konkretni_letovi.sacuvaj_kokretan_let(konkretni_letovi_fajl, "|", svi_konkretni_letovi)
    ucitaj_podatke()
    konkretni_let = svi_konkretni_letovi[sifra]

    return "nastavi_prodaju_karata"

def prodaj_kartu_neregistrovanom():
    global svi_korisnici, korisnik, korisnik2

    clear()
    print('''
--------------------

Korisnicko ime: ''', end="")
    korisnicko_ime = str(input())
    clear()
    print('''
--------------------

Lozinka: ''', end="")
    lozinka = str(input())
    clear()
    print('''
--------------------

Telefon: ''', end="")
    telefon = str(input())
    clear()
    print('''
--------------------

E-mail: ''', end="")
    email = str(input())
    clear()
    print('''
--------------------

Ime: ''', end="")
    ime = str(input())
    clear()
    print('''
--------------------

Prezime: ''', end="")
    prezime = str(input())
    clear()
    print('''
--------------------

Unesite 0 da preskocite unos ovog podatka.

Pasos: ''', end="")
    pasos = str(input())
    clear()
    print('''
--------------------

Unesite 0 da preskocite unos ovog podatka.

Drzavljanstvo: ''', end="")
    drzavljanstvo = str(input())
    clear()
    print('''
--------------------

Unesite 0 da preskocite unos ovog podatka.
    
Pol: ''', end="")
    pol = str(input())
    uloga = konstante.ULOGA_KORISNIK

    korisnici.kreiraj_korisnika(svi_korisnici, False, uloga, None, korisnicko_ime, lozinka, ime, prezime, email, pasos, drzavljanstvo, telefon, pol)
    korisnici.sacuvaj_korisnike(korisnici_fajl, "|", svi_korisnici)
    korisnik2 = svi_korisnici[korisnicko_ime]

    sifra = konkretni_let["sifra"]
    karte.kupovina_karte(sve_karte, svi_konkretni_letovi, konkretni_let["sifra"], [korisnik2], konkretni_let["zauzetost"], korisnik, datum_prodaje=datetime.now())
    karte.sacuvaj_karte(sve_karte, karte_fajl, "|")
    konkretni_letovi.sacuvaj_kokretan_let(konkretni_letovi_fajl, "|", svi_konkretni_letovi)
    ucitaj_podatke()
    konkretni_let = svi_konkretni_letovi[sifra]

    return "nastavi_prodaju_karata"

def nastavi_prodaju_karata():
    clear()
    print('''
--------------------

Nastaviti kupovinu karata?

[1] Prodaj kartu za povezani let
[2] Prodaj kartu za saputnika

[3] Nazad

--------------------
    
    ''', end="")

    unos = None
    while unos not in ["1","2","3"]:
        unos = str(input())
    if unos == "1": return "prodaj_kartu_za_povezani_let"
    if unos == "2": return "prodaj_kartu_za_saputnika"
    if unos == "3": return "prodaja_karata_meni"

def prodaj_kartu_za_povezani_let():
    global svi_letovi, konkretni_let

    polaziste = svi_letovi[konkretni_let["broj_leta"]]["sifra_odredisnog_aerodorma"]
    min_datum_i_vreme = konkretni_let["datum_i_vreme_dolaska"]
    max_datum_i_vreme = min_datum_i_vreme + timedelta(hours=2)

    pronadjeni_letovi = []
    for let in svi_letovi:
        if svi_letovi[let]["sifra_polazisnog_aerodroma"] == polaziste:
            pronadjeni_letovi.append(svi_letovi[let]["broj_leta"])

    pronadjeni_konkretni_letovi = []
    for let in svi_konkretni_letovi:
        if svi_konkretni_letovi[let]["datum_i_vreme_polaska"] >= min_datum_i_vreme and svi_konkretni_letovi[let]["datum_i_vreme_polaska"] <= max_datum_i_vreme:
            if svi_konkretni_letovi[let]["broj_leta"] in pronadjeni_letovi:
                pronadjeni_konkretni_letovi.append(svi_konkretni_letovi[let])

    clear()
    if pronadjeni_konkretni_letovi == []:
        print('''
--------------------
    
Ne postoje letovi povezani sa prodatim.
    
--------------------

''', end="")

    else:
        print('''
--------------------

Dostupni konkretni letovi:

          Broj           |          Sifra          |         Polazak         |         Dolazak         

''', end="")

        for konkretni_let in pronadjeni_konkretni_letovi:
            for i in ["broj_leta", "sifra", "datum_i_vreme_polaska", "datum_i_vreme_dolaska"]:
                word = str(konkretni_let[i])
                n = 25 - len(word)

                print(" " * floor(n/2.0) + word + " " * ceil(n/2.0), end="")
                if i != "datum_i_vreme_dolaska": print("|", end="")
                if i == "datum_i_vreme_dolaska": print("")

    input()
    return "prodaja_karata_meni"

def prodaj_kartu_za_saputnika():
    global sve_karte, svi_konkretni_letovi, konkretni_let, korisnik

    clear()
    print('''
--------------------

Ime putnika: ''', end="")
    ime = str(input())
    clear()
    print('''
--------------------

Prezime putnika: ''', end="")
    prezime = str(input())

    temp_korisnik = None
    for korisnik_ in svi_korisnici:
        if svi_korisnici[korisnik_]["ime"] == ime and svi_korisnici[korisnik_]["prezime"] == prezime:
            temp_korisnik = svi_korisnici[korisnik_]
    if temp_korisnik == None:
        clear()
        print('''
--------------------

Korisnik nije registrovan.
    
--------------------''', end="")
        input()
        return "prodaj_kartu_neregistrovanom"

    sifra = konkretni_let["sifra"]
    karte.kupovina_karte(sve_karte, svi_konkretni_letovi, konkretni_let["sifra"], [temp_korisnik], konkretni_let["zauzetost"], korisnik, datum_prodaje=datetime.now())
    karte.sacuvaj_karte(sve_karte, karte_fajl, "|")
    konkretni_letovi.sacuvaj_kokretan_let(konkretni_letovi_fajl, "|", svi_konkretni_letovi)
    ucitaj_podatke()
    konkretni_let = svi_konkretni_letovi[sifra]

    return "nastavi_prodaju_karata"

def prijava_na_let_prodavac():
    global korisnik, sve_karte, svi_konkretni_letovi, konkretni_let

    clear()
    print('''
--------------------

Broj karte: ''', end="")
    broj_karte = str(input())

    if int(broj_karte) not in sve_karte:
        clear()
        print('''
--------------------

Ta karta ne postoji.

--------------------''', end="")
        input()
        return "kupac_meni"
    if sve_karte[int(broj_karte)]["status"] == konstante.STATUS_REALIZOVANA_KARTA:
        clear()
        print('''
--------------------

Karta je vec realizovana.

--------------------''', end="")
        input()
        return "kupac_meni"
    
    sjedista = svi_konkretni_letovi[sve_karte[int(broj_karte)]["sifra_konkretnog_leta"]]["zauzetost"]
    konkretni_let = svi_konkretni_letovi[sve_karte[int(broj_karte)]["sifra_konkretnog_leta"]]

    clear()
    print('''
--------------------

Sjedista:

''')

    for i in range(len(sjedista)):
        print(f"Red {i+1}:\t\t", end="")
        for sjediste in sjedista[i]:
            if sjediste == True: print("O ", end="")
            else: print("X ", end="")
        print()
    print('''
Format: 0 0

Red i broj sjedista: ''', end="")
    sjediste = str(input())
    izbor = sjediste.split(" ")

    if sjedista[int(izbor[0])-1][int(izbor[1])-1] == False:
        clear()
        print('''
--------------------

To sjediste je vec zauzeto.

--------------------''')
        input()
    else:
        svi_konkretni_letovi[sve_karte[int(broj_karte)]["sifra_konkretnog_leta"]]["zauzetost"][int(izbor[0])-1][int(izbor[1])-1] = False
        sve_karte[int(broj_karte)]["status"] = konstante.STATUS_REALIZOVANA_KARTA

        sifra = konkretni_let["sifra"]
        karte.sacuvaj_karte(sve_karte, karte_fajl, "|")
        konkretni_letovi.sacuvaj_kokretan_let(konkretni_letovi_fajl, "|", svi_konkretni_letovi)
        ucitaj_podatke()
        konkretni_let = svi_konkretni_letovi[sifra]
    
    return "prodavac_meni"

def izmjena_karte():
    global svi_konkretni_letovi, sve_karte

    clear()
    print('''
--------------------

Broj karte: ''', end="")
    broj_karte = str(input())

    clear()
    print('''
--------------------

Unesite zeljene parametre za pretragu.
Unesite '0' da preskocite parametar.

Nova sifra leta: ''', end="")
    sifra = str(input())

    
    clear()
    print('''
--------------------

Unesite zeljene parametre za pretragu.
Unesite '0' da preskocite parametar.

Format: GGGG-MM-DD HH:MM

Datum i vrijeme polaska: ''', end="")
    polazak = str(input())
    polazak = datetime.strptime(polazak, "%Y-%m-%d %H:%M")
    
    karte.izmena_karte(sve_karte, svi_konkretni_letovi, int(broj_karte), sifra, polazak)

    karte.sacuvaj_karte(sve_karte, karte_fajl, "|")
    konkretni_letovi.sacuvaj_kokretan_let(konkretni_letovi_fajl, "|", svi_konkretni_letovi)
    ucitaj_podatke()

    return "prodavac_meni"

def brisanje_karte():
    global svi_konkretni_letovi, sve_karte, korisnik

    clear()
    print('''
--------------------

Broj karte: ''', end="")
    broj_karte = str(input())
    
    if int(broj_karte) in sve_karte:
        karte.brisanje_karte(korisnik, sve_karte, int(broj_karte))

        karte.sacuvaj_karte(sve_karte, karte_fajl, "|")
        konkretni_letovi.sacuvaj_kokretan_let(konkretni_letovi_fajl, "|", svi_konkretni_letovi)
        ucitaj_podatke()
    else:
        clear()
        print('''
--------------------

Ta karta ne postoji.

--------------------''')
        input()

    return "prodavac_meni"

def pretraga_prodatih_karata():
    global svi_konkretni_letovi

    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: AAA

    Polaziste: ''', end="")
    polaziste = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: AAA

    Odrediste: ''', end="")
    odrediste = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: GGGG-MM-DD HH:MM

    Datum i vrijeme polaska: ''', end="")
    polazak = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: GGGG-MM-DD HH:MM

    Datum i vrijeme dolaska: ''', end="")
    dolazak = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Ime putnika: ''', end="")
    ime = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Prezime putnika: ''', end="")
    prezime = str(input())

    clear()
    print('''
       Broj karte        |  Sifra konkretnog leta  |         Polazak         |         Putnik          

''', end="")

    pronadjene_karte = []
    for karta in sve_karte:
        if polaziste != "0" and svi_letovi[svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["broj_leta"]]["sifra_polazisnog_aerodroma"] != polaziste:
            continue
        if odrediste != "0" and svi_letovi[svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["broj_leta"]]["sifra_odredisnog_aerodroma"] != odrediste:
            continue
        if polazak != "0" and svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["datum_i_vreme_polaska"] != datetime.strptime(polazak, "%Y-%m-%d %H:%M"):
            continue
        if dolazak != "0" and svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["datum_i_vreme_dolaska"] != datetime.strptime(dolazak, "%Y-%m-%d %H:%M"):
            continue
        if ime != "0" and sve_karte[karta]["putnici"][0]["ime"] != ime:
            continue
        if prezime != "0" and sve_karte[karta]["putnici"][0]["prezime"] != prezime:
            continue
        pronadjene_karte.append(sve_karte[karta])

    clear()
    print('''
       Broj karte        |  Sifra konkretnog leta  |         Polazak         |         Putnik          

''', end="")

    for karta in pronadjene_karte:
        data1 = str(karta["broj_karte"])
        data2 = str(karta["sifra_konkretnog_leta"])
        data3 = str(svi_konkretni_letovi[karta["sifra_konkretnog_leta"]]["datum_i_vreme_polaska"])
        data4 = str(karta["putnici"][0]["ime"]) + " " + str(karta["putnici"][0]["prezime"])

        for i in [data1, data2, data3, data4]:
            n = 25 - len(i)

            print(" " * floor(n/2.0) + i + " " * ceil(n/2.0), end="")
            if i != data4: print("|", end="")
            if i == data4: print("")
    input()

    return "prodavac_meni"

def pretraga_konkretnih_letova_iz_menadzer_meni():
    global svi_konkretni_letovi

    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: AA00

    Broj konkretnog leta: ''', end="")
    broj = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Sifra konkretnog leta: ''', end="")
    sifra = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: GGGG-MM-DD HH:MM

    Datum i vrijeme polaska: ''', end="")
    polazak = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: GGGG-MM-DD HH:MM

    Datum i vrijeme dolaska: ''', end="")
    dolazak = str(input())

    pronadjeni_konkretni_letovi = []
    for let in svi_konkretni_letovi:
        if svi_konkretni_letovi[let] not in pronadjeni_konkretni_letovi:
            if broj != "0" and svi_konkretni_letovi[let]["broj_leta"] != broj:
                continue
            if sifra != "0" and str(svi_konkretni_letovi[let]["sifra"]) != sifra:
                continue
            if polazak != "0" and svi_konkretni_letovi[let]["datum_i_vreme_polaska"].strftime("%Y-%m-%d %H:%M") != polazak:
                continue
            if dolazak != "0" and svi_konkretni_letovi[let]["datum_i_vreme_dolaska"].strftime("%Y-%m-%d %H:%M") != dolazak:
                continue
            pronadjeni_konkretni_letovi.append(svi_konkretni_letovi[let])

    clear()
    print('''
          Broj           |          Sifra          |         Polazak         |         Dolazak         

''', end="")

    for konkretni_let in pronadjeni_konkretni_letovi:
        for i in ["broj_leta", "sifra", "datum_i_vreme_polaska", "datum_i_vreme_dolaska"]:
            word = str(konkretni_let[i])
            n = 25 - len(word)

            print(" " * floor(n/2.0) + word + " " * ceil(n/2.0), end="")
            if i != "datum_i_vreme_dolaska": print("|", end="")
            if i == "datum_i_vreme_dolaska": print("")
    input()

    return "menadzer_meni"

def pretraga_konkretnih_letova_iz_kupovina_karata_meni():
    global svi_konkretni_letovi

    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: AA00

    Broj konkretnog leta: ''', end="")
    broj = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Sifra konkretnog leta: ''', end="")
    sifra = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: GGGG-MM-DD HH:MM

    Datum i vrijeme polaska: ''', end="")
    polazak = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: GGGG-MM-DD HH:MM

    Datum i vrijeme dolaska: ''', end="")
    dolazak = str(input())

    pronadjeni_konkretni_letovi = []
    for let in svi_konkretni_letovi:
        if svi_konkretni_letovi[let] not in pronadjeni_konkretni_letovi:
            if broj != "0" and svi_konkretni_letovi[let]["broj_leta"] != broj:
                continue
            if sifra != "0" and str(svi_konkretni_letovi[let]["sifra"]) != sifra:
                continue
            if polazak != "0" and svi_konkretni_letovi[let]["datum_i_vreme_polaska"].strftime("%Y-%m-%d %H:%M") != polazak:
                continue
            if dolazak != "0" and svi_konkretni_letovi[let]["datum_i_vreme_dolaska"].strftime("%Y-%m-%d %H:%M") != dolazak:
                continue
            pronadjeni_konkretni_letovi.append(svi_konkretni_letovi[let])

    clear()
    print('''
          Broj           |          Sifra          |         Polazak         |         Dolazak         

''', end="")

    for konkretni_let in pronadjeni_konkretni_letovi:
        for i in ["broj_leta", "sifra", "datum_i_vreme_polaska", "datum_i_vreme_dolaska"]:
            word = str(konkretni_let[i])
            n = 25 - len(word)

            print(" " * floor(n/2.0) + word + " " * ceil(n/2.0), end="")
            if i != "datum_i_vreme_dolaska": print("|", end="")
            if i == "datum_i_vreme_dolaska": print("")
    input()

    return "kupovina_karata_meni"

def pretraga_konkretnih_letova_iz_prodaja_karata_meni():
    global svi_konkretni_letovi

    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: AA00

    Broj konkretnog leta: ''', end="")
    broj = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Sifra konkretnog leta: ''', end="")
    sifra = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: GGGG-MM-DD HH:MM

    Datum i vrijeme polaska: ''', end="")
    polazak = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: GGGG-MM-DD HH:MM

    Datum i vrijeme dolaska: ''', end="")
    dolazak = str(input())

    pronadjeni_konkretni_letovi = []
    for let in svi_konkretni_letovi:
        if svi_konkretni_letovi[let] not in pronadjeni_konkretni_letovi:
            if broj != "0" and svi_konkretni_letovi[let]["broj_leta"] != broj:
                continue
            if sifra != "0" and str(svi_konkretni_letovi[let]["sifra"]) != sifra:
                continue
            if polazak != "0" and svi_konkretni_letovi[let]["datum_i_vreme_polaska"].strftime("%Y-%m-%d %H:%M") != polazak:
                continue
            if dolazak != "0" and svi_konkretni_letovi[let]["datum_i_vreme_dolaska"].strftime("%Y-%m-%d %H:%M") != dolazak:
                continue
            pronadjeni_konkretni_letovi.append(svi_konkretni_letovi[let])

    clear()
    print('''
          Broj           |          Sifra          |         Polazak         |         Dolazak         

''', end="")

    for konkretni_let in pronadjeni_konkretni_letovi:
        for i in ["broj_leta", "sifra", "datum_i_vreme_polaska", "datum_i_vreme_dolaska"]:
            word = str(konkretni_let[i])
            n = 25 - len(word)

            print(" " * floor(n/2.0) + word + " " * ceil(n/2.0), end="")
            if i != "datum_i_vreme_dolaska": print("|", end="")
            if i == "datum_i_vreme_dolaska": print("")
    input()

    return "prodaja_karata_meni"

def pretraga_letova():
    global svi_letovi

    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: AA00

    Broj leta: ''', end="")
    broj = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: AAA

    Sifra polazisnog aerodroma: ''', end="")
    polaziste = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: AAA

    Sifra odredisnog aerodroma: ''', end="")
    odrediste = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: HH:MM

    Vrijeme polaska: ''', end="")
    polazak_vrijeme = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: HH:MM

    Vrijeme dolaska: ''', end="")
    dolazak_vrijeme = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: GGGG-MM-DD

    Datum polaska: ''', end="")
    pocetak = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: GGGG-MM-DD

    Datum dolaska: ''', end="")
    kraj = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Prevoznik: ''', end="")
    prevoznik = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Sifra aviona: ''', end="")
    avion_sifra = str(input())
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Format: 1,2,3 (Brojevi od 1 do 7 razdvojeni zarezom)

    1 - Ponedeljak
    2 - Utorak
    3 - Srijeda
    4 - Cetvrtak
    5 - Petak
    6 - Subota
    7 - Nedelja

    Dani: ''', end="")
    dani = str(input())
    dani = dani.split(",")
    dani.sort()
    dani = [int(dan) for dan in dani]
    clear()
    print('''
    --------------------

    Unesite zeljene parametre za pretragu.
    Unesite '0' da preskocite parametar.

    Cijena: ''', end="")
    cijena = str(input())

    pronadjeni_letovi = []
    for let in svi_letovi:
        if svi_letovi[let] not in pronadjeni_letovi:
            if broj != "0" and svi_letovi[let]["broj_leta"] != broj:
                continue
            if polaziste != "0" and svi_letovi[let]["sifra_polazisnog_aerodroma"] != polaziste:
                continue
            if odrediste != "0" and svi_letovi[let]["sifra_odredisnog_aerodorma"] != odrediste:
                continue
            if polazak_vrijeme != "0" and svi_letovi[let]["vreme_poletanja"].strftime("%H:%M") != polazak_vrijeme:
                continue
            if dolazak_vrijeme != "0" and svi_letovi[let]["vreme_sletanja"].strftime("%H:%M") != dolazak_vrijeme:
                continue
            if pocetak != "0" and svi_letovi[let]["datum_pocetka_operativnosti"].strftime("%Y-%m-%d") != pocetak:
                continue
            if kraj != "0" and svi_letovi[let]["datum_kraja_operativnosti"].strftime("%Y-%m-%d") != kraj:
                continue
            if prevoznik != "0" and svi_letovi[let]["prevoznik"] != prevoznik:
                continue
            if avion_sifra != "0" and str(svi_letovi[let]["model"]["id"]) != avion_sifra:
                continue
            if dani != [0] and svi_letovi[let]["dani"] != dani:
                print(dani)
                continue
            if cijena != "0" and str(svi_letovi[let]["cena"]) != cijena:
                continue
            pronadjeni_letovi.append(svi_letovi[let])

    clear()
    print('''
     Broj leta      |     Polaziste      |     Odrediste      | Vrijeme poljetanja | Vrijeme sljetanja  |    Pocetak op.     |      Kraj op.      |     Prevoznik      |        Dani        |       Cijena       

''', end="")

    for let in pronadjeni_letovi:
        for i in ["broj_leta", "sifra_polazisnog_aerodroma", "sifra_odredisnog_aerodorma", "vreme_poletanja", "vreme_sletanja", "datum_pocetka_operativnosti", "datum_kraja_operativnosti", "prevoznik", "dani", "cena"]:
            word = str(let[i])
            n = 20 - len(word)

            print(" " * floor(n/2.0) + word + " " * ceil(n/2.0), end="")
            if i != "cena": print("|", end="")
            if i == "cena": print("")
    input()

    return "menadzer_meni"

def registrovanje_novih_prodavaca():
    global svi_korisnici

    clear()
    print('''
    --------------------

    Korisnicko ime: ''', end="")
    korisnicko_ime = str(input())
    clear()
    print('''
    --------------------

    Lozinka: ''', end="")
    lozinka = str(input())
    clear()
    print('''
    --------------------

    Telefon: ''', end="")
    telefon = str(input())
    clear()
    print('''
    --------------------

    E-mail: ''', end="")
    email = str(input())
    clear()
    print('''
    --------------------

    Ime: ''', end="")
    ime = str(input())
    clear()
    print('''
    --------------------

    Prezime: ''', end="")
    prezime = str(input())
    clear()
    print('''
    --------------------

    Unesite 0 da preskocite unos ovog podatka.

    Pasos: ''', end="")
    pasos = str(input())
    clear()
    print('''
    --------------------

    Unesite 0 da preskocite unos ovog podatka.

    Drzavljanstvo: ''', end="")
    drzavljanstvo = str(input())
    clear()
    print('''
    --------------------

    Unesite 0 da preskocite unos ovog podatka.
    
    Pol: ''', end="")
    pol = str(input())
    uloga = konstante.ULOGA_PRODAVAC

    korisnici.kreiraj_korisnika(svi_korisnici, False, uloga, None, korisnicko_ime, lozinka, ime, prezime, email, pasos, drzavljanstvo, telefon, pol)
    korisnici.sacuvaj_korisnike(korisnici_fajl, "|", svi_korisnici)

    return "menadzer_meni"

def kreiranje_letova():
    global svi_letovi

    clear()
    print('''
    --------------------

    Format: AA00

    Broj leta: ''', end="")
    broj_leta = str(input())
    clear()
    print('''
    --------------------

    Format: AAA

    Sifra polazisnog aerodroma: ''', end="")
    sifra_polazisnog_aerodroma = str(input())
    if sifra_polazisnog_aerodroma not in svi_aerodromi:
        sifra_polazisnog_aerodroma = "polaziste"
    clear()
    print('''
    --------------------

    Format: AAA

    Sifra odredisnog aerodroma: ''', end="")
    sifra_odredisnog_aerodroma = str(input())
    if sifra_odredisnog_aerodroma not in svi_aerodromi:
        sifra_odredisnog_aerodroma = "odrediste"
    clear()
    print('''
    --------------------

    Format: HH:MM

    Vrijeme poljetanja: ''', end="")
    vreme_poletanja = str(input())
    clear()
    print('''
    --------------------

    Format: HH:MM

    Vrijeme sljetanja: ''', end="")
    vreme_sletanja = str(input())
    clear()
    print('''
    --------------------

    Format: Da/Ne

    Sljetanje sutra: ''', end="")
    sletanje_sutra = str(input())
    if sletanje_sutra.lower() == "da":
        sletanje_sutra = True
    elif sletanje_sutra.lower() == "ne":
        sletanje_sutra = False
    clear()
    print('''
    --------------------

    Prevoznik: ''', end="")
    prevoznik = str(input())
    clear()
    print('''
    --------------------

    Format: 1,2,3 (Brojevi od 1 do 7 razdvojeni zarezom)

    1 - Ponedeljak
    2 - Utorak
    3 - Srijeda
    4 - Cetvrtak
    5 - Petak
    6 - Subota
    7 - Nedelja

    Dani: ''', end="")
    dani = str(input())
    dani = dani.split(",")
    dani.sort()
    dani = [int(dan) for dan in dani]
    clear()
    print('''
    --------------------
    
    ID modela aviona: ''', end="")
    model = str(input())
    try:
        model = svi_avioni[int(model)]
    except:
        0
    clear()
    print('''
    --------------------
    
    Cijena: ''', end="")
    try:
        cena = float(input())
    except:
        cena = 0
    clear()
    print('''
    --------------------

    Format: GGGG-MM-DD
    
    Datum pocetka operativnosti: ''', end="")
    datum_pocetka_operativnosti = str(input())
    try:
        datum_pocetka_operativnosti = datetime.strptime(datum_pocetka_operativnosti, "%Y-%m-%d")
    except:
        0
    clear()
    print('''
    --------------------

    Format: GGGG-MM-DD
    
    Datum kraja operativnosti: ''', end="")
    datum_kraja_operativnosti = str(input())
    try:
        datum_kraja_operativnosti = datetime.strptime(datum_kraja_operativnosti, "%Y-%m-%d")
    except:
        0

    letovi.kreiranje_letova(svi_letovi, broj_leta, sifra_polazisnog_aerodroma, sifra_odredisnog_aerodroma, vreme_poletanja, vreme_sletanja, sletanje_sutra, prevoznik, dani, model, cena, datum_pocetka_operativnosti, datum_kraja_operativnosti)
    letovi.sacuvaj_letove(letovi_fajl, "|", svi_letovi)
    konkretni_letovi.kreiranje_konkretnog_leta(svi_konkretni_letovi, svi_letovi[broj_leta])
    for konkretni_let in svi_konkretni_letovi:
        letovi.podesi_matricu_zauzetosti(svi_letovi, svi_konkretni_letovi[konkretni_let])
    konkretni_letovi.sacuvaj_kokretan_let(konkretni_letovi_fajl, "|", svi_konkretni_letovi)

    return "menadzer_meni"

def pregled_nerealizovanih_letova():
    global svi_letovi

    nerealizovani_letovi = letovi.pregled_nerealizoivanih_letova(svi_letovi)

    clear()
    print('''
     Broj leta      |     Polaziste      |     Odrediste      | Vrijeme poljetanja | Vrijeme sljetanja  |    Pocetak op.     |      Kraj op.      |     Prevoznik      |        Dani        |       Cijena       

''', end="")

    for let in nerealizovani_letovi:
        for i in ["broj_leta", "sifra_polazisnog_aerodroma", "sifra_odredisnog_aerodorma", "vreme_poletanja", "vreme_sletanja", "datum_pocetka_operativnosti", "datum_kraja_operativnosti", "prevoznik", "dani", "cena"]:
            word = str(let[i])
            n = 20 - len(word)

            print(" " * floor(n/2.0) + word + " " * ceil(n/2.0), end="")
            if i != "cena": print("|", end="")
            if i == "cena": print("")
    input()

    return "pocetni_meni"

def izmjena_letova():
    global svi_konkretni_letovi, svi_letovi

    clear()
    print('''
    --------------------

    Format: AA00

    Broj leta: ''', end="")
    broj_leta = str(input())
    clear()
    print('''
    --------------------

    Format: AAA

    Sifra polazisnog aerodroma: ''', end="")
    sifra_polazisnog_aerodroma = str(input())
    if sifra_polazisnog_aerodroma not in svi_aerodromi:
        sifra_polazisnog_aerodroma = "polaziste"
    clear()
    print('''
    --------------------

    Format: AAA

    Sifra odredisnog aerodroma: ''', end="")
    sifra_odredisnog_aerodroma = str(input())
    if sifra_odredisnog_aerodroma not in svi_aerodromi:
        sifra_odredisnog_aerodroma = "odrediste"
    clear()
    print('''
    --------------------

    Format: HH:MM

    Vrijeme poljetanja: ''', end="")
    vreme_poletanja = str(input())
    clear()
    print('''
    --------------------

    Format: HH:MM

    Vrijeme sljetanja: ''', end="")
    vreme_sletanja = str(input())
    clear()
    print('''
    --------------------

    Format: Da/Ne

    Sljetanje sutra: ''', end="")
    sletanje_sutra = str(input())
    if sletanje_sutra.lower() == "da":
        sletanje_sutra = True
    elif sletanje_sutra.lower() == "ne":
        sletanje_sutra = False
    clear()
    print('''
    --------------------

    Prevoznik: ''', end="")
    prevoznik = str(input())
    clear()
    print('''
    --------------------

    Format: 1,2,3 (Brojevi od 1 do 7 razdvojeni zarezom)

    1 - Ponedeljak
    2 - Utorak
    3 - Srijeda
    4 - Cetvrtak
    5 - Petak
    6 - Subota
    7 - Nedelja

    Dani: ''', end="")
    dani = str(input())
    dani = dani.split(",")
    dani.sort()
    dani = [int(dan) for dan in dani]
    clear()
    print('''
    --------------------
    
    ID modela aviona: ''', end="")
    model = str(input())
    try:
        model = svi_avioni[int(model)]
    except:
        0
    clear()
    print('''
    --------------------
    
    Cijena: ''', end="")
    try:
        cena = float(input())
    except:
        cena = 0
    clear()
    print('''
    --------------------

    Format: GGGG-MM-DD
    
    Datum pocetka operativnosti: ''', end="")
    datum_pocetka_operativnosti = str(input())
    try:
        datum_pocetka_operativnosti = datetime.strptime(datum_pocetka_operativnosti, "%Y-%m-%d")
    except:
        0
    clear()
    print('''
    --------------------

    Format: GGGG-MM-DD
    
    Datum kraja operativnosti: ''', end="")
    datum_kraja_operativnosti = str(input())
    
    letovi.izmena_letova(svi_letovi, broj_leta, sifra_polazisnog_aerodroma, sifra_odredisnog_aerodroma, vreme_poletanja, vreme_sletanja, False, prevoznik, dani, model, cena, datum_pocetka_operativnosti, datum_kraja_operativnosti)
    letovi.sacuvaj_letove(letovi_fajl, "|", svi_letovi)
    ucitaj_podatke()

    return "menadzer_meni"

def izvjestavanje_meni():
    clear()
    print('''
    --------------------

    [1] Prodate karte za dan prodaje
    [2] Prodate karte za dan polaska
    [3] Prodate karte za dan prodaje i prodavaoca
    [4] Broj i cijena prodatih karata za dan prodaje
    [5] Broj i cijena prodatih karata za dan polaska
    [6] Broj i cijena prodatih karata za dan prodaje i prodavaoca
    [7] Broj i cijena prodatih karata u zadnjih 30 dana

    [8] Nazad

    --------------------
    
    ''', end="")

    unos = None
    while unos not in ["1","2","3","4","5","6","7","8"]:
        unos = str(input())
    if unos == "1": return "prodate_karte_za_dan_prodaje"
    if unos == "2": return "prodate_karte_za_dan_polaska"
    if unos == "3": return "prodate_karte_za_dan_prodaje_i_prodavaoca"
    if unos == "4": return "broj_i_cijena_za_dan_prodaje"
    if unos == "5": return "broj_i_cijena_za_dan_polaska"
    if unos == "6": return "broj_i_cijena_za_dan_prodaje_i_prodavaoca"
    if unos == "7": return "broj_i_cijena_za_30_dana"
    if unos == "8": return "menadzer_meni"

def prodate_karte_za_dan_prodaje():
    global sve_karte

    clear()
    print('''
    --------------------

    Format: GGGG-MM-DD

    Dan prodaje: ''', end="")
    dan = datetime.strptime(str(input()), "%Y-%m-%d")

    dani = izvestaji.izvestaj_prodatih_karata_za_dan_prodaje(sve_karte, dan)
    
    clear()
    print('''
       Broj karte        |  Sifra konkretnog leta  |         Polazak         |         Putnik          

''', end="")

    for karta in dani:
        data1 = str(karta["broj_karte"])
        data2 = str(karta["sifra_konkretnog_leta"])
        data3 = str(svi_konkretni_letovi[karta["sifra_konkretnog_leta"]]["datum_i_vreme_polaska"])
        data4 = str(karta["putnici"][0]["ime"]) + " " + str(karta["putnici"][0]["prezime"])

        for i in [data1, data2, data3, data4]:
            n = 25 - len(i)

            print(" " * floor(n/2.0) + i + " " * ceil(n/2.0), end="")
            if i != data4: print("|", end="")
            if i == data4: print("")
    input()

    return "izvjestavanje_meni"

def prodate_karte_za_dan_polaska():
    global sve_karte, svi_konkretni_letovi

    clear()
    print('''
    --------------------

    Format: GGGG-MM-DD

    Dan polaska: ''', end="")
    dan = datetime.strptime(str(input()), "%Y-%m-%d").date()

    dani = izvestaji.izvestaj_prodatih_karata_za_dan_polaska(sve_karte, svi_konkretni_letovi, dan)
    
    clear()
    print('''
       Broj karte        |  Sifra konkretnog leta  |         Polazak         |         Putnik          

''', end="")

    for karta in dani:
        data1 = str(karta["broj_karte"])
        data2 = str(karta["sifra_konkretnog_leta"])
        data3 = str(svi_konkretni_letovi[karta["sifra_konkretnog_leta"]]["datum_i_vreme_polaska"])
        data4 = str(karta["putnici"][0]["ime"]) + " " + str(karta["putnici"][0]["prezime"])

        for i in [data1, data2, data3, data4]:
            n = 25 - len(i)

            print(" " * floor(n/2.0) + i + " " * ceil(n/2.0), end="")
            if i != data4: print("|", end="")
            if i == data4: print("")
    input()

    return "izvjestavanje_meni"

def prodate_karte_za_dan_prodaje_i_prodavaoca():
    global sve_karte, svi_konkretni_letovi

    clear()
    print('''
    --------------------

    Format: GGGG-MM-DD

    Dan prodaje: ''', end="")
    dan = datetime.strptime(str(input()), "%Y-%m-%d").date()
    clear()
    print('''
    --------------------

    Prodavac: ''', end="")
    prodavac = str(input())

    dani = izvestaji.izvestaj_prodatih_karata_za_dan_prodaje_i_prodavca(sve_karte, dan, prodavac)
    
    clear()
    print('''
       Broj karte        |  Sifra konkretnog leta  |         Polazak         |         Putnik          

''', end="")

    for karta in dani:
        data1 = str(karta["broj_karte"])
        data2 = str(karta["sifra_konkretnog_leta"])
        data3 = str(svi_konkretni_letovi[karta["sifra_konkretnog_leta"]]["datum_i_vreme_polaska"])
        data4 = str(karta["putnici"][0]["ime"]) + " " + str(karta["putnici"][0]["prezime"])

        for i in [data1, data2, data3, data4]:
            n = 25 - len(i)

            print(" " * floor(n/2.0) + i + " " * ceil(n/2.0), end="")
            if i != data4: print("|", end="")
            if i == data4: print("")
    input()

    return "izvjestavanje_meni"

def broj_i_cijena_za_dan_prodaje():
    global sve_karte, svi_konkretni_letovi, svi_letovi

    clear()
    print('''
    --------------------

    Format: GGGG-MM-DD

    Dan prodaje: ''', end="")
    dan = datetime.strptime(str(input()), "%Y-%m-%d").date()

    broj, cijena = izvestaji.izvestaj_ubc_prodatih_karata_za_dan_prodaje(sve_karte, svi_konkretni_letovi, svi_letovi, dan)

    clear()
    print(f'''
--------------------

Broj prodatih karata: {broj}
Ukupna cijena prodatih karata: {cijena}

--------------------''', end="")
    input()

    return "izvjestavanje_meni"

def broj_i_cijena_za_dan_polaska():
    global sve_karte, svi_konkretni_letovi, svi_letovi

    clear()
    print('''
    --------------------

    Format: GGGG-MM-DD

    Dan polaska: ''', end="")
    dan = datetime.strptime(str(input()), "%Y-%m-%d").date()

    broj, cijena = izvestaji.izvestaj_ubc_prodatih_karata_za_dan_polaska(sve_karte, svi_konkretni_letovi, svi_letovi, dan)

    clear()
    print(f'''
--------------------

Broj prodatih karata: {broj}
Ukupna cijena prodatih karata: {cijena}

--------------------''', end="")
    input()

    return "izvjestavanje_meni"

def broj_i_cijena_za_dan_prodaje_i_prodavaoca():
    global sve_karte, svi_konkretni_letovi

    clear()
    print('''
    --------------------

    Format: GGGG-MM-DD

    Dan prodaje: ''', end="")
    dan = datetime.strptime(str(input()), "%Y-%m-%d").date()
    clear()
    print('''
    --------------------

    Prodavac: ''', end="")
    prodavac = str(input())

    dani = izvestaji.izvestaj_ubc_prodatih_karata_za_dan_prodaje_i_prodavca(sve_karte, svi_konkretni_letovi, svi_letovi, dan, prodavac)
    
    clear()
    print('''
       Broj karte        |  Sifra konkretnog leta  |         Polazak         |         Putnik          

''', end="")

    for karta in dani:
        data1 = str(karta["broj_karte"])
        data2 = str(karta["sifra_konkretnog_leta"])
        data3 = str(svi_konkretni_letovi[karta["sifra_konkretnog_leta"]]["datum_i_vreme_polaska"])
        data4 = str(karta["putnici"][0]["ime"]) + " " + str(karta["putnici"][0]["prezime"])

        for i in [data1, data2, data3, data4]:
            n = 25 - len(i)

            print(" " * floor(n/2.0) + i + " " * ceil(n/2.0), end="")
            if i != data4: print("|", end="")
            if i == data4: print("")
    input()

    return "izvjestavanje_meni"

def broj_i_cijena_za_30_dana():
    return "izvjestavanje_meni"

def prijava():
    global svi_korisnici, korisnik

    clear()
    print('''
--------------------

Korisnicko ime: ''', end="")
    korisnicko_ime = str(input())
    clear()
    print('''
--------------------

Lozinka: ''', end="")
    lozinka = str(input())

    try:
        korisnik = korisnici.login(svi_korisnici, korisnicko_ime, lozinka)

        if korisnik["uloga"] == konstante.ULOGA_KORISNIK:
            return "kupac_meni"
        elif korisnik["uloga"] == konstante.ULOGA_PRODAVAC:
            return "prodavac_meni"
        elif korisnik["uloga"] == konstante.ULOGA_ADMIN:
            return "menadzer_meni"
    except:
        print('''
--------------------

Neispravan login.

--------------------''')
        input()
        return "pocetni_meni"

def registracija_kupca():
    global svi_korisnici

    clear()
    print('''
--------------------

Korisnicko ime: ''', end="")
    korisnicko_ime = str(input())
    clear()
    print('''
--------------------

Lozinka: ''', end="")
    lozinka = str(input())
    clear()
    print('''
--------------------

Telefon: ''', end="")
    telefon = str(input())
    clear()
    print('''
--------------------

E-mail: ''', end="")
    email = str(input())
    clear()
    print('''
--------------------

Ime: ''', end="")
    ime = str(input())
    clear()
    print('''
--------------------

Prezime: ''', end="")
    prezime = str(input())
    clear()
    print('''
--------------------

Unesite 0 da preskocite unos ovog podatka.

Pasos: ''', end="")
    pasos = str(input())
    clear()
    print('''
--------------------

Unesite 0 da preskocite unos ovog podatka.

Drzavljanstvo: ''', end="")
    drzavljanstvo = str(input())
    clear()
    print('''
--------------------

Unesite 0 da preskocite unos ovog podatka.
    
Pol: ''', end="")
    pol = str(input())
    uloga = konstante.ULOGA_KORISNIK

    korisnici.kreiraj_korisnika(svi_korisnici, False, uloga, None, korisnicko_ime, lozinka, ime, prezime, email, pasos, drzavljanstvo, telefon, pol)
    korisnici.sacuvaj_korisnike(korisnici_fajl, "|", svi_korisnici)

    return "pocetni_meni"

def ucitaj_podatke():
    global svi_aerodromi, svi_avioni, sve_karte, svi_konkretni_letovi, svi_korisnici, svi_letovi

    svi_aerodromi = aerodromi.ucitaj_aerodrom(aerodromi_fajl, "|")
    svi_avioni = model_aviona.ucitaj_modele_aviona(avioni_fajl, "|")
    sve_karte = karte.ucitaj_karte_iz_fajla(karte_fajl, "|")
    svi_konkretni_letovi = konkretni_letovi.ucitaj_konkretan_let(konkretni_letovi_fajl, "|")
    svi_korisnici = korisnici.ucitaj_korisnike_iz_fajla(korisnici_fajl, "|")
    svi_letovi = letovi.ucitaj_letove_iz_fajla(letovi_fajl, "|")
    karte.sledeci_broj_karte = len(sve_karte) + 1

def main():
    ucitaj_podatke()
    task = "pocetni_meni"
    
    while task != "izlaz":
        if task == "pocetni_meni": task = pocetni_meni()
        if task == "kupac_meni": task = kupac_meni()
        if task == "prodavac_meni": task = prodavac_meni()
        if task == "menadzer_meni": task = menadzer_meni()
        if task == "kupovina_karata_meni": task = kupovina_karata_meni()
        if task == "pregled_nerealizovanih_karata": task = pregled_nerealizovanih_karata()
        if task == "prijava_na_let_kupac": task = prijava_na_let_kupac()
        if task == "prijava_na_let_prodavac": task = prijava_na_let_prodavac()
        if task == "prodaja_karata_meni": task = prodaja_karata_meni()
        if task == "izmjena_karte": task = izmjena_karte()
        if task == "brisanje_karte": task = brisanje_karte()
        if task == "pretraga_prodatih_karata": task = pretraga_prodatih_karata()
        if task == "registrovanje_novih_prodavaca": task = registrovanje_novih_prodavaca()
        if task == "kreiranje_letova": task = kreiranje_letova()
        if task == "izmjena_letova": task = izmjena_letova()
        if task == "izvjestavanje_meni": task = izvjestavanje_meni()
        if task == "prijava": task = prijava()
        if task == "registracija_kupca": task = registracija_kupca()
        if task == "pretraga_konkretnih_letova_iz_menadzer_meni": task = pretraga_konkretnih_letova_iz_menadzer_meni()
        if task == "pretraga_konkretnih_letova_iz_kupovina_karata_meni": task = pretraga_konkretnih_letova_iz_kupovina_karata_meni()
        if task == "pretraga_konkretnih_letova_iz_prodaja_karata_meni": task = pretraga_konkretnih_letova_iz_prodaja_karata_meni()
        if task == "pretraga_letova": task = pretraga_letova()
        if task == "kupi_kartu_za_sebe": task = kupi_kartu_za_sebe()
        if task == "kupi_kartu_za_drugu_osobu": task = kupi_kartu_za_drugu_osobu()
        if task == "nastavi_kupovinu_karata": task = nastavi_kupovinu_karata()
        if task == "kupi_kartu_za_povezani_let": task = kupi_kartu_za_povezani_let()
        if task == "kupi_kartu_za_saputnika": task = kupi_kartu_za_saputnika()
        if task == "kupi_kartu": task = kupi_kartu()
        if task == "pregled_nerealizovanih_letova": task = pregled_nerealizovanih_letova()
        if task == "prodaj_kartu": task = prodaj_kartu()
        if task == "prodaj_kartu_registrovanom": task = prodaj_kartu_registrovanom()
        if task == "prodaj_kartu_neregistrovanom": task = prodaj_kartu_neregistrovanom()
        if task == "nastavi_prodaju_karata": task = nastavi_prodaju_karata()
        if task == "prodaj_kartu_za_povezani_let": task = prodaj_kartu_za_povezani_let()
        if task == "prodaj_kartu_za_saputnika": task = prodaj_kartu_za_saputnika()
        if task == "prodate_karte_za_dan_prodaje": task = prodate_karte_za_dan_prodaje()
        if task == "prodate_karte_za_dan_polaska": task = prodate_karte_za_dan_polaska()
        if task == "prodate_karte_za_dan_prodaje_i_prodavaoca": task = prodate_karte_za_dan_prodaje_i_prodavaoca()
        if task == "broj_i_cijena_za_dan_prodaje": task = broj_i_cijena_za_dan_prodaje()
        if task == "broj_i_cijena_za_dan_polaska": task = broj_i_cijena_za_dan_polaska()
        if task == "broj_i_cijena_za_dan_prodaje_i_prodavaoca": task = broj_i_cijena_za_dan_prodaje_i_prodavaoca()
        if task == "broj_i_cijena_za_30_dana": task = broj_i_cijena_za_30_dana()

    clear()
    print("Dovidjenja")
    exit()

main()
