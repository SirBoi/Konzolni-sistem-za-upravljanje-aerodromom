from datetime import datetime, date, timedelta


def provjera_validnosti_podataka(svi_letovi: dict, broj_leta: str, sifra_polazisnog_aerodroma: str, sifra_odredisnog_aerodorma: str,
    vreme_poletanja: str, vreme_sletanja: str, sletanje_sutra: bool, prevoznik: str, dani: list, model: dict, cena: float,
    datum_pocetka_operativnosti: datetime, datum_kraja_operativnosti: datetime):

    # Provjera za unos praznog stringa ili nule
    for key in [broj_leta, sifra_polazisnog_aerodroma, sifra_odredisnog_aerodorma, vreme_poletanja, vreme_sletanja, datum_pocetka_operativnosti, datum_kraja_operativnosti, sletanje_sutra, prevoznik, dani]:
        if key == "":
            return "prazan unos"
    for key in [model, cena]:
        if key == 0:
            return "prazan unos"
    
    # Provjera za broj leta
    try:
        if not (len(broj_leta) == 4 and broj_leta[0:2].isalpha() and broj_leta[2:4].isdigit()):
            return "broj leta"
    except:
        return "broj leta"

    # Provjera za sifru polazisnog aerodroma i sifru odredisnog aerodroma
    try:
        if sifra_polazisnog_aerodroma == "polaziste":
            return "polaziste"
        if sifra_odredisnog_aerodorma == "odrediste":
            return "odrediste"
        if sifra_odredisnog_aerodorma == sifra_polazisnog_aerodroma:
            return "polaziste i odrediste"
    except:
        return "polaziste i odrediste"

    # Provjera za vrijeme polaska
    try:
        if not (len(vreme_poletanja) == 5 and type(vreme_poletanja) == str and vreme_poletanja[2] == ':'
        and vreme_poletanja[0:2].isdigit() and int(vreme_poletanja[0:2]) >= 0 and int(vreme_poletanja[0:2]) <= 24
        and vreme_poletanja[3:5].isdigit() and int(vreme_poletanja[3:5]) >= 0 and int(vreme_poletanja[3:5]) <= 60):
            return "vreme polaska"
    except:
        return "vreme polaska"

    # Provjera za vrijeme dolaska
    try:
        if not (len(vreme_sletanja) == 5 and type(vreme_sletanja) == str and vreme_sletanja[2] == ':'
        and vreme_sletanja[0:2].isdigit() and int(vreme_sletanja[0:2]) >= 0 and int(vreme_sletanja[0:2]) <= 24
        and vreme_sletanja[3:5].isdigit() and int(vreme_sletanja[3:5]) >= 0 and int(vreme_sletanja[3:5]) <= 60):
            return "vreme dolaska"
    except:
        return "vreme dolaska"
    
    # Provjera za sletanje sutra
    try:
        if not (type(sletanje_sutra) == bool):
            return "sletanje sutra"
    except:
        return "sletanje sutra"

    # Provjera za dane
    try:
        if not (len(dani) >= 1 and len(dani) <= 7 and type(dani) == list):
            return "losi dani"
        else:
            for dan in dani:
                if not (type(dan) == int and dan >= 0 and dan <= 6):
                    return "losi dani"
    except:
        return "losi dani"

    # Provjera za cijenu
    try:
        if type(cena) != float:
            return "cena"
    except:
        return "cena"

    # Provjera za model
    try:
        if not (type(model) == dict and len(model) == 4):
            return "model"
    except:
        return "model"
    
    # Provjera za datume operativnosti
    try:
        if not (type(datum_pocetka_operativnosti) == datetime and type(datum_kraja_operativnosti) == datetime):
            return "datumi operativnosti"
        elif (datum_pocetka_operativnosti > datum_kraja_operativnosti):
            return "pocetak posle kraja"
    except:
        return "datumi operativnosti"

    return "nema greske"


"""
Funkcija koja omogucuje korisniku da pregleda informacije o letovima
Ova funkcija sluzi samo za prikaz
"""
def pregled_nerealizoivanih_letova(svi_letovi: dict):
    
    ocekivani_letovi = []

    for let in svi_letovi:
        if svi_letovi[let]["datum_pocetka_operativnosti"] > datetime.now():
            ocekivani_letovi.append(svi_letovi[let])

    return ocekivani_letovi


