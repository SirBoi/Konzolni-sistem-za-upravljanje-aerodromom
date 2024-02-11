from datetime import datetime, date
"""
Funkcija kao rezultat vraća listu karata prodatih na zadati dan.
"""
def izvestaj_prodatih_karata_za_dan_prodaje(sve_karte: dict, dan: date) -> list:
    
    list_ = []

    for karta in sve_karte:
        if datetime.strptime(sve_karte[karta]["datum_prodaje"][:10], "%Y-%m-%d").date() == dan.date():
            list_.append(sve_karte[karta])
    
    return list_


"""
Funkcija kao rezultat vraća listu svih karata čiji je dan polaska leta na zadati dan.
"""
def izvestaj_prodatih_karata_za_dan_polaska(sve_karte: dict, svi_konkretni_letovi: dict, dan: date) -> list:
    
    list_ = []

    for karta in sve_karte:
        for let in svi_konkretni_letovi:
            if svi_konkretni_letovi[let]["sifra"] == sve_karte[karta]["sifra_konkretnog_leta"] and svi_konkretni_letovi[let]["datum_i_vreme_polaska"].date() == dan:
                list_.append(sve_karte[karta])
                break

    return list_


"""
Funkcija kao rezultat vraća listu karata koje je na zadati dan prodao zadati prodavac.
"""
def izvestaj_prodatih_karata_za_dan_prodaje_i_prodavca(sve_karte: dict, dan: date, prodavac: str) -> list:
    
    list_ = []

    for karta in sve_karte:
        if datetime.strptime(sve_karte[karta]["datum_prodaje"][:10], "%Y-%m-%d").date() == dan and sve_karte[karta]["prodavac"] == prodavac:
            list_.append(sve_karte[karta])
    
    return list_


"""
Funkcija kao rezultat vraća dve vrednosti: broj karata prodatih na zadati dan i njihovu ukupnu cenu.
Rezultat se vraća kao torka. Npr. return broj, suma
"""
def izvestaj_ubc_prodatih_karata_za_dan_prodaje(
    sve_karte: dict,
    svi_konkretni_letovi: dict,
    svi_letovi,
    dan: date
) -> tuple:
    
    num = 0
    cijena = 0

    for karta in sve_karte:
        if datetime.strptime(sve_karte[karta]["datum_prodaje"][:10], "%Y-%m-%d").date() == dan:
            num += 1
            cijena += svi_letovi[svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["broj_leta"]]["cena"]
    
    return (num, cijena)


"""
Funkcija kao rezultat vraća dve vrednosti: broj karata čiji je dan polaska leta na zadati dan i njihovu ukupnu cenu.
Rezultat se vraća kao torka. Npr. return broj, suma
"""
def izvestaj_ubc_prodatih_karata_za_dan_polaska(
    sve_karte: dict,
    svi_konkretni_letovi: dict,
    svi_letovi: dict,
    dan: date
) -> tuple:
    
    num = 0
    cijena = 0

    for karta in sve_karte:
        if svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["datum_i_vreme_polaska"].date() == dan:
            num += 1
            cijena += svi_letovi[svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["broj_leta"]]["cena"]
    
    return (num, cijena)


"""
Funkcija kao rezultat vraća dve vrednosti: broj karata koje je zadati prodavac prodao na zadati dan i njihovu 
ukupnu cenu. Rezultat se vraća kao torka. Npr. return broj, suma
"""
def izvestaj_ubc_prodatih_karata_za_dan_prodaje_i_prodavca(
    sve_karte: dict,
    konkretni_letovi: dict,
    svi_letovi: dict,
    dan: date,
    prodavac: str
) -> tuple:
    
    num = 0
    cijena = 0

    for karta in sve_karte:
        if sve_karte[karta]["datum_prodaje"].date() == dan and sve_karte[karta]["prodavac"] == prodavac:
            num += 1
            cijena += svi_letovi[konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["broj_leta"]]["cena"]
    
    return (num, cijena)


"""
Funkcija kao rezultat vraća rečnik koji za ključ ima dan prodaje, a za vrednost broj karata prodatih na taj dan.
Npr: {"2023-01-01": 20}
"""
def izvestaj_ubc_prodatih_karata_30_dana_po_prodavcima(
    sve_karte: dict,
    svi_konkretni_letovi: dict,
    svi_letovi: dict
) -> dict: #ubc znaci ukupan broj i cena
    
    dict_ = {}

    for karta in sve_karte:
        try:
            dict_[sve_karte[karta]["datum_prodaje"]] += 1
        except:
            dict_[sve_karte[karta]["datum_prodaje"]] = 1
    
    return dict_

    # Sta tacno ova funkcija treba da radi? Njeno ime trazi jedno, njen opis nesto drugo, a test nesto trece?
    # U testu se ne spominje 30 dana ni na jednom mjestu.
    # Takodjer se ne spominje sta se tacno treba vratiti kao rezultat ove funkcije.
    # Potrebno je vratiti neki dict, ali nije receno koji su kljucevi tog dict-a niti sta su vrijednosti.
    # Gledajuci test, cini mi se da je vrijednost neka lista, ali ne znam kolika niti sta treba da sadrzi.
    # Misli da je lista jer se elem indeksira sa integerima, mada moze biti i dict sa integerima za kljuceve, sto bas i nema smisla u ovom primjeru.
    # Spominju se indeksi 1 i 2, ali nigdje 0? Sta je onda prvi clan te liste?

    # Redovi 459 i 460 su takodjer zbunjujuci. Zasto se prvo generise nasumican string duzine 5 znakova, a onda se brise zadnjih 4?
    # To ne pravi probleme, ali je bespotrebno zbunjujuce.

    # Da li red 469 mijenja podatke zadate u redu 465?
