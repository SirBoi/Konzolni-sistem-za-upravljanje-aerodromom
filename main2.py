from sys import exit
from os import system
from datetime import datetime, timedelta



from common import konstante
from korisnici import korisnici
from izvestaji import izvestaji
from karte import karte
from konkretni_letovi import konkretni_letovi
from letovi import letovi
from model_aviona import model_aviona
from aerodromi import aerodromi

aerodromi_fajl = "C:\\Users\\Administrator\\Desktop\\fajl_za_rad\\projekat-2022-main\\fajlovi\\aerodromi.csv"
avioni_fajl = "C:\\Users\\Administrator\\Desktop\\fajl_za_rad\\projekat-2022-main\\fajlovi\\avioni.csv"
karte_fajl = "C:\\Users\\Administrator\\Desktop\\fajl_za_rad\\projekat-2022-main\\fajlovi\\karte.csv"
konkretni_letovi_fajl = "C:\\Users\\Administrator\\Desktop\\fajl_za_rad\\projekat-2022-main\\fajlovi\\konkretni_letovi.csv"
korisnici_fajl = "C:\\Users\\Administrator\\Desktop\\fajl_za_rad\\projekat-2022-main\\fajlovi\\korisnici.csv"
letovi_fajl = "C:\\Users\\Administrator\\Desktop\\fajl_za_rad\\projekat-2022-main\\fajlovi\\letovi.csv"

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

    [3] Izlaz

    --------------------
    
    ''', end="")
    
    unos = None
    while unos not in ["1","2","3"]:
        unos = str(input())
    
    if unos == "1":
        prijava()
    elif unos == "2":
        registracija_kupca()
    elif unos == "3":
        izlaz()

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

    if unos == "1":
        kupovina_karata()
    elif unos == "2":
        pregled_nerealizovanih_karata()
    elif unos == "3":
        prijava_na_let()
    elif unos == "4":
        pocetni_meni()

def prodavac_meni():
    clear()
    print('''
    --------------------

    [1] Prodaja karata
    [2] Prijava na let
    [3] Izmjena karte
    [4] Brisanje karte
    [5] Prodaja prodatih karata

    [6] Izloguj se

    --------------------
    
    ''', end="")

    unos = None
    while unos not in ["1","2","3","4","5","6"]:
        unos = str(input())

    if unos == "6":
        pocetni_meni()

def menadzer_meni():
    clear()
    print('''
    --------------------

    [1] Pretraga prodatih karata
    [2] Registrovanje novih prodavaca
    [3] Kreiranje letova
    [4] Izmjena letova
    [5] Brisanje karata
    [6] Izvjestavanje

    [7] Izloguj se

    --------------------
    
    ''', end="")

    unos = None
    while unos not in ["1","2","3","4","5","6","7"]:
        unos = str(input())

    if unos == "7":
        pocetni_meni()

def kupovina_karata():
    print("kupovina_karata")

def pregled_nerealizovanih_karata():
    print("pregled_nerealizovanih_karata")

def prijava_na_let():
    print("prijava_na_let")

def prodaja_karata():
    print("prodaja_karata")

def prijava_na_let():
    print("prijava_na_let")

def izmjena_karte():
    print("izmjena_karte")

def brisanje_karte():
    print("brisanje_karte")

def pretraga_prodatih_karata():
    print("pretraga_prodatih_karata")

def registrovanje_novih_prodavaca():
    print("registrovanje_novih_prodavaca")

def kreiranje_letova():
    print("kreiranje_letova")

def izmjena_letova():
    print("izmjena_letova")

def brisanje_karata():
    print("brisanje_karata")

def izvjestavanje():
    print("izvjestavanje")

def prijava():
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

    try:
        korisnik = korisnici.login(svi_korisnici, korisnicko_ime, lozinka)
        clear()
        kupac_meni()
    except:
        pocetni_meni()
        # Ovdje je greska

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
    korisnici.sacuvaj_korisnike("C:\\Users\\Administrator\\Desktop\\fajl_za_rad\\projekat-2022-main\\fajlovi\\korisnici.csv", "|", svi_korisnici)

def izlaz():
    clear()
    print("Dovidjenja")
    exit()

def ucitaj_podatke():
    global svi_korisnici

    svi_korisnici = korisnici.ucitaj_korisnike_iz_fajla(korisnici_fajl, "|")

def main():
    ucitaj_podatke()
    pocetni_meni()

main()
print("Greska! Ne treba biti moguce doci ovdje")
exit()

    # prijava
    # izlaz
    # registracija


    # svi
    # pregled nerealizovanih letova
    # pretraga letova
    # . Prikaz 10 najjeftinijih (po opadajućoj ceni) letova između zadatog polazišta i odredišta.
    # fleksibilni polasci
    # odjava

    # kupac
    # kupivana karata
    # pregled nerealizovanoh karata
    # prijava na let

    # prodavac
    # prodaja karata
    # prijava na let
    # izmjena karte
    # brisanje karete
    # pretraga prodatih karata

    # menadzer
    # pretraga prodatih karata
    # registrovanje novih prodavaca
    # kreiranje letova
    # izmjena letova
    # brisanje karata
    # izvjestavanje


    # pregled nerealizovanih letova
    # pretraga letova
    # visekriterijumska pretraga letova
    # prikaz 10 najjeftinijih letova
    # fleksibilni polasci
    # odjava
    # kupovina karata
    # pregled nerealizovanih karata
    # prijava na let
    # prodaja karata
    # prijava na let (prodavac)
    # izmjena karte
    # brisanje karte
    # pretraga prodatih karata
    # pretraga prodatih karata (menadzer)
    # registracija novih prodavaca
    # kreirabnje letova
    # izmena letova
    # brisanje karata
    # izvestavanje