"""
Funkcija koja omogucava pretragu leta po yadatim kriterijumima. Korisnik moze da zada jedan ili vise kriterijuma.
Povratna vrednost je lista konkretnih letova.
vreme_poletanja i vreme_sletanja su u formatu hh:mm
"""
def pretraga_letova(svi_letovi: dict, konkretni_letovi:dict, polaziste: str = "", odrediste: str = "",
                    datum_polaska: datetime = None, datum_dolaska: datetime = None,
                    vreme_poletanja: str = "", vreme_sletanja: str = "", prevoznik: str = "") -> list:
    
    # Provjera za prazan unos
    if svi_letovi == None:
        raise Exception("Nije vraćena kolekcija letova")
    
    lista_konkretnih_letova = []

    konkretan_let_keys = [polaziste, odrediste, vreme_poletanja, vreme_sletanja, prevoznik]
    svi_letovi_keys = ["sifra_polazisnog_aerodroma","sifra_odredisnog_aerodorma","vreme_poletanja","vreme_sletanja","prevoznik"]
    
    if datum_polaska != None:
        for let in konkretni_letovi:
            if konkretni_letovi[let]["datum_i_vreme_polaska"] == datum_polaska:
                lista_konkretnih_letova.append(konkretni_letovi[let])

    elif datum_dolaska != None:
        for let in konkretni_letovi:
            if konkretni_letovi[let]["datum_i_vreme_dolaska"] == datum_dolaska:
                lista_konkretnih_letova.append(konkretni_letovi[let])

    else:
        for let in svi_letovi:
            match = True

            for key1,key2 in zip(konkretan_let_keys,svi_letovi_keys):
                if key1 != "":
                    if svi_letovi[let][key2] != key1:
                        match = False
                        break
            
            if match:
                konkretan_let = {
                    "sifra": konkretni_letovi[1234]["sifra"],
                    "broj_leta": svi_letovi[let]["broj_leta"],
                    "datum_i_vreme_polaska": konkretni_letovi[1234]["datum_i_vreme_polaska"],
                    "datum_i_vreme_dolaska": konkretni_letovi[1234]["datum_i_vreme_dolaska"]
                }

                lista_konkretnih_letova.append(konkretan_let)
    
    if len(lista_konkretnih_letova) > 0:
        return lista_konkretnih_letova
    else:
        raise Exception("Neuspesno trazenje leta")



"""
Funkcija koja kreira novi rečnik koji predstavlja let sa prosleđenim vrednostima. Kao rezultat vraća kolekciju
svih letova proširenu novim letom. 
Ova funkcija proverava i validnost podataka o letu. Paziti da kada se kreira let, da se kreiraju i njegovi konkretni letovi.
vreme_poletanja i vreme_sletanja su u formatu hh:mm
CHECKPOINT2: Baca grešku sa porukom ako podaci nisu validni.
"""
def kreiranje_letova(svi_letovi : dict, broj_leta: str, sifra_polazisnog_aerodroma: str,
                     sifra_odredisnog_aerodorma: str,
                     vreme_poletanja: str, vreme_sletanja: str, sletanje_sutra: bool, prevoznik: str,
                     dani: list, model: dict, cena: float,  datum_pocetka_operativnosti: datetime = None ,
                    datum_kraja_operativnosti: datetime = None):
    
    greska = provjera_validnosti_podataka(svi_letovi, broj_leta, sifra_polazisnog_aerodroma, sifra_odredisnog_aerodorma, vreme_poletanja, vreme_sletanja,
        sletanje_sutra, prevoznik, dani, model, cena, datum_pocetka_operativnosti, datum_kraja_operativnosti)
    
    if greska != "nema greske":
        raise Exception(f"Provera za nevalidnu vrednost: {greska}")

    # Prosle su sve provjere, vraca se ispravan dict
    svi_letovi[broj_leta] = {
            "broj_leta": broj_leta,
            "sifra_polazisnog_aerodroma": sifra_polazisnog_aerodroma,
            "sifra_odredisnog_aerodorma": sifra_odredisnog_aerodorma,
            "vreme_poletanja": vreme_poletanja,
            "vreme_sletanja": vreme_sletanja,
            "datum_pocetka_operativnosti": datum_pocetka_operativnosti,
            "datum_kraja_operativnosti": datum_kraja_operativnosti,
            "sletanje_sutra": sletanje_sutra,
            "prevoznik": prevoznik,
            "dani": dani,
            "model": model,
            "cena": cena}

    return svi_letovi


