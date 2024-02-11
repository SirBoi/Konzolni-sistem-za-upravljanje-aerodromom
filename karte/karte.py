from common import konstante
from functools import reduce
from datetime import datetime
import csv

"""
Brojačka promenljiva koja se automatski povećava pri kreiranju nove karte.
"""
sledeci_broj_karte = 1

"""
Kupovina karte proverava da li prosleđeni konkretni let postoji i da li ima slobodnih mesta. U tom slučaju se karta 
dodaje  u kolekciju svih karata. Slobodna mesta se prosleđuju posebno iako su deo konkretnog leta, zbog lakšeg 
testiranja. Baca grešku ako podaci nisu validni.
kwargs moze da prihvati prodavca kao recnik, i datum_prodaje kao datetime
recnik prodavac moze imati id i ulogu
CHECKPOINT 2: kupuje se samo za ulogovanog korisnika i bez povezanih letova.
ODBRANA: moguće je dodati saputnike i odabrati povezane letove. 
"""
def kupovina_karte(
    sve_karte: dict,
    svi_konkretni_letovi: dict,
    sifra_konkretnog_leta: int,
    putnici: list,
    slobodna_mesta: list,
    kupac: dict,
    **kwargs
) -> (dict, dict):
    
    global sledeci_broj_karte

    # Provjera postojanja leta
    if sifra_konkretnog_leta not in svi_konkretni_letovi:
        raise Exception("Provera za nepostojeći let")
    
    # Provjera slobodnih mjesta
    try:
        broj_slobodnih_mjesta = 0

        for red in slobodna_mesta:
            for sjediste in red:
                if sjediste == True:
                    broj_slobodnih_mjesta += 1
        
        if broj_slobodnih_mjesta == 0:
            raise Exception("Nema mesta")
    except:
        raise Exception("Nema mesta")

    if "prodavac" in kwargs:
        if kwargs["prodavac"]["uloga"] != konstante.ULOGA_PRODAVAC:
            raise Exception("Prodavac mora da proda kartu")

    # Sve provjere su prosle, karta se dodaje u kolekciju svih karata
    karta = {
        "broj_karte": sledeci_broj_karte,
        "putnici": putnici,
        "sifra_konkretnog_leta": sifra_konkretnog_leta,
        "status": konstante.STATUS_NEREALIZOVANA_KARTA, 
        "kupac": kupac,
        "prodavac": kwargs["prodavac"] if "prodavac" in kwargs else None,
        "datum_prodaje": kwargs["datum_prodaje"] if "datum_prodaje" in kwargs else None,
        "obrisana": False
    }

    sve_karte[sledeci_broj_karte] = karta

    return (karta, sve_karte)


def pregled_nerealizovanaih_karata(korisnik: dict, sve_karte: iter):
    
    list_ = []

    for karta in sve_karte:
        if korisnik in karta["putnici"] and karta["status"] == konstante.STATUS_NEREALIZOVANA_KARTA:
            list_.append(karta)
    
    return list_


"""
Funkcija menja sve vrednosti karte novim vrednostima. Kao rezultat vraća rečnik sa svim kartama, 
koji sada sadrži izmenu.
"""
def izmena_karte(
    sve_karte: iter,
    svi_konkretni_letovi: iter,
    broj_karte: int,
    nova_sifra_konkretnog_leta: int=None,
    nov_datum_polaska:
    datetime=None,
    sediste=None
) -> dict:

    if broj_karte in sve_karte:
        if nova_sifra_konkretnog_leta != None:
            sve_karte[broj_karte]["sifra_konkretnog_leta"] = nova_sifra_konkretnog_leta
        if nov_datum_polaska != None:
            for let in svi_konkretni_letovi:
                if svi_konkretni_letovi[let]["broj_leta"] == sve_karte[broj_karte]["sifra_konkretnog_leta"] and svi_konkretni_letovi[let]["datum_i_vreme_polaska"] == nov_datum_polaska:
                    sve_karte[broj_karte]["sifra_konkretnog_leta"] = svi_konkretni_letovi[let]["sifra"]
        if sediste != None:
            sve_karte[broj_karte]["sifra_sedista"] = sediste
    else:
        raise Exception("Trazena karta ne postoji.")

    return sve_karte


