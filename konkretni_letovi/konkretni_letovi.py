from datetime import datetime, timedelta


sifra_konkretnog_leta = 0


def provjera_validnosti_podataka(svi_konkretni_letovi: dict, broj_leta: str, sifra_polazisnog_aerodroma: str, sifra_odredisnog_aerodorma: str,
    vreme_poletanja: str, vreme_sletanja: str, sletanje_sutra: bool, prevoznik: str, dani: list, datum_pocetka_operativnosti: datetime, datum_kraja_operativnosti: datetime):

    # Provjera za unos praznog stringa ili nule
    for key in [broj_leta, sifra_polazisnog_aerodroma, sifra_odredisnog_aerodorma, vreme_poletanja, vreme_sletanja, datum_pocetka_operativnosti, datum_kraja_operativnosti, sletanje_sutra, prevoznik, dani]:
        if key == "":
            return "prazan unos"

    # Provjera za broj leta
    try:
        if not (broj_leta[0:2].isalpha() and broj_leta[2:4].isdigit() and len(broj_leta) == 4):
            return "broj leta"
    except:
        return "broj leta"
    
    # Provjera za sifru polazisnog aerodroma
    try:
        if not (sifra_polazisnog_aerodroma.isalpha() and len(sifra_polazisnog_aerodroma) == 3):
            return "polaziste"
    except:
        return "polaziste"
    
    # Provjera za sifru odredisnog aerodroma
    try:
        if not (sifra_odredisnog_aerodorma.isalpha() and len(sifra_odredisnog_aerodorma) == 3):
            return "odrediste"
    except:
        return "odrediste"

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

    # Provjera za prevoznika
    try:
        if not (prevoznik.isalpha()):
            return "prevoznik"
    except:
        return "prevoznik"

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
    
    # Provjera za datume operativnosti
    try:
        if not (type(datum_pocetka_operativnosti) == datetime and type(datum_kraja_operativnosti)):
            return "datumi operativnosti"
        elif (datum_pocetka_operativnosti > datum_kraja_operativnosti):
            return "pocetak posle kraja"
    except:
        return "datumi operativnosti"

    return "nema greske"


"""
Funkcija koja za zadati konkretni let kreira sve konkretne letove u opsegu operativnosti.
Kao rezultat vraća rečnik svih konkretnih letova koji sadrži nove konkretne letove.
"""
def kreiranje_konkretnog_leta(svi_konkretni_letovi: dict, let: dict) -> dict:
    
    global sifra_konkretnog_leta

    broj_leta = let["broj_leta"]
    datum_pocetka_operativnosti = let["datum_pocetka_operativnosti"]
    datum_kraja_operativnosti = let["datum_kraja_operativnosti"]
    vreme_poletanja = let["vreme_poletanja"]
    vreme_sletanja = let["vreme_sletanja"]
    sletanje_sutra = let["sletanje_sutra"]
    dani = let["dani"]

    while datum_pocetka_operativnosti < datum_kraja_operativnosti: # mozda treba <=, vidi nakon promjene testova
        if (datum_pocetka_operativnosti.weekday() in dani):
            if sletanje_sutra == True and (datum_pocetka_operativnosti + timedelta(days=1)) > datum_kraja_operativnosti:
                continue

            else:
                svi_konkretni_letovi[sifra_konkretnog_leta] = {
                "sifra": sifra_konkretnog_leta,
                "broj_leta": broj_leta,
                "datum_i_vreme_polaska": datetime.combine(datum_pocetka_operativnosti.date(), datetime.strptime(vreme_poletanja, "%H:%M").time()),
                "datum_i_vreme_dolaska": datetime.combine(datum_pocetka_operativnosti.date(), datetime.strptime(vreme_sletanja, "%H:%M").time())
            }
                if sletanje_sutra == True:
                    svi_konkretni_letovi[sifra_konkretnog_leta]["datum_i_vreme_dolaska"] = svi_konkretni_letovi[sifra_konkretnog_leta]["datum_i_vreme_dolaska"] + timedelta(days=1)

            sifra_konkretnog_leta += 1

        datum_pocetka_operativnosti += timedelta(days=1)

    return svi_konkretni_letovi


"""
Funkcija čuva konkretne letove u fajl na zadatoj putanji sa zadatim separatorom. 
"""
def sacuvaj_kokretan_let(putanja: str, separator: str, svi_konkretni_letovi: dict):
    
    with open(putanja, "w") as f:
        for konkretni_let in svi_konkretni_letovi:
            list_ = []

            for key in svi_konkretni_letovi[konkretni_let]:
                if (type(svi_konkretni_letovi[konkretni_let][key]) == datetime):
                    list_.append(svi_konkretni_letovi[konkretni_let][key].strftime("%Y %m %d %H %M %S"))

                elif (type(svi_konkretni_letovi[konkretni_let][key]) == bool):
                    if (svi_konkretni_letovi[konkretni_let][key]):
                        list_.append("1")
                    else:
                        list_.append("0")

                elif (type(svi_konkretni_letovi[konkretni_let][key]) == list):
                    broj_podlisti = len(svi_konkretni_letovi[konkretni_let][key])
                    broj_clanova_podliste = len(svi_konkretni_letovi[konkretni_let][key][0])

                    list_.append(str(broj_podlisti))
                    list_.append(str(broj_clanova_podliste))

                    str_ = ""

                    for i in range(broj_podlisti):
                        for j in range(broj_clanova_podliste):
                            if svi_konkretni_letovi[konkretni_let][key][i][j]:
                                str_ += "1"
                            else:
                                str_ += "0"
                    
                    list_.append(str_)

                else:
                    list_.append(str(svi_konkretni_letovi[konkretni_let][key]))

            line = separator.join(list_)

            f.writelines(line + '\n')


"""
Funkcija učitava konkretne letove iz fajla na zadatoj putanji sa zadatim separatorom.
"""
def ucitaj_konkretan_let(putanja: str, separator: str) -> dict:
    
    dict_ = {}

    with open(putanja, "r") as f:
        for line in f.readlines():
            line = line[:-1]

            list_ = line.split(separator)
            
            zauzetost = []

            for i in range(int(list_[4])):
                zauzetost_ = []

                for j in range(int(list_[5])):
                    zauzetost_.append(bool(int(list_[6][i * int(list_[5]) + j])))
                
                zauzetost.append(zauzetost_)

            dict_[int(list_[0])] = {
                "sifra": int(list_[0]),
                "broj_leta": list_[1],
                "datum_i_vreme_polaska": datetime.strptime(list_[2], "%Y %m %d %H %M %S"),
                "datum_i_vreme_dolaska": datetime.strptime(list_[3], "%Y %m %d %H %M %S"),
                "zauzetost": zauzetost
            }
    
    return dict_

    # Ne mjenjaj ovu funkciju, ona radi pravilno.
    # Test ne prolazi jer je lose napisan (specificno, test pada u redu 88).
    # U testu postoji petlja u kojoj se prolazi kroz svaki clan dict-a ucitani_letovi.
    # Problem je u tome sto sam test tokom prolaska kroz dict ucitani_letovi ga ujedno i mijenja.
    # Dakle, svakim prolazom kroz petlju, dict ucitani_letovi biva promjenjen, te je nemoguce ikada ga referencirati za neku provjeru podataka.