"""
Funkcija koja menja let sa prosleđenim vrednostima. Kao rezultat vraća kolekciju
svih letova sa promenjenim letom. 
Ova funkcija proverava i validnost podataka o letu.
vreme_poletanja i vreme_sletanja su u formatu hh:mm
CHECKPOINT2: Baca grešku sa porukom ako podaci nisu validni.
"""
def izmena_letova(
    svi_letovi : dict,
    broj_leta: str,
    sifra_polazisnog_aerodroma: str,
    sifra_odredisnog_aerodorma: str,
    vreme_poletanja: str,
    vreme_sletanja: str,
    sletanje_sutra: bool,
    prevoznik: str,
    dani: list,
    model: dict,
    cena: float,
    datum_pocetka_operativnosti: datetime,
    datum_kraja_operativnosti: datetime
) -> dict:
    
    greska = provjera_validnosti_podataka(svi_letovi, broj_leta, sifra_polazisnog_aerodroma, sifra_odredisnog_aerodorma, vreme_poletanja, vreme_sletanja,
        sletanje_sutra, prevoznik, dani, model, cena, datum_pocetka_operativnosti, datum_kraja_operativnosti)
    
    if greska != "nema greske":
        raise Exception(f"Provera za nevalidnu vrednost: {greska}")

    let_postoji = False

    for let in svi_letovi:
        if svi_letovi[let]["broj_leta"] == broj_leta:
            let_postoji = True

            svi_letovi[let]["sifra_polazisnog_aerodroma"] = sifra_polazisnog_aerodroma
            svi_letovi[let]["sifra_odredisnog_aerodorma"] = sifra_odredisnog_aerodorma
            svi_letovi[let]["vreme_poletanja"] = vreme_poletanja
            svi_letovi[let]["vreme_sletanja"] = vreme_sletanja
            svi_letovi[let]["datum_pocetka_operativnosti"] = datum_pocetka_operativnosti
            svi_letovi[let]["datum_kraja_operativnosti"] = datum_kraja_operativnosti
            svi_letovi[let]["sletanje_sutra"] = sletanje_sutra
            svi_letovi[let]["prevoznik"] = prevoznik
            svi_letovi[let]["dani"] = dani
            svi_letovi[let]["model"] = model
            svi_letovi[let]["cena"] = cena
    
    if let_postoji:
        return svi_letovi
    else:
        raise Exception("Provera za nevalidnu vrednost: nepostojeci let")


"""
Funkcija koja cuva sve letove na zadatoj putanji
"""
def sacuvaj_letove(putanja: str, separator: str, svi_letovi: dict):
    
    with open(putanja, "w") as f:
        for korisnik in svi_letovi:
            list_ = []

            for key in svi_letovi[korisnik]:
                if (type(svi_letovi[korisnik][key]) == datetime):
                    list_.append(svi_letovi[korisnik][key].strftime("%Y %m %d"))

                elif (type(svi_letovi[korisnik][key]) == bool):
                    if (svi_letovi[korisnik][key]):
                        list_.append("1")
                    else:
                        list_.append("0")

                elif (type(svi_letovi[korisnik][key]) == list):
                    str_ = ""
                    for element in svi_letovi[korisnik][key]:
                        str_ += str(element)
                    
                    list_.append(str_)

                elif (type(svi_letovi[korisnik][key]) == dict):
                    list_.append(str(svi_letovi[korisnik][key]["id"]))
                    list_.append(str(svi_letovi[korisnik][key]["naziv"]))
                    list_.append(str(svi_letovi[korisnik][key]["broj_redova"]))
                    
                    str_ = ""
                    for element in svi_letovi[korisnik][key]["pozicije_sedista"]:
                        str_ += str(element)
                    
                    list_.append(str_)

                else:
                    list_.append(str(svi_letovi[korisnik][key]))

            line = separator.join(list_)

            f.writelines(line + '\n')