"""
 Funkcija brisanja karte se ponaša drugačije u zavisnosti od korisnika:
- Prodavac: karta se označava za brisanje
- Admin/menadžer: karta se trajno briše
Kao rezultat se vraća nova kolekcija svih karata.
"""
def brisanje_karte(korisnik: dict, sve_karte: dict, broj_karte: int) -> dict:
    
    karta_obrisana = False

    for karta in sve_karte:
        if sve_karte[karta]["broj_karte"] == broj_karte:
            if korisnik["uloga"] == konstante.ULOGA_KORISNIK:
                raise Exception("Običan korisnik ne može da obriše kartu")
            
            elif korisnik["uloga"] == konstante.ULOGA_PRODAVAC:
                sve_karte[karta]["obrisana"] = True
                karta_obrisana = True
                break
            
            elif korisnik["uloga"] == konstante.ULOGA_ADMIN:
                del sve_karte[broj_karte]
                karta_obrisana = True
                break

    if karta_obrisana == False:
        raise Exception("Brisanje nepostojeće karte")
    return sve_karte


"""
Funkcija vraća sve karte koje se poklapaju sa svim zadatim kriterijumima. 
Kriterijum se ne primenjuje ako nije prosleđen.
"""
def pretraga_prodatih_karata(sve_karte: dict, svi_letovi:dict, svi_konkretni_letovi:dict, polaziste: str="",
                             odrediste: str="", datum_polaska: datetime="", datum_dolaska: str="",
                             korisnicko_ime_putnika: str="")->list:
    
    karte = []

    for karta in sve_karte:
        if polaziste != "":
            if svi_letovi[svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["broj_leta"]]["sifra_polazisnog_aerodroma"] != polaziste:
                continue
        if odrediste != "":
            if svi_letovi[svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["broj_leta"]]["sifra_odredisnog_aerodroma"] != odrediste:
                continue
        if datum_polaska != "":
            if svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["datum_i_vreme_polaska"] != datum_polaska:
                continue
        if datum_dolaska != "":
            if svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["datum_i_vreme_dolaska"] != datum_dolaska:
                continue
        if korisnicko_ime_putnika != "":
            check = False

            for putnik in sve_karte[karta]["putnici"]:
                if putnik["id"] == korisnicko_ime_putnika:
                    check = True

            if not check:
                continue
        
        karte.append(sve_karte[karta])

    return karte


"""
Funkcija čuva sve karte u fajl na zadatoj putanji sa zadatim separatorom.
"""
def sacuvaj_karte(sve_karte: dict, putanja: str, separator: str):
    
    with open(putanja, "w") as f:
        for karta in sve_karte:
            list_ = []

            for key in sve_karte[karta]:
                if (type(sve_karte[karta][key]) == bool):
                    if (sve_karte[karta][key]):
                        list_.append("1")
                    else:
                        list_.append("0")

                else:
                    list_.append(str(sve_karte[karta][key]))

            line = separator.join(list_)

            f.writelines(line + '\n')


"""
Funkcija učitava sve karte iz fajla sa zadate putanje sa zadatim separatorom.
"""
def ucitaj_karte_iz_fajla(putanja: str, separator: str) -> dict:

    dictionary_ = {}

    with open(putanja, "r") as f:
        for line in f.readlines():
            line = line[:-1]

            list_ = line.split(separator)

            # Kreiranje dict-a za kupca
            string_ = list_[4][1:-1]
            string_ = string_.split("'")

            kupac = {}
            
            for i in range(len(string_) // 4):
                kupac[string_[i*4 + 1]] = string_[i*4 + 3]

            # Kreiranje dict-a za prodavca
            string_ = list_[5][1:-1]
            string_ = string_.split("'")

            prodavac = {}
            
            for i in range(len(string_) // 4):
                prodavac[string_[i*4 + 1]] = string_[i*4 + 3]

            # Kreiranje liste za putnike
            putnici = []
            lista = list_[1][2:-1]
            lista = lista.split("{")

            for elem1 in lista:
                putnik = elem1.split("'")

                dict_ = {}

                for elem2 in range(len(putnik) // 4):
                    dict_[putnik[elem2 * 4 + 1]] = putnik[elem2 * 4 + 3]

                putnici.append(dict_)

            # Kreiranje konacnog dict-a
            dictionary_[int(list_[0])] = {
                "broj_karte": int(list_[0]),
                "putnici": putnici,
                "sifra_konkretnog_leta": int(list_[2]),
                "status": list_[3],
                "kupac": kupac,
                "prodavac": prodavac,
                "datum_prodaje": list_[6],
                "obrisana": bool(int(list_[7])),
            }
    
    return dictionary_