"""
Funkcija koja učitava sve letove iz fajla i vraća ih u rečniku.
"""
def ucitaj_letove_iz_fajla(putanja: str, separator: str) -> dict:
    
    dictionary = {}

    with open(putanja, "r") as f:
        for line in f.readlines():
            line = line[:-1]

            list_ = line.split(separator)
            
            dict_ = {
                "id": int(list_[10]),
                "naziv": list_[11],
                "broj_redova": int(list_[12]),
                "pozicije_sedista": [sjediste for sjediste in list_[13]]
            }

            dictionary[list_[0]] = {
                "broj_leta": list_[0],
                "sifra_polazisnog_aerodroma": list_[1],
                "sifra_odredisnog_aerodorma": list_[2],
                "vreme_poletanja": list_[3],
                "vreme_sletanja": list_[4],
                "datum_pocetka_operativnosti": datetime.strptime(list_[5], "%Y %m %d"),
                "datum_kraja_operativnosti": datetime.strptime(list_[6], "%Y %m %d"),
                "sletanje_sutra": bool(int(list_[7])),
                "prevoznik": list_[8],
                "dani": [int(dan) for dan in list_[9]],
                "model": dict_,
                "cena": float(list_[14])
            }
    
    return dictionary


"""
Pomoćna funkcija koja podešava matricu zauzetosti leta tako da sva mesta budu slobodna.
Prolazi kroz sve redove i sve poziciej sedišta i postavlja ih na "nezauzeto".
"""
def podesi_matricu_zauzetosti(svi_letovi: dict, konkretni_let: dict):
    broj_redova = svi_letovi[konkretni_let["broj_leta"]]["model"]["broj_redova"]
    pozicije_sjedista = svi_letovi[konkretni_let["broj_leta"]]["model"]["pozicije_sedista"]

    matrica = [[lett for lett in pozicije_sjedista] for num in range(broj_redova)]

    konkretni_let["zauzetost"] = matrica


"""
Funkcija koja vraća matricu zauzetosti sedišta. Svaka stavka sadrži oznaku pozicije i oznaku reda.
Primer: [[True, False], [False, True]] -> A1 i B2 su zauzeti, A2 i B1 su slobodni
"""
def matrica_zauzetosti(konkretni_let: dict) -> list:
    
    og_matrica, matrica = konkretni_let["zauzetost"], konkretni_let["zauzetost"]
    
    for red in range(len(og_matrica)):
        for sjediste in range(len(og_matrica[red])):
            if (og_matrica[red][sjediste] == 'X'):
                matrica[red][sjediste] = True
            else:
                matrica[red][sjediste] = False

    return matrica


"""
Funkcija koja zauzima sedište na datoj poziciji u redu, najkasnije 48h pre poletanja. Redovi počinju od 1. 
Vraća grešku ako se sedište ne može zauzeti iz bilo kog razloga.
"""
def checkin(karta, svi_letovi: dict, konkretni_let: dict, red: int, pozicija: str) -> (dict, dict):
    pass


"""
Funkcija koja vraća listu konkretni letova koji zadovoljavaju sledeće uslove:
1. Polazište im je jednako odredištu prosleđenog konkretnog leta
2. Vreme i mesto poletanja im je najviše 120 minuta nakon sletanja konkretnog leta
"""
def povezani_letovi(svi_letovi: dict, svi_konkretni_letovi: dict, konkretni_let: dict) -> list:

    letovi = []

    for let in svi_konkretni_letovi:
        if svi_letovi[svi_konkretni_letovi[let]["broj_leta"]]["sifra_odredisnog_aerodroma"] == svi_letovi[konkretni_let["broj_leta"]]["sifra_odredisnog_aerodroma"]:
            if svi_konkretni_letovi[let]["datum_i_vreme_polaska"] >= konkretni_let["datum_i_vreme_dolaska"]:
                if svi_konkretni_letovi[let]["datum_i_vreme_polaska"] <= konkretni_let["datum_i_vreme_dolaska"] + timedelta(minutes=120):
                    letovi.append(svi_konkretni_letovi[let])

    return letovi


"""
Funkcija koja vraća sve konkretne letove čije je vreme polaska u zadatom opsegu, +/- zadati broj fleksibilnih dana
"""
def fleksibilni_polasci(svi_letovi: dict, konkretni_letovi: dict, polaziste: str, odrediste: str,
                        datum_polaska: date, broj_fleksibilnih_dana: int, datum_dolaska: date) -> list:
    
    letovi = []

    datum_manje = datum_polaska - timedelta(days=broj_fleksibilnih_dana)
    datum_vise = datum_polaska + timedelta(days=broj_fleksibilnih_dana)

    for let in konkretni_letovi:
        if konkretni_letovi[let]["datum_i_vreme_polaska"] >= datum_manje and konkretni_letovi[let]["datum_i_vreme_polaska"] <= datum_vise:
            letovi.append(konkretni_letovi[let])

    return letovi